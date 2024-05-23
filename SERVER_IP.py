import requests

# Отправляем GET-запрос на сайт для получения IP-адреса
response = requests.get('http://ip.bablosoft.com')

# Извлекаем IP-адрес из текстового ответа сервера
ip_address = response.text.strip()
