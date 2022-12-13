import requests

print("Для вывода шутки из категории введите: 1 - animal, 2 - career, 3 - celebrity, 4 - dev, 5 - explicit, 6 - fashion, 7 - food, 8 - history, 9 - money, 10 - movie, 11 - music, 12 - political, 13- religion, 14 - science, 15 - sport, 16 - travel")
list = ['blank', 'animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
#          0        1         2           3         4         5          6        7         8        9        10       11          12          13          14      15         16
i = int(input())
if 0 < i <= 16:
    print("Вы выбрали шутку из категории " + list[i])
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

    result = requests.get(url)
    print("статус код :" + str(result.status_code))
    assert 200 == result.status_code
    if result.status_code == 200:
        print("Успешно!!! Мы получили ссылку нужной нам категории")
    else:
        print("Провал!!! Запрос ошибочный")
    result.encoding = "utf-8"
    # print(result.text)
    l = result.text
    DONE1 = (l.translate({ord(i): None for i in '"[]'})).split(",", 16)
    # print(DONE1)
    print(url_2 + list[i])
    result2 = requests.get(url_2 + list[i])

    """Шутка из выбранной категории"""
    print("Шутка из категории" + "-" + list[i])
    result2 = requests.get(url_2 + list[i])
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
    print(check_info)

    if list[i] in check_info:
        print("Выбранная категория валидная и входит в список категорий шуток")
    check_info_value = check.get("value")
    print(check_info_value)
    name = "Chuck"
    if name in check_info_value:
        print("Chuck присутствует")
    else:
        print("Chuck отсутствует")

else:
    print('Некорректные данные')


