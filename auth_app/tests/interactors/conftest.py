import pytest
import datetime

# from auth_app.tests.factories.interactor_dtos import UserAuthTokensDTOFactory, UserIdentityDtoFactory
from auth_app.interactors.storages.dtos import UserIdentityDto
from common.dtos import UserAuthTokensDTO


@pytest.fixture()
def access_token_dto():
    access_token_dto = UserAuthTokensDTO(
        access_token="mytoken",
        user_id=1,
        refresh_token="refresh token",
        expires_in = datetime.datetime(2020,10,1)
    )
    return access_token_dto


@pytest.fixture()
def user_identity_dto():
    user_identity_dto = UserIdentityDto(user_id=1, is_admin=False)
    return user_identity_dto
