import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://cstillma:wO7zKANdKLIl32xMMogTGB3yUiTqTNE7@dpg-cj218ri7l0fj36ub0f40-a/flaskappdb")
    conn.close()
    return "Database Connection Successful"
