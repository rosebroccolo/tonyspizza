from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/rosebroccolo/Downloads/data.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "user info"
    else:
        return render_template('register.html')


"""@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]"""

""""login = User.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("index.html"))
        return redirect(url_for("register.html"))
return render_template("login.html")"""

"""@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']"""

"""register = user(username=uname, email=mail, password=passw)
    db.session.add(register)
    db.session.commit()"""

"""return redirect(url_for("login"))


return render_template("register.html")"""

"""if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)"""


