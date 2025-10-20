from django.apps import AppConfig


class TheblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theblog'

    def ready(self):
        import theblog.signals
