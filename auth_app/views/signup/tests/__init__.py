# pylint: disable=wrong-import-position

APP_NAME = "auth_app"
OPERATION_NAME = "signup"
REQUEST_METHOD = "post"
URL_SUFFIX = "signup/v1/"

from .test_case_01 import TestCase01SignupAPITestCase

__all__ = [
    "TestCase01SignupAPITestCase"
]
