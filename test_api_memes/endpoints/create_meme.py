import allure
import requests

from .endpoints import Endpoint


class CreateMeme(Endpoint):
    meme_id = None

    @allure.step("Create meme")
    def create_meme(self, payload, headers=None):
        headers = headers or self.headers
        self.response = requests.post(
            f"http://memesapi.course.qa-practice.com/meme",
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.meme_id = self.json["id"]
        return self.response

    @allure.step("Create meme 2")
    def create_meme_text(self, text, url, tags, author, headers=None):
        payload = {
            "text": text,
            "url": url,
            "tags": tags,
            "info": {"author": author}
        }
        return self.create_meme(payload)
