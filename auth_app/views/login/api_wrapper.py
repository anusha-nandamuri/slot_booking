from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from common.oauth2_storage import OAuth2SQLStorage
from .validator_class import ValidatorClass
from ...interactors.login_interactor import LoginInteractor
from ...presenters.presenter_implementation import LoginPresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    storage = StorageImplementation()
    oauth_storage = OAuth2SQLStorage()
    presenter = LoginPresenterImplementation()
    interactor = LoginInteractor(storage=storage, oauth_storage=oauth_storage)
    http_response = interactor.login_wrapper(username=username, password=password, presenter=presenter)
    return http_response
