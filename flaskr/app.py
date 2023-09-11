from flask import Flask, render_template, flash, redirect, url_for, request
from formmodels import RegistrationForm, LoginForm, SearchPage
from connector import pipeline,connection
import pprint as pp

app = Flask(__name__, static_folder='C:\\Users\SaptarshiMohanty\webapp\src')

app.config['SECRET_KEY'] = '3b301329dd4aec7ff92ca50e8e328f52'

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('search'))
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.empid.data}')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchPage()
    name = form.first_name.data
    if request.method == 'POST':
        return redirect(url_for("result", name=name))
    else:
        pp.pprint(result)
        return render_template('search.html', form = form)

@app.route("/result/<name>", methods = ['POST', 'GET'])
def result(name):
    r = pipeline.get_value(name=name)
    return render_template('result.html', r = r)

if __name__ == '__main__':
    app.run(debug=True)