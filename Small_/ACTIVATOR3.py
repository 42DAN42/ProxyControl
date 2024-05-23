from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/activate_script')
def activate_script():
    subprocess.call(['python', 'C:\Python27\proxy\Small\CHANGER3.py'])
    #subprocess.call(['python', 'C:\Python27\proxy\++ULTIMATE_switcher_UPD.py'])
    return 'Скрипт успешно запущен!'

if __name__ == '__main__':
    app.run(host='192.168.0.102', port=8042)
