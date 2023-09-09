from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.tests.user_finder import UserFinderSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"name":"MyTest", "username":"MyTest"}

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    print()
    print()
    print(response)
    print(response.body)
    print(response.status_code)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None