import time,os,psycopg2
from flask import Flask
app = Flask(__name__)

# KUBERNETES otomatik olarak HOSTNAME'i container'ın environment'ına enjekte eder
hostname = os.environ['HOSTNAME']

# Postgresql bağlantı bilgilerini env'den alalım
postgre_hostname=os.environ['POSTGRE_HOSTNAME']
postgre_port=os.environ['POSTGRE_PORT']
postgre_username=os.environ['POSTGRE_USERNAME']
postgre_password=os.environ['POSTGRE_PASSWORD']
postgre_dbname=os.environ['POSTGRE_DBNAME']

DB_VERSION = None

@app.route('/')
def hello_world():
    connect()
    return hostname+'- PostgreSQL DB Version is:' + DB_VERSION + '\n'

def connect():
    
    conn = None

    try:
        print('Connecting PostgreSQL db..')
        conn = psycopg2.connect(
            host=postgre_hostname,
            port=postgre_port,
            database=postgre_dbname,
            user=postgre_username,
            password=postgre_password)
        
        cur = conn.cursor()
        cur.execute('SELECT version()')
        DB_VERSION = str(cur.fetchone())

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    time.sleep(15) # baslarken 15 saniye gecik, sonradan ayaga kalk
    app.run(host='0.0.0.0',port=8080)
