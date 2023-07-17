from flask import Blueprint, render_template
# home.py is a Python Module because it has a .py extension & its belongs to the routes package
from app.models import Post
from app.db import get_db
# Blueprint() lets us consolidate routes into a single file
# This corresponds to using Router() in Express
bp = Blueprint('home', __name__, url_prefix='/')


# @bp is a decorator that tells Flask what URL to trigger the function
@bp.route('/')
# def index() is the function that will be triggered when the URL is visited
def index():
  # get all posts
  # get_db() resturns a session connection tied to routes context
  db = get_db()
  # Use query() method to query the Post model in descending order
  posts = db.query(Post).order_by(Post.created_at.desc()).all()

  return render_template(
    'homepage.html',
    posts=posts
  )

@bp.route('/login')
def login():
  return render_template('login.html')

# <id> is a dynamic parameter that will be passed into the function 
@bp.route('/post/<id>')
# single(id) is the function parameter that will be passed into the function
def single(id):
#   whatever is returned from the function will be rendered in the browser
#   in this case, the single-post.html template
  return render_template('single-post.html')

# You can import any variables or functions defined in Python Modules into other modules or files
# We only care about the bp variable thanks to the @bp.route() decorator, so we import it like this:
# from app.routes.home import bp