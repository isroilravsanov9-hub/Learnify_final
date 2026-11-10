# ============================================================================
# Python 3.14+ Compatibility Patch for Django Template BaseContext.__copy__
# In Python 3.14, copy(super()) inside BaseContext returns super object which
# lacks __dict__, causing AttributeError in Django admin template rendering.
# ============================================================================
try:
    import django.template.context as _ctx

    def _patched_basecontext_copy(self):
        duplicate = object.__new__(self.__class__)
        duplicate.__dict__.update(self.__dict__)
        duplicate.dicts = self.dicts[:]
        return duplicate

    _ctx.BaseContext.__copy__ = _patched_basecontext_copy
except Exception:
    pass
