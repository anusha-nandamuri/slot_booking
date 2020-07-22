import abc


class LoginPresenterInterface:
    @abc.abstractmethod
    def get_username_not_found_http_response(self):
        pass

    @abc.abstractmethod
    def get_password_bad_request_http_response(self):
        pass

    @abc.abstractmethod
    def get_login_response(self, authentication_dto):
        pass


class SignupPresenterInterface:
    @abc.abstractmethod
    def get_user_name_already_exist_bad_request_response(self):
        pass

    @abc.abstractmethod
    def get_signup_success_responce(self):
        pass