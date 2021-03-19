from flask import Flask, request, render_template
from datetime import date, time, datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Vitaly')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/test/info/<id>')
def info(id):
    # id, time = id, datetime.now().strftime("%H:%M:%S")
    user_dict = dict(id=id, time=datetime.now().strftime("%H:%M:%S"), morning=datetime.time('6', '0'),
                     day=datetime.time('12', '0'), evening=datetime.time('16', '0'))
    return render_template('info.html', **user_dict)


# @app.route('/users/<id>/')
# def user_profile(id):
#     id, time = id, datetime.now().strftime("%H:%M:%S")
#     user_dict = dict(id=id, time=time )
#     return render_template('users.html', **user_dict)


# @app.route('/user/')
# def user_info():
#     return render_template('user.html')


if __name__ == '__main__':
    app.run(debug=True)
