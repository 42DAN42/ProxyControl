# Импортируем библиотеку pickle для сохранения и загрузки данных
import pickle

# Создаем словарь для хранения IP-адресов
ip_dict = {}

# Функция для сохранения IP-адресов в файл
def save_ips():
    with open('ip_data.pickle', 'wb') as f:
        pickle.dump(ip_dict, f)

# Функция для загрузки IP-адресов из файла
def load_ips():
    global ip_dict
    try:
        with open('ip_data.pickle', 'rb') as f:
            ip_dict = pickle.load(f)
    except FileNotFoundError:
        pass

# Функция для получения всех IP-адресов
def get_all_ips():
    return ip_dict

# Функция для получения внешнего IP-адреса по номеру модема
def get_external_ip(modem_number):
    return ip_dict.get("ext_ip_{}".format(modem_number))

# Функция для получения внутреннего IP-адреса по номеру модема
def get_internal_ip(modem_number):
    return ip_dict.get("modem_ip_{}".format(modem_number))

# Функция для сохранения внешнего IP-адреса по номеру модема
def save_external_ip(modem_number, ip_address):
    ip_dict["ext_ip_{}".format(modem_number)] = ip_address
    save_ips()

# Функция для сохранения внутреннего IP-адреса по номеру модема
def save_internal_ip(modem_number, ip_address):
    ip_dict["modem_ip_{}".format(modem_number)] = ip_address
    save_ips()

# Загружаем IP-адреса из файла при импорте модуля
load_ips()
