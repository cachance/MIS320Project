from flask import Flask, render_template, request

app = Flask(__name__)

WEB_APP_NAME = "BFC PORTAL"


@app.route('/')
@app.route('/home')
def home(name=WEB_APP_NAME):
    return render_template("home.html", content=name)


@app.route('/login', methods=['POST'])
def employeeLogin():
    user = request.form['user']
    password = request.form['password']

    if user == 'cody' and password == '12345':
        return render_template("login_good.html", user=user)
    return render_template("login_form.html")


@app.route('/login', methods=['GET'])
def employeeLogin_Page():
    return render_template("login_form.html")


@app.route('/membership/')
def membership(name=WEB_APP_NAME):
    return render_template("membership.html", content=name)


@app.route('/course/')
def course(name=WEB_APP_NAME):
    return render_template("course.html", content=name)


@app.route('/calendar/')
def calendar(name=WEB_APP_NAME):
    return render_template("calendar.html", content=name)


@app.route('/employee/')
def employee(name=WEB_APP_NAME):
    return render_template("employee.html", content=name)


@app.route('/product/')
def product(name=WEB_APP_NAME):
    return render_template("product.html", content=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
