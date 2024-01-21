from .models import Settings
from django.core.cache import cache




def get_settings(request):
    try:
        settings_date = cache.get('settings_date')
    except Exception:
        settings_date = Settings.objects.last()
        cache.set('settings_date',settings_date,60*60*24)

    return {'settings_date':settings_date}