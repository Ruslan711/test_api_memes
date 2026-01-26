import pytest

from .endpoints.authorize import Authorize
from .endpoints.create_meme import CreateMeme
from .endpoints.delete_meme import DeleteMeme
from .endpoints.get_meme import GetMeme
from .endpoints.update_meme import UpdateMeme


@pytest.fixture(scope="session")
def auth_token():
    auth = Authorize()

    if auth.token and auth.check_token(auth.token):
        return auth.token

    token = auth.authorize(name="Ruslan")
    return token


@pytest.fixture()
def create_meme_endpoint(auth_token):
    client = CreateMeme()
    client.headers["Authorization"] = auth_token
    return client


@pytest.fixture()
def get_meme_endpoint(auth_token):
    client = GetMeme()
    client.headers["Authorization"] = auth_token
    return client


@pytest.fixture()
def update_meme_endpoint(auth_token):
    client = UpdateMeme()
    client.headers["Authorization"] = auth_token
    return client


@pytest.fixture()
def delete_meme_endpoint(auth_token):
    client = DeleteMeme()
    client.headers["Authorization"] = auth_token
    return client


@pytest.fixture()
def new_meme_id(create_meme_endpoint, delete_meme_endpoint):
    create_meme_endpoint.create_meme_text(
        text="Мой первый мем",
        url="https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FIST51rB_SJo%2Fmaxresdefault.jpg&lr=10313&pos=27&rpt=simage&text=mems",
        tags=["funny", "ruslan"],
        author="Ruslan"
    )
    meme_id = create_meme_endpoint.meme_id
    yield meme_id
    delete_meme_endpoint.delete_meme(meme_id)
