from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def launch():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('aboutUs.html')

@app.route("/programs")
def program():
    return render_template('programs.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method =='POST':
        login_details= request.get_json()
        print(login_details)


    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/setup")
def setUp():
    return render_template('profile_form.html')

@app.route("/profile")
def profile():
    return render_template('profilepage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)