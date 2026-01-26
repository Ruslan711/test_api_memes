from .create_meme import CreateMeme
from .delete_meme import DeleteMeme
from .get_meme import GetMeme
from .update_meme import UpdateMeme


class MemesApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": token, "Content-Type": "application/json"}
        self.create = CreateMeme()
        self.get = GetMeme()
        self.update = UpdateMeme()
        self.delete = DeleteMeme()
        for endpoint in [self.create, self.get, self.update, self.delete]:
            endpoint.headers = self.headers
