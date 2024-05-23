import tkinter as tk
import json
from SERVER_IP import ip_address
import subprocess

internal_ips_json = 'internal_ips.json'

# Функции для перезагрузки модемов
def reboot_modem(modem_number):
    # Чтение данных из файла internal_ips.json
    with open('internal_ips_json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для указанного модема
    modem_name = 'Modem ' + str(modem_number)
    internal_ip = internal_ips[modem_name]

    # Запуск скрипта REBOOTER.py с передачей значения internal_ip в качестве аргумента
    subprocess.run(['python3', 'REBOOTER.py', internal_ip])

# Функции для смены ip
def ch_ip_modem(modem_name):
    # Чтение данных из файла internal_ips.json
    with open('internal_ips_json', 'r') as f:
        internal_ips = json.load(f)

    # Получение значения IP-адреса для указанного модема
    internal_ip = internal_ips[modem_name]

    # Запуск скрипта CHANGER.py с передачей значения internal_ip в качестве аргумента
    subprocess.run(['python3', 'CHANGER.py', internal_ip])

# Функция для копирования ссылки
def copy_link(event):
    # Получаем номер строки и столбца кнопки, на которую нажали
    row, col = event.widget.grid_info()["row"], event.widget.grid_info()["column"]
    # Находим ячейку со ссылкой по номеру строки
    link_label = event.widget.master.master.children["!frame{}.!label".format(row)]
    # Копируем ссылку в буфер обмена
    link = link_label["text"]
    root.clipboard_clear()
    root.clipboard_append(link)

# Функция для загрузки данных из файла
def load_data():
    try:
        with open('internal_ips_json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

# Функция для сохранения данных в файл
def save_data():
    data = {}
    for row in range(10):
        modem_label = table.grid_slaves(row=row+1, column=0)[0]
        internal_ip = table.grid_slaves(row=row+1, column=1)[0].get()
        data[modem_label["text"]] = internal_ip
    with open('internal_ips_json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

# Создаем окно
root = tk.Tk()
root.title("Управление модемами")

# Создаем таблицу
table = tk.Frame(root)
table.pack(pady=10)

# Заголовки столбцов
headers = ["Modem", "Внутренний IP", "Внешний IP", "Ссылка", "Действия"]

# Создаем ячейки таблицы
data = load_data()
for row in range(10):
    # Создаем ячейки с названием модема
    modem_label = tk.Label(table, text="Modem {}".format(row+1))
    modem_label.grid(row=row+1, column=0)

    # Создаем ячейки с IP-адресами
    internal_ip = tk.Entry(table, width=15)
    internal_ip.insert(0, data.get("Modem {}".format(row+1), ""))
    internal_ip.grid(row=row+1, column=1)

    external_ip = tk.Entry(table, width=15)
    external_ip.grid(row=row+1, column=2)

    # Создаем ячейку со ссылкой
    link_label = tk.Label(table, text="https://example.com/modem{}".format(row+1))
    link_label.grid(row=row+1, column=3)

    # Создаем ячейку с кнопками действий
    actions_frame = tk.Frame(table)
    actions_frame.grid(row=row+1, column=4)

    # Создаем кнопки действий
    restart_button = tk.Button(actions_frame, text="R_Modem_{}".format(row + 1), width=10)
    restart_button.pack(side=tk.LEFT, padx=(10, 5))
    restart_button.bind("<Button-1>", lambda event, modem_number=row + 1: reboot_modem(modem_number))

    change_ip_button = tk.Button(actions_frame, text="CH_IP_{}".format(row + 1), width=10)
    change_ip_button.pack(side=tk.LEFT, padx=5)
    change_ip_button.bind("<Button-1>", lambda event, row=row + 1: globals()["ch_ip_modem_{}".format(row)]())

    change_network_button = tk.Button(actions_frame, text="CH_NET_{}".format(row + 1), width=10)
    change_network_button.pack(side=tk.LEFT, padx=5)

    copy_link_button = tk.Button(actions_frame, text="C_URL_{}".format(row + 1), width=10)
    copy_link_button.pack(side=tk.LEFT, padx=5)
    copy_link_button.bind("<Button-1>", copy_link)

# Создаем заголовки
for col, header in enumerate(headers):
    header_label = tk.Label(table, text=header)
    header_label.grid(row=0, column=col, sticky="we")

# Создаем ячейку с сервером
server_ip_label = tk.Label(table, text="Server IP")
server_ip_label.grid(row=11, column=0)

# Создаем ячейку с получением IP
server_ip_entry = tk.Entry(table, width=15)
server_ip_entry.grid(row=11, column=1)

get_ip_button = tk.Button(table, text="Получить IP", command=lambda: server_ip_entry.insert(0, SERVER_IP))
get_ip_button.grid(row=11, column=2)

# Создаем кнопку "Save"
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack(side=tk.RIGHT, padx=10)

# Перемещаем ячейку с сервером
server_ip_label.grid(row=12, column=0)
server_ip_entry.grid(row=12, column=1)
get_ip_button.grid(row=12, column=2)

# Запускаем цикл обработки событий
root.mainloop()
