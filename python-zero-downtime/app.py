import time,os
from flask import Flask
app = Flask(__name__)

hostname = os.environ.get('HOSTNAME','localhost')

@app.route('/')
def hello_world():
    return hostname+'v4 - 25sn gecikmeli kalkis - Hey gidi koca dunya \n'

if __name__ == '__main__':
    time.sleep(25) # baslarken 25 saniye gecik, sonradan ayaga kalk
    app.run(host='0.0.0.0',port=8080)
