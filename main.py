import sqlite3
from flask import Flask, make_response, request, render_template, send_from_directory
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static/style.css')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/rosebroccolo/Downloads/data.db'
db = SQLAlchemy(app)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


class OrderItem(db.Model):
    __tablename__ = 'OrderItem'
    OrderItemId = db.Column(db.Integer, primary_key=True)
    OrderId = db.Column(db.Integer)
    MenuItemId = db.Column(db.Integer)
    ExtraId = db.Column(db.Integer)


class Order(db.Model):
    __tablename__ = 'Order'
    OrderId = db.Column(db.Integer, primary_key= True)
    Date = db.Column(db.TEXT)
    Time = db.Column(db.TEXT)
    CustomerId = db.Column(db.Integer)
    CustomerName = db.Column(db.TEXT)
    CustomerPhone = db.Column(db.TEXT)



@app.route('/order', methods=['POST'])
def medium(menu_item):
    item = Item.query.filter(Item.id == item_id)
    cart_item = CartItem(product=product)
    db.session.add(cart_item)
    db.session.commit()

    return render_tempate('home.html', product=products)


"""def get_item(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
         = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))"""
