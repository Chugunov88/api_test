import requests

class Joke_tests():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def get_list_of_all_categories(self):
        """Получение списка всех категорий шуток"""


    url = "https://api.chucknorris.io/jokes/categories"
    url_2 = "https://api.chucknorris.io/jokes/random?category="
    print(url)
    result = requests.get(url)
    print("статус код :" + str(result.status_code))
    assert 200 == result.status_code
    if result.status_code == 200:
        print("Успешно!!! Мы получили список всех категорий шуток")
    else:
        print("Провал!!! Запрос ошибочный")
    result.encoding = "utf-8"
    print(result.text)


    def get_jokes_from_categories(self):
        """Шутки из категорий"""
        url = "https://api.chucknorris.io/jokes/categories"
        url_2 = "https://api.chucknorris.io/jokes/random?category="
        result = requests.get(url)
        print("статус код :" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно!!! Мы получили по 1 шутке из каждой категории")
        else:
            print("Провал!!! Запрос ошибочный")
        result.encoding = "utf-8"
        print(result.text)
        l = result.text
        DONE1 = (l.translate({ord(i): None for i in '"[]'})).split(",", 16)
        print(DONE1)
        for i in DONE1:
            print("Шутка из категории" + "-" + i)
            result2 = requests.get(url_2 + i)
            print(str(i))
            print("статус код :" + str(result2.status_code))
            assert 200 == result.status_code
            if result.status_code == 200:
                print("Успешно!!! Мы получили новую шутку")
            else:
                print("Провал!!! Запрос ошибочный")
            result2.encoding = "utf-8"
            print(result2.text)
            check = result2.json()
            check_info = check.get("categories")
            assert check_info == [i]
            print("Категория верна")
            check_info_value = check.get("value")
            print(check_info_value)
            name = "Chuck"
            if name in check_info_value:
                print("Chuck присутствует")
            else:
                print("Chuck отсутствует")




get_all_categories = Joke_tests()
get_all_categories.get_jokes_from_categories()
# get_all_categories.get_list_of_all_categories()