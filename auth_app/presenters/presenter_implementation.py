import json

from django.http import HttpResponse

from auth_app.interactors.dtos import AuthenticationDto
from auth_app.interactors.presenters.presenter_interface import LoginPresenterInterface, SignupPresenterInterface


class LoginPresenterImplementation(LoginPresenterInterface):
    def get_login_response(self, authentication_dto: AuthenticationDto):
        authentication_details = {
            "access_token": authentication_dto.access_token,
            "is_admin": authentication_dto.is_admin
        }
        json_response = json.dumps(authentication_details)
        http_response = HttpResponse(json_response, status=200)

        return http_response

    def get_username_not_found_http_response(self):
        username_not_found = {
            "response": "Given username not found in database",
            "http_status_code": 404,
            "res_status": "INVALID_USERNAME"
        }
        json_response = json.dumps(username_not_found)
        http_response = HttpResponse(json_response, status=404)

        return http_response

    def get_password_bad_request_http_response(self):
        password_bad_request = {
            "response": "Given password didn't matched with the given username",
            "http_status_code": 400,
            "res_status": "INVALID_PASSWORD"
        }
        json_response = json.dumps(password_bad_request)
        http_response = HttpResponse(json_response, status=400)
        return http_response


class SignupPresenterImplementation(SignupPresenterInterface):
    def get_user_name_already_exist_bad_request_response(self):
        bad_request_response = {
            "response": "Given username already exists",
            "http_status_code": 400,
            "res_status": "USER_NAME_ALREADY_EXISTS"
        }
        json_response = json.dumps(bad_request_response)
        http_response = HttpResponse(json_response, status=400)
        return http_response

    def get_signup_success_responce(self):
        http_response = HttpResponse("signed up successfully", status=201)
        return http_response
