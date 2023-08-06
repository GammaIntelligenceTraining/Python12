from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(seconds=5)


@app.route('/')
def home():
    return render_template('home.html', user_name='Roman', numbers=[1, 2, 3, 4, 5, 6, 7],
                           person={'name': 'Jack', 'age': 20})


# @app.route('/<name>')
# def user(name):
#     return f'Hello {name}'

@app.route('/user')
def user():
    if 'user_name' in session:
        user = session['user_name']
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['user-name']
        session['user_name'] = user
        return redirect(url_for('user', name=user))
    else:
        if 'user_name' in session:
            return redirect(url_for('user'))
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))


@app.route('/admin')
def admin():
    return redirect(url_for('home'))


@app.route('/api')
def api():
    return {'name': 'Jack', 'popular': True}



if __name__ == '__main__':
    app.run(debug=True)