from flask import Flask, render_template, request, redirect, jsonify 

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
        received_details= request.get_json()
        user_details = received_details['user_details']
        print(received_details)
        if received_details['status'] == 'login':
            email = user_details['email']
            password = user_details['password']
            #database validation function
        elif received_details['status']=='sign_up':
            first_name = user_details['first_name']
            last_name = user_details['last_name']
            mobile_number = user_details['mobile_number']
            email = user_details['email']
            password = user_details['password']
            #database validation to prevent duplicates mail
            #database save function

            

    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/setup",methods=['GET','POST'])
def setUp():
    if request.method == 'POST': 
        received_details= request.get_json()
        profile_photo=received_details['profile_photo']
        address = received_details['address']
        country = received_details['country']
        github_link = received_details['github_link']
        city = received_details['city']
        interests =received_details['interests']

    return render_template('profile_form.html')

@app.route("/profile")
def profile():
    #get data as dict from database
    profile_data = {'full_name': 'dan', 'city':'Ibadan'}
    #jsonify_data = jsonify(profile_data)

    # city =profile_data['city']
    # email = profile_data['email']
    # github_link = profile_data['github_link']
    # name = f"{profile_data['full_name']} {profile_data['full_name']}"
    # years_with_factory = profile_data['years_with_factory']

    



    return render_template('profilepage.html', profile_data = profile_data)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)