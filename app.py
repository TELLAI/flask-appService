import logging
from logging import FileHandler
from flask import Flask, request, render_template, redirect, url_for, jsonify
from mail import send_mail
import psycopg2

app = Flask(__name__)

logging.basicConfig(filename = "journal.log", level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

host = '52.158.246.63'
dbname = 'test_ansible'
user = 'postgres'
password = 'pw'
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def sendMail():
    if request.method == 'POST':
        email = request.form['text']
        cur = conn.cursor()
        cur.execute("select * from test;")
        result = cur.fetchall()
        cur.close()
        send_mail(result[0][0], email)
    return redirect(url_for("my_form"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3200, debug=True)
