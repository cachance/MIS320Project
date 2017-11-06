from flask import Flask, render_template, request
import markdown as md
import csv

app = Flask(__name__)

WEB_APP_NAME = "BFC PORTAL"


@app.route('/')
@app.route('/home')
@app.route('home/<name>')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)


@app.route('/employeePortal/')
@app.route('/employeePortal/<name>')
def EmployeePortal(name=WEB_APP_NAME):
    return render_template("employeePortal.html", content=name)


@app.route('/membership/')
@app.route('/membership/<name>')
def membership(name=WEB_APP_NAME):
    return render_template("membership.html", content=name)


@app.route('/courses/')
@app.route('/courses/<name>')
def courses(name=WEB_APP_NAME):
    return render_template("courses.html", content=name)


@app.route('/calendar/')
@app.route('/calendar/<name>')
def calendar(name=WEB_APP_NAME):
    return render_template("calendar.html", content=name)


@app.route('/employee/')
@app.route('/employee/<name>')
def employee(name=WEB_APP_NAME):
    return render_template("employee.html", content=name)


@app.route('/products/')
@app.route('/products/<name>')
def products(name=WEB_APP_NAME):
    return render_template("products.html", content=name)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
