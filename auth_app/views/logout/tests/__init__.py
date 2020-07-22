# pylint: disable=wrong-import-position

APP_NAME = "auth_app"
OPERATION_NAME = "logout"
REQUEST_METHOD = "delete"
URL_SUFFIX = "logout/v1/"

from .test_case_01 import TestCase01LogoutAPITestCase

__all__ = [
    "TestCase01LogoutAPITestCase"
]
