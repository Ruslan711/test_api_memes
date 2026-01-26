import allure


class Endpoint:
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    @allure.step("Check status is 200")
    def check_status_200(self):
        assert self.response.status_code == 200

    @allure.step("Check data is not empty")
    def check_data_is_not_empty(self):
        assert self.json["data"]

    @allure.step("Check meme text")
    def check_meme_text(self, expected_text):
        assert self.json["text"] == expected_text
