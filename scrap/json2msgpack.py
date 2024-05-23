import json
import msgpack

# Загрузка данных из файла JSON
with open('internal_ips.json', 'r') as f:
    data = json.load(f)

# Сохранение данных в файл msgpack
with open('internal_ips.msgpack', 'wb') as f:
    packed = msgpack.packb(data)
    f.write(packed)
