import psycopg2
import os.path
from flask import *
app = Flask(__name__)

app.config.from_object('config-test')

try:
    app.config.from_envvar('PYTHON_DEV_CONFIG')
except:
    print("weoweo error I dont care")

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

@app.route('/test')
def hello_world():
    try:
        conn = psycopg2.connect(app.config['DBCONN'])
        print ("Connected much very good")
    except:
        print ("I am unable to connect to the database")

    print ("More most good question: Can I haz conn here?")
    print(conn)
    cur = conn.cursor()
    cur.execute("""SELECT * from skill""")
    rows = cur.fetchall()

    print ("\nShow me the databases:\n")
    for row in rows:
        print ("   ", row[0])
        print ("   ", row[1])
    return row[1]

@app.route('/app')
def send_app():
    try:
        print(app.config['TESTVAR'])
        print(app.config['TESTVAR2'])
        return send_from_directory(root_dir(),"page.html", as_attachment=False)
    except Exception as e:
        print("many error")
        print(root_dir())
        print("errore:" + str(e))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
