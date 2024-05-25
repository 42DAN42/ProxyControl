# Мониторинг и управление IP-адресами модемов

Этот скрипт позволяет мониторить и управлять IP-адресами модемов через интерфейс tkinter.

## Установка зависимостей

Для работы скрипта требуется установить библиотеку `tkinter`:

```sh
pip install tk
```

## Использование

1. Запустите скрипт `main.py`.
2. В окне программы вы увидите список модемов с возможностью включения и выключения каждого.
3. Введите IP-адрес каждого модема в соответствующее поле.
4. Нажмите кнопку "Save" для сохранения изменений.


## Работа программы:

1. Создание процессов для каждого модема:
   - Для каждого модема запускается отдельный процесс.
   - Процесс запускается с помощью `subprocess.Popen` и запускает скрипт для соответствующего модема.

2. Отслеживание состояния каждого процесса:
   - Используется список `processes` для хранения процессов.
   - Используется список `flags` для отслеживания состояния каждого процесса (включен или выключен).

3. Включение и выключение модемов:
   - Для каждого модема есть кнопка, которая меняет состояние модема (включен или выключен).
   - При нажатии кнопки:
     - Если модем выключен, запускается соответствующий процесс и кнопка меняет цвет на зеленый.
     - Если модем включен, процесс останавливается и кнопка меняет цвет на красный.

4. Загрузка и сохранение данных об IP-адресах:
   - Данные об IP-адресах загружаются из файла `internal_ips.json` и отображаются в таблице.
   - При сохранении данных из таблицы они записываются обратно в файл `internal_ips.json`.

5. Отображение интерфейса с помощью библиотеки `tkinter`:
   - Создается главное окно с названием "Modem IP Addresses".
   - Создается таблица с модемами и их IP-адресами.
   - Создаются кнопки для включения и выключения модемов.
   - Создается поле для ввода пути к файлу лога и кнопка для сохранения изменений.

## Связь с автором

- Email: 42dannymarshall@gmail.com
- GitHub: https://github.com/42DAN42
- Telegram: @I_DAN_I

---
