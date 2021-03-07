from flask import Flask, request, render_template
from datetime import date, time, datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Vitaly')


@app.route('/users/<id>/')
def user_profile(id):
    id, time = id, datetime.now().strftime("%H:%M:%S")
    user_dict = dict(id=id, time=time )
    return render_template('users.html', **user_dict)


@app.route('/user/')
def user_info():
    return render_template('user.html')


if __name__ == '__main__':
    app.run(debug=True)
