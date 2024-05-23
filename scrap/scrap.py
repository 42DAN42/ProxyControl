# Функции для перезагрузки модемов
def reboot_modem_1():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 1
    internal_ip = internal_ips['Modem 1']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_2():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 2
    internal_ip = internal_ips['Modem 2']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_3():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 3
    internal_ip = internal_ips['Modem 3']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_4():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 4
    internal_ip = internal_ips['Modem 5']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_5():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 5
    internal_ip = internal_ips['Modem 5']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_6():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 6
    internal_ip = internal_ips['Modem 6']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_7():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 7
    internal_ip = internal_ips['Modem 7']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_8():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 8
    internal_ip = internal_ips['Modem 8']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'REBOOTER.py', internal_ip])

def reboot_modem_9():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 9
    internal_ip = internal_ips['Modem 9']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python3', 'REBOOTER.py', internal_ip])

def reboot_modem_10():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 10
    internal_ip = internal_ips['Modem 10']

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    run(['python3', 'REBOOTER.py', internal_ip])

# Функции для смены ip
def ch_ip_modem_1():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 1
    internal_ip = internal_ips['Modem 1']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_2():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 2
    internal_ip = internal_ips['Modem 2']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_3():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 3
    internal_ip = internal_ips['Modem 3']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_4():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 4
    internal_ip = internal_ips['Modem 5']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_5():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 5
    internal_ip = internal_ips['Modem 5']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_6():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 6
    internal_ip = internal_ips['Modem 6']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_7():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 7
    internal_ip = internal_ips['Modem 7']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_8():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 8
    internal_ip = internal_ips['Modem 8']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_9():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 9
    internal_ip = internal_ips['Modem 9']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])


def ch_ip_modem_10():
    # Чтение данных из файла internal_ips.json
    with open('../internal_ips.json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для Modem 10
    internal_ip = internal_ips['Modem 10']

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    run(['python', 'CHANGER.py', internal_ip])

change_ip_button.bind("<Button-1>", lambda event: ch_ip_modem_1)
change_ip_button.bind("<Button-2>", lambda event: ch_ip_modem_2)
change_ip_button.bind("<Button-3>", lambda event: ch_ip_modem_3)
change_ip_button.bind("<Button-4>", lambda event: ch_ip_modem_4)
change_ip_button.bind("<Button-5>", lambda event: ch_ip_modem_5)
change_ip_button.bind("<Button-6>", lambda event: ch_ip_modem_6)
change_ip_button.bind("<Button-7>", lambda event: ch_ip_modem_7)
change_ip_button.bind("<Button-8>", lambda event: ch_ip_modem_8)
change_ip_button.bind("<Button-9>", lambda event: ch_ip_modem_9)
change_ip_button.bind("<Button-10>", lambda event: ch_ip_modem_10)