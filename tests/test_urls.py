import http


async def test_main_page_get(client):
    response = client.get('/')
    assert response.status_code == http.HTTPStatus.OK
    assert response.json() == {'greeting': 'HELLO MY FRIEND!!!!'}


async def test_main_page_post(client):
    response = client.post('/')
    assert response.status_code == http.HTTPStatus.OK
    assert response.json() == {'greeting': 'HELLO MY FRIEND!!!!'}
