from django.apps import AppConfig


class AuthAppAppConfig(AppConfig):
    name = "auth_app"

    def ready(self):
        from auth_app import signals # pylint: disable=unused-variable
