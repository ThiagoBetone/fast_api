from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - "arranjo - configuração para o teste"
    - A: Act     - "Executa a coisa (o SUT)"
    - A: Assert  - "Garante que A é A"
    :return:
    """
    # arrange
    client = TestClient(app)
    # act
    response = client.get('/')
    # assert
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK
