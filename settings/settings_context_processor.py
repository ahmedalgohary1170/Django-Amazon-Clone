from .models import Settings



def get_settings(request):
    date = Settings.objects.last()

    return {'settings_date':date}