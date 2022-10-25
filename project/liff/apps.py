from django.apps import AppConfig


class LiffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'liff'

    def ready(self):
        from . import views
        views.start()
