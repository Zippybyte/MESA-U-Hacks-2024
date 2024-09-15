from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/homepage/<name>')
def homepage(name=None):
    return render_template('homepage.html', name=escape(name))

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)}\'s profile'



with app.test_request_context():
    print(url_for('homepage'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

    
if __name__ == '__main__':
    app.run()