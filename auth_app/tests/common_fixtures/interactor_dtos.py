import datetime

import factory

from common.dtos import UserAuthTokensDTO

from auth_app.interactors.dtos import AuthenticationDto


class UserAuthTokensDTOFactory:
    class Meta:
        model = UserAuthTokensDTO

    now = factory.LazyFunction(datetime.datetime.utcnow)
    user_id = factory.sequence(lambda a: a)
    access_token = factory.sequence(lambda a: 'mytoken' + a)
    refresh_token = factory.sequence(lambda a: 'refreshtoken' + a)
    expires_in = factory.LazyAttribute(lambda o: o.now + datetime.timedelta(hours=1))


class AuthenticationDtoFactory:
    class Meta:
        model = AuthenticationDto

    access_token = factory.sequence(lambda a: 'mytoken'+ a)
