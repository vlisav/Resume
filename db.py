import psycopg2
from flask import *
app = Flask(__name__)

@app.route('/test')
def hello_world():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='Highter95'")
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
    return row[0]

@app.route('/app')
def send_app():
    try:
        return send_from_directory("C:/Project\Resume","page.html", as_attachment=False)
    except Exception as e:
        print("many error")
        print("errore:" + str(e))

if __name__ == '__main__':
    app.debug = True
    app.run()
