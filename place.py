import requests

class new_location_test():
    """работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""

        base_url = "https://rahulshettyacademy.com/"    # Базовая url
        key = "?key=qaclick123"                         # Параметр для всех запросов
        post_resource = "/maps/api/place/add/json"      # Ресурс метода Post

        post_url = base_url + post_resource + key

        json_for_create_new_location = {

        }