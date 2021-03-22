from flask import Flask, request, render_template, redirect, url_for
from mail import send_mail
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        email = request.form['text']
        send_mail(email)
    return redirect(url_for("my_form"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3200, debug=True)
    