"""
# TODO: Update test case description
# test login when given valid details
"""
from datetime import datetime
from unittest.mock import patch

from django_swagger_utils.utils.test import CustomAPITestCase

from auth_app.utils.custom_test_utils import CustomTestUtils
from common.dtos import UserAuthTokensDTO
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "user1",
    "password": "password1"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01LoginAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
    def test_case(self, patch_obj):
        user_access_token_dto = UserAuthTokensDTO(
            user_id=1,
            access_token="my_token",
            refresh_token="my_refersh_token",
            expires_in=datetime(2021, 5, 27, 0, 0)
        )
        OAuthUserAuthTokensService.create_user_auth_tokens.return_value = user_access_token_dto
        self.create_single_user(username="user1", password="password1")
        self.default_test_case()
