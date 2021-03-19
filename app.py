from flask import Flask, make_response, request, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/rosebroccolo/Downloads/data.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)

class User(db.Model):
    query = None
    __tablename__ = 'user'
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

def __repr__(self):
    return '<User %r>' % self.name

class UserModel(Resource):
    def get(user_id):
        user = User.query.filter_by(userid=user_id).first()
        if user is None:
            return make_response("no user matching that id", 404)
        return {'user_id': user.userid, 'username': user.username, 'email': user.email, 'password': user.password}


"""def post(self, user_id):
    username_param = request.form['username']
    email_param = request.form['email']
    password_param = request.form['password']
    new_user = User(userid=user_id, username=username_param, email=email_param, password=password_param,
    db.session.add(new_user)
    db.session.commit()
    return make_response({'user_id': user_id, 'username': username_param, 'email': email_param, 'password': password_param}, 201)"""


def put(self, user_id):
    user = User.query.filter_by(userid=user_id).first()
    if user is not None:
        user.username = request.form['username']
        user.email = request.form['email']
        user.password = request.form['password']

        db.session.add(user)
        db.session.commit()
        return make_response({'user_id': user.userid, 'username': user.username, 'email': user.email,
                              'password': user.password}, 201)
    else:
        return make_response("no user matching that id", 404)


def delete(self, user_id):
        user = User.query.filter_by(userid=user_id).first()

        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return make_response({'user_id': user.userid, 'username':user.username, 'email':user.email, 'password':user.password}, 202)
            return make_response("deleted", 202)
        else:
            return make_response("no user matching that id", 404)


api.add_resource(UserModel, '/<string:user_id>')



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
