from flask import Flask, render_template
from flask_wtf import FlaskForm
from formmodels import RegistrationForm, LoginForm

app = Flask(__name__)

SECRETS_URI = '3b301329dd4aec7ff92ca50e8e328f52'

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)