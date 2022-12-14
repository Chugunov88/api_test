import requests

print("Привет, на какую тему вы хотите шутку?")
i = input("Введите название категории : ")

print("Вы выбрали шутку из категории " + i)
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
if result.status_code == 200:
    print("Ссылка на выбранную категорию сгенерирована")
result.encoding = "utf-8"
# print(result.text)
l = result.text
DONE1 = (l.translate({ord(i): None for i in '"[]'})).split(",", 16)
# print(DONE1)
print(url_2 + i)
result2 = requests.get(url_2 + i)

"""Шутка из выбранной категории"""
if i in DONE1:
    print("Шутка из категории" + "-" + i)
    result2 = requests.get(url_2 + i)
    print("статус код :" + str(result2.status_code))
    result2.encoding = "utf-8"
    print(result2.text)
    assert 200 == result.status_code
    if result.status_code == 200:
        print("Успешно!!! Мы получили новую шутку")
else:
    print("Неверная категория шутки, конец программы")
    quit()

result2.encoding = "utf-8"
check = result2.json()
check_info = check.get("categories")
print(check_info)
check_info_value = check.get("value")
print(check_info_value)
name = "Chuck"
if name in check_info_value:
    print("Chuck присутствует")
else:
    print("Chuck отсутствует")





# if i in check_info:
#     print("Выбранная категория валидная и входит в список категорий шуток")
# else:
#     print("Выбранная категория Неверная!!! и входит в список категорий шуток")
# check_info_value = check.get("value")
# print(check_info_value)
# assert check_info == []
# print("GGGGG")
# check_info_value = check.get("value")
# print(check_info_value)
# name = "Chuck"
# if name in check_info_value:
#     print("Chuck присутствует")
# else:
#     print("Chuck отсутствует")
#


# list = ['blank', 'animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']
# #          0        1         2           3         4         5          6        7         8        9        10       11          12          13          14      15         16
