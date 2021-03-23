import logging
from logging import FileHandler
from flask import Flask, request, render_template, redirect, url_for
from mail import send_mail
app = Flask(__name__)

logging.basicConfig(filename = "web_scrapping.log", level= logging.DEBUG, 
                    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    try:
        if request.method == 'POST':
            email = request.form['text']
            send_mail(email)
        return redirect(url_for("my_form"))
    except Exception as e:
        logging.error("split method in carpet descripsion is expecting a bytes-like object" +str(e))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3200, debug=True)
    