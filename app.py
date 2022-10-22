import email
from flask import Flask, render_template, request, jsonify, redirect, url_for
from firestoreDB import *
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
    return render_template('launch.html')

@app.route("/about")
def about():
    return render_template('aboutUs.html')

@app.route("/programs")
def program():
    return render_template('programs.html')

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('launch.html')

@app.route("/dory")
def tester():
    return 'Hello Foo!'

@app.route("/setup/<email>",methods=['GET','POST'])
def setUp(email):
    return render_template('profile_form.html',  email=email)

@app.route("/setupForm",methods=['GET','POST'])
def setForm():
    if request.method == 'POST': 
        received_details= request.form

        id = received_details['email']
        address = received_details['address']
        github_link = received_details['github']
        city = received_details['city']
        level = received_details['level']
        interest1 = received_details['interest1']
        interest2 = received_details['interest2']

        data = {
            'email': id,
            'address': address,
            'github' : github_link,
            'city' : city,
            'level' : level,
            'interest1' : interest1,
            'interest2' : interest2
        }

        userProfileData(data)
    return redirect(url_for('profile', id=id, isAuth=True))


@app.route('/profile', methods=['GET', 'POST'])
@app.route('/profile/<id>/<isAuth>', methods=['GET', 'POST'])
def profile(id, isAuth):
    if str2bool(isAuth) == True:
        userData = getUserData(id)
        return render_template('profilepage.html', userData=userData)
    return redirect(url_for('login'))

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

@app.route("/authCheck", methods=['GET','POST'])
def authCheck():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        authData =  authenticateLogin(email, password)
        if type(authData) == dict:
            return redirect(url_for('profile', id=authData['id'], isAuth=True))
    return redirect(url_for('login'))


@app.route("/signUp", methods=['GET','POST'])
def signUp():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['number']
        
        obfusEmail = obfusMail(email)
        # check if email exists
        emailExists = checkEmail(obfusEmail)
        print(emailExists)
        if emailExists == True:
            # email already exists, return to login
            return redirect(url_for('login'))
        
        # put new info into the database
        data  =  {'id':obfusMail(email), 'email':email, 'password':password, 'name':name, 'phone': phone} 
        signUpUser(data)
        #authData =  authenticateLogin(email, password)
        #if type(authData) == dict:
        #    return redirect(url_for('profile', id=authData['id'], isAuth=True))
    return redirect(url_for('setUp', email=obfusEmail))
       
# TO DO 
 # Pass sign in error message to login


@app.route('/test')
def test():
    return render_template('test.html')

#if __name__ == '__main__':
 #   app.run(host='0.0.0.0', port='8000', debug=True)