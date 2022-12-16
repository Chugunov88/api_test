import requests

class new_location_test():
    """работа с новой локацией"""

    def test_create_new_location(self):
        """Создание новой локации"""
        for i in range(5):
            base_url = "https://rahulshettyacademy.com/"    # Базовая url
            key = "?key=qaclick123"                         # Параметр для всех запросов
            post_resource = "/maps/api/place/add/json"      # Ресурс метода Post

            """Создание новой локации"""
            post_url = base_url + post_resource + key
            print(post_url)
            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"

            }
            result_post = requests.post(post_url, json=json_for_create_new_location)
            print(result_post.text)
            print("статус код :" + str(result_post.status_code))

            check_post = result_post.json()
            check_info_post = check_post.get("status")
            print("Статус код :" + check_info_post)
            assert check_info_post == "OK"
            print("Статус ответа верен")
            place_id = check_post.get("place_id")
            print("Place id : " + place_id)

            my_file = open("Exersise.txt", "a+")
            my_file.write(place_id + "\n")
            my_file.close()

def check_id():
    my_file = open("Exersise.txt", "r+")
    file_contents = my_file.read()
    print(file_contents)
    list = []
    for line in file_contents.split("\n"):
        if not line.strip():
            continue
        list.append(line.lstrip())
    print(list)

"""Проверка создания новой локации"""
def check_id_from_file():
    base_url = "https://rahulshettyacademy.com/"  # Базовая url
    key = "?key=qaclick123"  # Параметр для всех запросов
    get_resource = "/maps/api/place/get/json"  # Ресурс метода Get

    for k in range (5):
        get_url = base_url + get_resource + key + "&place_id=" + check_id().list[k]
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("статус код :" + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!!! Проверка создания новой локации прошла успешно")
        else:
            print("Провал!!! Запрос ошибочный")





validation_id = new_location_test()
validation_id.test_create_new_location()
check_id()
check_id_from_file()





