from flask import Flask, render_template, flash, redirect, url_for
from formmodels import RegistrationForm, LoginForm

app = Flask(__name__, static_folder='C:\\Users\SaptarshiMohanty\webapp\src')

app.config['SECRET_KEY'] = '3b301329dd4aec7ff92ca50e8e328f52'

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.empid.data}')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)