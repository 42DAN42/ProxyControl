import requests
from xml.etree import ElementTree
from main import internal_ip

# Получаем IP-адрес модема


# Указываем URL для запроса на получение токена
url = "http://{}/api/webserver/SesTokInfo".format(internal_ip)

# Отправляем запрос на получение токена
response = requests.get(url)

# Парсим XML-ответ и получаем токен и идентификатор сессии
root = ElementTree.fromstring(response.text)
token = root.find("TokInfo").text
session_id = root.find("SesInfo").text

# Указываем URL для перезагрузки модема
url = "http://{}/api/device/control".format(internal_ip)

# Параметры для запроса на перезагрузку модема
payload = "<request><Control>1</Control></request>"
headers = {
    'Content-Type': 'text/xml',
    '__RequestVerificationToken': token,
    'Cookie': session_id
}

# Отправляем запрос на перезагрузку модема
response = requests.post(url, data=payload, headers=headers)

# Выводим результат запроса
print(response.text)
