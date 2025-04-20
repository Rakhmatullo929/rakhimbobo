from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    
    def ready(self):
        """Import template tags to ensure they are registered."""
        import core.templatetags.custom_filters  # noqa
