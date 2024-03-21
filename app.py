import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    conn = psycopg2.connect(
        dbname="sampledb",
        user="sampleuser",
        password="samplepassword",
        host="db",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT version()")
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Hello, World! Database version: {db_version[0]}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')