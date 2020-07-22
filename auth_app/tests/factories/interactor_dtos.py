# import datetime
#
# import factory
#
# from common.dtos import UserAuthTokensDTO
#
# from auth_app.interactors.dtos import AuthenticationDto
#
#
# class UserAuthTokensDTOFactory(factory.Factory):
#     class Meta:
#         model = UserAuthTokensDTO
#
#     now = factory.LazyFunction(datetime.datetime.utcnow)
#     user_id = factory.sequence(lambda a: a)
#     access_token = factory.sequence(lambda a: 'mytoken' + a)
#     refresh_token = factory.sequence(lambda a: 'refreshtoken' + a)
#     expires_in = factory.LazyAttribute(lambda o: o.now + datetime.timedelta(hours=1))
#
#
# class AuthenticationDtoFactory(factory.Factory):
#     class Meta:
#         model = AuthenticationDto
#
#     access_token = factory.sequence(lambda a: 'mytoken'+ a)
#
# class UserIdentityDtoFactory(factory.Factory):
#     class Meta:
#         model = AuthenticationDto
#
#     user_id = factory.sequence(lambda a: a)
#
