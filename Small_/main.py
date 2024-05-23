import json
import tkinter as tk
import subprocess

# Создаем список процессов и флагов
processes = []
flags = []

for i in range(10):
    # Создаем процесс и флаг для каждого модема
    process = subprocess.Popen(['python', f'C:\Python27\proxy\Small\ACTIVATOR{i+1}.py'])
    flag = True
    processes.append(process)
    flags.append(flag)

for process in processes:
    process.terminate()

# Функция для загрузки данных из файла
def load_data():
    try:
        with open('C:\Python27\proxy\Small\internal_ips.json', 'r', encoding='utf-8-sig') as f:
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
    with open('C:\Python27\proxy\Small\internal_ips.json', 'w', encoding='utf-8-sig') as f:
        json.dump(data, f)

# Создаем окно
window = tk.Tk()
window.title("Modem IP Addresses")

# Создаем таблицу
table = tk.Frame(window)
table.grid(row=0, column=0)

# Создаем подписи модемов
for i in range(10):
    modem_label = tk.Label(table, text="Modem {}".format(i+1))
    modem_label.grid(row=i+1, column=0)

    # Создаем квадратную кнопку
    button = tk.Button(table, text="OFF", bg="red", fg="white", width=5)
    button.grid(row=i+1, column=2)

    # Добавляем обработчик нажатия на кнопку
    button.config(command=lambda button=button, index=i: toggle_button(button, index))

def toggle_button(button, index):
    global processes, flags
    if flags[index]:
        # Останавливаем процесс и меняем флаг
        processes[index].kill()
        flags[index] = False
        button.config(text="OFF", bg="red")
    else:
        # Запускаем процесс и меняем флаг
        processes[index] = subprocess.Popen(['python', f'C:\Python27\proxy\Small\ACTIVATOR{index+1}.py'])
        flags[index] = True
        button.config(text="ON", bg="green")

# Загружаем данные из файла
data = load_data()

# Заполняем таблицу данными
for i, (label, ip) in enumerate(data.items()):
    label_widget = table.grid_slaves(row=i+1, column=0)[0]
    ip_entry = tk.Entry(table)
    ip_entry.insert(0, ip)
    ip_entry.grid(row=i+1, column=1)

# Создаем подпись "Log" и поле для ввода пути к файлу
log_label = tk.Label(table, text="Log")
log_label.grid(row=11, column=0)
log_entry = tk.Entry(table)
log_entry.grid(row=11, column=1)
log_entry.bind("<Enter>", lambda event: table.after(500, lambda: table_tooltip(table, "File_path to network_switch.log", log_entry)))

# Создаем кнопку сохранения данных
save_button = tk.Button(window, text="Save", command=save_data)
save_button.grid(row=1, column=1)

def table_tooltip(widget, text, field):
    x, y, _, _ = widget.bbox("insert")
    x += widget.winfo_rootx() + 75
    y += widget.winfo_rooty() + 250
    # Creates a toplevel window
    tw = tk.Toplevel(widget)
    # Leaves only the label and removes the app window
    tw.wm_overrideredirect(True)
    tw.wm_geometry("+%d+%d" % (x, y))
    label = tk.Label(tw, text=text, justify='left', background='white',
                     relief='solid', borderwidth=1, font=("times", "8", "normal"))
    label.pack(ipadx=1)
    # Set the timer to close the tooltip after 3 seconds
    tw.after(3000, tw.destroy)

window.mainloop()
