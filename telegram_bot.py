import json
import logging
import threading
import time
import urllib.parse
import urllib.request
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = '8957411415:AAEhNbw_-mGuyiLG1zxCbd7cavng9AOiqhE'
TELEGRAM_BOT_USERNAME = 'computer12super_bot'
TEACHER_CHAT_ID = '8623359226'


def send_telegram_raw_message(chat_id, text, reply_markup=None):
    """
    Telegram bot orqali istalgan chat_id ga xabar yuborish.
    """
    def _send():
        try:
            params = {
                'chat_id': str(chat_id),
                'text': text,
                'parse_mode': 'HTML',
            }
            if reply_markup:
                params['reply_markup'] = json.dumps(reply_markup)

            data = urllib.parse.urlencode(params).encode('utf-8')
            url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
            req = urllib.request.Request(url, data=data, method='POST')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            with urllib.request.urlopen(req, timeout=10) as resp:
                resp.read()
        except Exception as e:
            logger.error(f"[Telegram Send Error] {e}")

    t = threading.Thread(target=_send, daemon=True)
    t.start()


def notify_teacher_new_request(user, profile):
    """
    O'qituvchi (Teacher / Admin) ga yangi taklifnoma so'rovi kelganida xabar yuborish.
    """
    now = timezone.now().strftime('%d.%m.%Y %H:%M')
    text = (
        f"⚡️ <b>YANGI O'QUVCHI TAKLIFNOMASI (PRIGLASHENIYA)!</b>\n\n"
        f"👤 <b>F.I.Sh:</b> {user.first_name or user.username}\n"
        f"📧 <b>Email:</b> {user.email}\n"
        f"👥 <b>Guruhi:</b> {profile.group_name}\n"
        f"📚 <b>Yo'nalishi:</b> {profile.direction}\n"
        f"🔑 <b>Parol tekshirildi:</b> ✅ Tasdiqlangan\n"
        f"🕐 <b>Vaqt:</b> {now}\n\n"
        f"<i>O'qituvchi boshqaruv panelida (Teacher Dashboard) kutmoqda. Talabani qabul qilish uchun panelga o'ting:</i>\n"
        f"🔗 <a href='http://127.0.0.1:8000/teacher/'>Teacher Dashboardga o'tish</a>"
    )
    send_telegram_raw_message(TEACHER_CHAT_ID, text)


def notify_student_approved(user, profile, login=None, password=None):
    """
    O'qituvchi talabani qabul qilganda talabaga ustoz belgilagan Login va Parolni yuborish.
    """
    final_login = login or user.username or user.email
    final_password = password or profile.telegram_auth_code or "O'qituvchi tasdiqlagan parol"

    text = (
        f"🎉 <b>XUSHXABAR! SIZ PLATFORMAGA QABUL QILINDINGIZ!</b> 🎉\n\n"
        f"Hurmatli <b>{user.first_name or user.username}</b>!\n"
        f"Ustoz sizning taklifnomangizni <b>QABUL QILDI</b> va siz uchun shaxsiy hisob ochdi! ✅\n\n"
        f"🔑 <b>SIZNING TIZIMGA KIRISH MA'LUMOTLARINGIZ:</b>\n"
        f"📧 <b>Login:</b> <code>{final_login}</code>\n"
        f"🔐 <b>Parol:</b> <code>{final_password}</code>\n\n"
        f"🌐 <b>Saytga kirish havolasi:</b> <a href='http://127.0.0.1:8000/login/'>Learnify Login Sahifasi</a>\n\n"
        f"Ushbu login va parolni kiritib hoziroq barcha darslarni boshlashingiz mumkin! 🚀"
    )

    if profile.telegram_chat_id:
        send_telegram_raw_message(profile.telegram_chat_id, text)
    else:
        # Agar talaba chat_id si bo'lmasa, ustozga ham yuboriladi
        send_telegram_raw_message(TEACHER_CHAT_ID, f"🔔 Talaba {user.first_name} qabul qilindi.\nLogin: <code>{final_login}</code>\nParol: <code>{final_password}</code>")


def notify_student_rejected(user, profile):
    """
    O'qituvchi a'zolikni rad etganda talabaga xabar berish.
    """
    if profile.telegram_chat_id:
        text = (
            f"ℹ️ <b>A'zolik So'rovi Holati</b>\n\n"
            f"Hurmatli <b>{user.first_name or user.username}</b>,\n"
            f"Sizning Learnify platformasidagi so'rovingiz ustoz tomonidan ko'rib chiqildi va rad etildi.\n"
            f"Qo'shimcha ma'lumot olish uchun o'qituvchingizga murojaat qiling."
        )
        send_telegram_raw_message(profile.telegram_chat_id, text)


# ============================================================================
# TELEGRAM BOT BACKGROUND POLLING LISTENER
# ============================================================================
_listener_thread = None
_last_update_id = 0


def _telegram_bot_polling_loop():
    global _last_update_id
    from django.contrib.auth.models import User
    from Courses.models import UserProfile

    logger.info("[Telegram Bot] Polling listener started for @%s", TELEGRAM_BOT_USERNAME)

    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates?offset={_last_update_id + 1}&timeout=15"
            req = urllib.request.Request(url, headers={'User-Agent': 'LearnifyBotService/1.0'})
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = json.loads(resp.read().decode('utf-8'))

            if data.get('ok') and data.get('result'):
                for item in data['result']:
                    _last_update_id = item['update_id']
                    msg = item.get('message')
                    if not msg:
                        continue

                    chat_id = msg.get('chat', {}).get('id')
                    text = (msg.get('text') or '').strip()
                    sender_name = msg.get('from', {}).get('first_name', "Foydalanuvchi")

                    if not chat_id or not text:
                        continue

                    # /start tekshiruvi (IMMENNO O'SHA TELEGRAM USERGA O'Z PAROLINI BERISH)
                    if text.startswith('/start'):
                        parts = text.split()
                        target_user = None
                        sender_username = (msg.get('from', {}).get('username') or '').strip().lstrip('@').lower()

                        # 1. Havoladagi auth_ parametri orqali qidirish
                        if len(parts) > 1:
                            param = parts[1].strip()
                            if param.startswith('auth_'):
                                try:
                                    uid = int(param.replace('auth_', ''))
                                    target_user = User.objects.filter(id=uid).first()
                                except Exception:
                                    pass

                        # 2. IMMENNO sender_username (Telegram Username) bo'yicha qidirish
                        if not target_user and sender_username:
                            profile_match = UserProfile.objects.filter(telegram_username__iexact=sender_username).order_by('-id').first()
                            if profile_match:
                                target_user = profile_match.user

                        # 3. Agar mavjud bo'lsa chat_id bo'yicha qidirish
                        if not target_user:
                            profile_match = UserProfile.objects.filter(telegram_chat_id=str(chat_id)).first()
                            if profile_match:
                                target_user = profile_match.user

                        # AGAR IMMENNO O'SHA RO'YXATDAN O'TGAN USER BO'LSA:
                        if target_user and hasattr(target_user, 'profile'):
                            import random
                            profile = target_user.profile
                            profile.telegram_chat_id = str(chat_id)
                            if sender_username and not profile.telegram_username:
                                profile.telegram_username = sender_username
                            if not profile.telegram_auth_code:
                                profile.telegram_auth_code = str(random.randint(100000, 999999))
                            target_user.set_password(profile.telegram_auth_code)
                            target_user.save()
                            profile.save(update_fields=['telegram_chat_id', 'telegram_username', 'telegram_auth_code'])

                            code = profile.telegram_auth_code

                            reply_text = (
                                f"👋 <b>Assalomu alaykum, {target_user.first_name or sender_name}!</b>\n\n"
                                f"🎓 <b>Learnify</b> platformasiga xush kelibsiz!\n"
                                f"✅ Sizning Telegram hisobingiz (<b>@{sender_username or target_user.username}</b>) tasdiqlandi!\n\n"
                                f"🔐 <b>Siz uchun maxsus bir martalik parol:</b>\n"
                                f"👉 <code>{code}</code> 👈\n\n"
                                f"📋 <i>Ushbu parolni nusxalab platformadagi ro'yxatdan o'tish sahifasiga kiriting. Shundan so'ng ustozga taklifnomangiz (priglasheniya) yuboriladi!</i>"
                            )
                        else:
                            # AGAR BEGONA ODAM BO'LSA VA RO'YXATDAN O'TMAGAN BO'LSA:
                            # Boshqa foydalanuvchilarning paroli hech qachon berilmaydi!
                            user_tag = f"@{sender_username}" if sender_username else "username o'rnatilmagan"
                            reply_text = (
                                f"👋 <b>Assalomu alaykum, {sender_name}!</b>\n\n"
                                f"⚠️ <b>DIQQAT:</b> Sizning ushbu Telegram hisobingiz (<b>{user_tag}</b>) orqali Learnify saytida hali ro'yxatdan o'tilmagan!\n\n"
                                f"🔒 Platforma xavfsizligi tufayli har bir talabaning paroli faqat saytda ro'yxatdan o'tgan o'sha Telegram akkauntiga beriladi.\n\n"
                                f"Iltimos, avval platformamizga kirib ro'yxatdan o'ting:\n"
                                f"🌐 <a href='http://127.0.0.1:8000/register/'>Learnify Ro'yxatdan O'tish Sahifasi</a>\n\n"
                                f"<i>Ro'yxatdan o'tishda 'Telegram Username' maydoniga aynan ushbu {user_tag} hisobingizni yozing!</i>"
                            )

                        send_telegram_raw_message(chat_id, reply_text)

                    elif '@' in text:
                        email_input = text.strip().lower()
                        user_obj = User.objects.filter(email__iexact=email_input).first()
                        if user_obj and hasattr(user_obj, 'profile'):
                            profile = user_obj.profile
                            profile.telegram_chat_id = str(chat_id)
                            profile.save(update_fields=['telegram_chat_id'])
                            code = profile.telegram_auth_code or "123456"
                            reply_text = (
                                f"✅ <b>Foydalanuvchi topildi:</b> {user_obj.first_name}\n\n"
                                f"🔐 Sizning tasdiqlash parolingiz:\n"
                                f"👉 <code>{code}</code> 👈\n\n"
                                f"Ushbu parolni saytga kiriting!"
                            )
                        else:
                            reply_text = f"❌ Ushbu email (<code>{email_input}</code>) bo'yicha so'rov topilmadi."
                        send_telegram_raw_message(chat_id, reply_text)

                    elif text.lower() in ['parol', 'kod', 'password', 'code']:
                        profile_match = UserProfile.objects.filter(telegram_chat_id=str(chat_id)).first()
                        if not profile_match:
                            profile_match = UserProfile.objects.filter(approval_status__in=['pending_telegram', 'pending_teacher']).order_by('-id').first()

                        if profile_match:
                            reply_text = (
                                f"🔐 Sizning tasdiqlash parolingiz:\n"
                                f"👉 <code>{profile_match.telegram_auth_code}</code> 👈\n\n"
                                f"Ushbu parolni saytga kiriting!"
                            )
                        else:
                            reply_text = "Iltimos, avval saytdan ro'yxatdan o'ting: http://127.0.0.1:8000/register/"
                        send_telegram_raw_message(chat_id, reply_text)

        except Exception as e:
            time.sleep(3)


def start_bot_background_listener():
    global _listener_thread
    if _listener_thread is None or not _listener_thread.is_alive():
        _listener_thread = threading.Thread(target=_telegram_bot_polling_loop, daemon=True, name="LearnifyTelegramBotListener")
        _listener_thread.start()
