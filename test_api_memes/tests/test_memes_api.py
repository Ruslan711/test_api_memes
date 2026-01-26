import allure


@allure.feature("Memes")
@allure.story("Get all memes")
def test_get_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_status_200()
    get_meme_endpoint.check_data_is_not_empty()


@allure.feature("Memes")
@allure.story("Get single meme")
def test_get_single_meme(new_meme_id, get_meme_endpoint):
    get_meme_endpoint.get_meme(new_meme_id)
    get_meme_endpoint.check_status_200()
    get_meme_endpoint.check_meme_text("Мой первый мем")


@allure.feature("Memes")
@allure.story("Create meme")
def test_create_meme(create_meme_endpoint):
    create_meme_endpoint.create_meme_text(
        text="Мой первый мем",
        url="https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FIST51rB_SJo%2Fmaxresdefault.jpg&lr=10313&pos=27&rpt=simage&text=mems",
        tags=["funny", "ruslan"],
        author="Ruslan"
    )

    create_meme_endpoint.check_status_200()
    create_meme_endpoint.check_meme_text("Мой первый мем")


@allure.feature("Memes")
@allure.story("Update meme")
def test_update_meme(new_meme_id, update_meme_endpoint):
    payload = {
        "id": new_meme_id,
        "text": "Обновлённый мем",
        "url": "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.ytimg.com%2Fvi%2FIST51rB_SJo%2Fmaxresdefault.jpg&lr=10313&pos=27&rpt=simage&text=mems",
        "tags": ["funny", "ruslan"],
        "info": {"author": "Ruslan"}
    }
    update_meme_endpoint.update_put(new_meme_id, payload)
    update_meme_endpoint.check_status_200()
    update_meme_endpoint.check_meme_text("Обновлённый мем")


@allure.feature("Memes")
@allure.story("Delete meme")
def test_delete_meme(new_meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_status_200()
