import requests
import logging
from xml.etree import ElementTree
import time
import os
import json

# Загружаем данные из файла internal_ips.json
#with open('internal_ips.json', 'r', encoding='utf-8-sig') as f:
with open('C:\Python27\proxy\Small\internal_ips.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# Получаем IP-адрес модема №7 из данных файла internal_ips.json
internal_ip = data['Modem 7']

# Выводим данные в терминал
print(f"Loaded internal IP: {internal_ip}")

log_file_path = 'C:\\Python27\\proxy\\network_switch.log'
if not os.path.exists(log_file_path):
    print(f'File {log_file_path} does not exist')
    log_dir = os.path.dirname(log_file_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    open(log_file_path, 'a').close()  # создание пустого файла
    print(f'Created file {log_file_path}')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)


# Указываем URL для запроса на получение токена
url = "http://{}/api/webserver/SesTokInfo".format(internal_ip)

# задаем URL-адрес, по которому будет производиться переключение сети
url_switch = "http://{}/api/net/net-mode".format(internal_ip)

# задаем интервал между переключением сети (в секундах)
interval = 1

# задаем целевой тип сети
target_network_3g = "02"
target_network_4g = "03"

failed_attempts = 0
while True:
    try:
        # получаем токен и идентификатор сессии
        response = requests.get(url)
        root = ElementTree.fromstring(response.content)
        if root.find("TokInfo") is None:
            error_message = "Error occurred: TokInfo element not found in response"
            logging.error(error_message)
            failed_attempts += 1
            if failed_attempts > 5:
                break
            time.sleep(interval)
            continue
        token = root.find("TokInfo").text
        session_id = root.find("SesInfo").text

        # получаем текущую сеть
        response = requests.get(url_switch, headers={
            'Content-Type': 'text/xml',
            '__RequestVerificationToken': token,
            'Cookie': session_id
        })
        root = ElementTree.fromstring(response.content)
        current_mode = root.find("NetworkMode").text

        # переключаемся на 3G, если текущая сеть не 3G
        if current_mode != target_network_3g:
            payload = f'<request><NetworkMode>{target_network_3g}</NetworkMode><NetworkBand>3FFFFFFF</NetworkBand><LTEBand>7FFFFFFFFFFFFFFF</LTEBand></request>'
            response = requests.post(url_switch, data=payload, headers={
                'Content-Type': 'text/xml',
                '__RequestVerificationToken': token,
                'Cookie': session_id
            })

            # добавляем обработку ошибок
            if response.status_code != 200:
                error_message = f"Error occurred while switching to network {target_network_3g}. Response code: {response.status_code}"
                logging.error(error_message)
                failed_attempts += 1
                if failed_attempts > 5:
                    break
            else:
                success_message = f"Switched to network {target_network_3g}"
                logging.info(success_message)
                failed_attempts = 0

            time.sleep(interval)
            continue

        # получаем текущую сеть
        response = requests.get(url_switch, headers={
            'Content-Type': 'text/xml',
            '__RequestVerificationToken': token,
            'Cookie': session_id
        })
        root = ElementTree.fromstring(response.content)
        current_mode = root.find("NetworkMode").text

        # переключаемся на 4G, если текущая сеть не 4G
        if current_mode != target_network_4g:
            payload = f'<request><NetworkMode>{target_network_4g}</NetworkMode><NetworkBand>3FFFFFFF</NetworkBand><LTEBand>7FFFFFFFFFFFFFFF</LTEBand></request>'
            response = requests.post(url_switch, data=payload, headers={
                'Content-Type': 'text/xml',
                '__RequestVerificationToken': token,
                'Cookie': session_id
            })

            # добавляем обработку ошибок
            if response.status_code != 200:
                error_message = f"Error occurred while switching to network {target_network_4g}. Response code: {response.status_code}"
                logging.error(error_message)
                failed_attempts += 1
                if failed_attempts > 5:
                    break
            else:
                success_message = f"Switched to network {target_network_4g}"
                logging.info(success_message)
                failed_attempts = 0
                break

            time.sleep(interval)
            continue

    except Exception as e:
        # Если произошла ошибка, ждем заданный интервал времени и повторяем попытку
        total_error_message = f"Error occurred: {str(e)}"
        logging.exception(total_error_message)
        failed_attempts += 1
        if failed_attempts > 5:
            break

    else:
        success_message = f"Switched to network {target_network_4g}"
        logging.info(success_message)
        failed_attempts = 0
        break