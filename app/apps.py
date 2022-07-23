"""
    - app file
"""
from django.apps import AppConfig


class AppConfig(AppConfig):
    """
        app config class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        """
            - calling app signal
        """
        import app.signals
