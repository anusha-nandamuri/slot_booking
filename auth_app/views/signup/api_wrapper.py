from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from gyaan import presenters
from .validator_class import ValidatorClass
from ...interactors.signup_interactor import SignupInteractor
from ...presenters.presenter_implementation import SignupPresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    username = request_data["username"]
    password = request_data["password"]
    storage = StorageImplementation()
    presenter = SignupPresenterImplementation()
    interactor = SignupInteractor(storage=storage)
    http_response = interactor.signup_wrapper(username=username, password=password, presenter=presenter)
    return http_response
