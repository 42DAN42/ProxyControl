import pickle
import json
import sys
import os

# Открыть файл .pkl
with open(sys.argv[1], 'rb') as f:
    obj = pickle.load(f)

# Преобразовать объект .pkl в объект json
json_obj = json.loads(json.dumps(obj, default=str))

# Записать json-файл
with open(os.path.splitext(sys.argv[1])[0] + '.json', 'w', encoding='utf-8') as f:
    json.dump(json_obj, f, ensure_ascii=False, indent=4)
