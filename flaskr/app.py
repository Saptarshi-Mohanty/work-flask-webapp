from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bcrypt import Bcrypt
from formmodels import RegistrationForm, LoginForm, SearchPage
from connector import pipeline
import pprint as pp

app = Flask(__name__, static_folder='C:\\Users\SaptarshiMohanty\webapp\source')

app.config['SECRET_KEY'] = '3b301329dd4aec7ff92ca50e8e328f52'

def password_hashing(password):
    bcrypt = Bcrypt(app)
    pas = bcrypt.generate_password_hash(password).decode('UTF-8')
    return pas

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
        hashed_password = password_hashing(form.password.data)
        pipeline.insert_user(fname=form.first_name.data, lname=form.last_name.data, email=form.email.data, empid=form.empid.data, title=form.title.data, password=hashed_password)
        flash(f'Account created for {form.empid.data}')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchPage()
    name = form.first_name.data
    value = None
    if form.dropdown.data:
        value = form.dropdown.data
    if request.method == 'POST' and value :
        return redirect(url_for("result", name=name, value=value))
    elif request.method == 'POST':
        return redirect(url_for("result", name=name))
    else:
        return render_template('search.html', form = form)

@app.route("/result/<name>/<value>", methods = ['POST', 'GET'])
def result(name, value):
    if name != "all" and value == 'sbn':
        r = pipeline.sort_name(name=name)
        return render_template('result.html', r = r)
    elif name != "all" and value == 'sbr':
        r = pipeline.sort_rating(name=name)
        return render_template('result.html', r = r)
    elif name != "all" and value == 'None':
        r = pipeline.get_first_name(name=name)
        return render_template('result.html', r = r)
    elif name == "all" and value =="sbn":
        r = pipeline.sort_name_all()
        return render_template('result.html', r = r)
    elif name == "all" and value =="sbr":
        r = pipeline.sort_rating_all()
        return render_template('result.html', r = r)
    elif name == 'all' and value == 'None':
        r = pipeline.get_all()
        return render_template('result.html', r = r)
    
if __name__ == '__main__':
    app.run(debug=True)