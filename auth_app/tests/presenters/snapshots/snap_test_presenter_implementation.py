# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['Testlogin.test_get_login_response_returns_user_authentications_details_dto http_response'] = GenericRepr("<HttpResponse status_code=200, "text/html; charset=utf-8">")

snapshots['Testlogin.test_get_username_not_found_http_response http_response'] = GenericRepr("<HttpResponse status_code=404, "text/html; charset=utf-8">")

snapshots['Testlogin.test_get_password_bad_request_http_response http_response'] = GenericRepr("<HttpResponse status_code=400, "text/html; charset=utf-8">")

snapshots['TestSignup.test_get_user_name_already_exist_bad_request_response http_response'] = GenericRepr("<HttpResponse status_code=400, "text/html; charset=utf-8">")

snapshots['TestSignup.test_get_signup_success_responce http_response'] = GenericRepr("<HttpResponse status_code=201, "text/html; charset=utf-8">")
