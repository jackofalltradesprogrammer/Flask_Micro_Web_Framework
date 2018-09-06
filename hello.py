from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello, World!'

@app.route('/login')
def login():
	return 'login'

@app.route('/user/<username>')
def profile(username):
	#show the user profile for that user
	return '{}\'s profile'.format(username)

with app.test_request_context():
	print(url_for('index'))
	print(url_for('login'))
	print(url_for('login', next='/'))
	print(url_for('profile', username='John Doe'))

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	#show the subpath after /path/
	return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
	# Url for "/projects/" is like a directory 
	return 'The project page'

@app.route('/about')
def about():
	# Url for "about" without slash is similar to a filename
	return 'The about page'
