from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - "arranjo - configuração para o teste"
    - A: Act     - "Executa a coisa (o SUT)"
    - A: Assert  - "Garante que A é A"
    :return:
    """
    # arrange
    # client = TestClient(app)
    # act
    response = client.get('/')
    # assert
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


def test_root_deve_retornar_exercicio(client):
    # client = TestClient(app)

    response = client.get('/exercicio')

    assert response.json() == {'message': 'checando exercicio'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'alice@example.com',
                'username': 'alice',
            }
        ],
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_user_not_created(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_select_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_selected_user_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_user_deleted_not_created(client):
    response = client.delete(
        '/users/2',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
