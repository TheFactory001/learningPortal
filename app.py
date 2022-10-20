from flask import Flask, render_template, request, jsonify, redirect, url_for
#from firestoreDB import *
import os
from flask_cors import CORS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static')
app.config['SECRET_KEY'] = '#2703ARAD'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

#print(type(authenticateLogin("johnDoe@doe.com", "123JohnDoe")))


@app.route("/")
def launch():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('aboutUs.html')


@app.route("/programs")
def program():
    return render_template('programs.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/dory")
def tester():
    return 'Hello Foo!'


@app.route("/setup", methods=['GET', 'POST'])
def setUp():
    if request.method == 'POST':
        received_details = request.get_json()
        profile_photo = received_details['profile_photo']
        address = received_details['address']
        country = received_details['country']
        github_link = received_details['github_link']
        city = received_details['city']
        interests = received_details['interests']

    return render_template('profile_form.html')

<<<<<<< HEAD

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    return render_template('profilepage.html')
=======
@app.route('/profile/<id>/<isAuth>', methods=['GET', 'POST'])
def profile(id, isAuth):
    if str2bool(isAuth) == True:
        userData = getUserData(id)
        return render_template('profilepage.html', userData=userData)
    return redirect(url_for('login'))

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")
>>>>>>> db8401780323f16e4b19087acff61f8b0c495882


@app.route("/authCheck", methods=['GET', 'POST'])
def authCheck():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        authData = authenticateLogin(email, password)
        if type(authData) == dict:
            return redirect(url_for('profile', id=authData['id'], isAuth=True))
    return redirect(url_for('login'))

# TO DO
    # Sign up support from DB
    # Pass sign in error message to login
    # Pass info to profile page


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
