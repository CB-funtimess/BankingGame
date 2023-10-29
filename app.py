from functools import wraps
from flask import Flask, Response, redirect, render_template, request, session, url_for
import requests
import a

app = Flask(__name__)
app.config['SECRET_KEY'] = "iuyofhowburkjlseirufyUJ98IUAHG3F83LAYUGAIELKRV.JAIUO"

def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
    # Check to see if it's in their session
        if 'api_session_token' not in session:
            # If it isn't return our access denied message (you can also return a redirect or render_template)
            return Response("Access denied")

        # Otherwise just send them where they wanted to go
        return func(*args, **kwargs)

    return check_token

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login/", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        id = request.form.get('accountID')
        firstname = request.form.get('fname')
        login_credentials(id)
        return redirect('/main')
    return render_template('login.html')

def login_credentials(id):
    response = a.getSpecificAccount(id)
    if response != None:
        #token = response["user"]["authentication-token"]
        token = "jlhdfalskfdasikjdhbalijrgnaeilkhaj;ougilkjhaoghag"
        
        session['api_session_token'] = token
        session['user_id'] = id
        
@app.route("/main")
@require_api_token
def main():
    return render_template('main.html')


@app.route("/main/atm/")
@require_api_token
def atm():
    return render_template('atm.html')


@app.route("/main/help")
@require_api_token
def enquiries():
    return render_template('hc.html')

def render_enquiry_form():
    return render_template('enquiry.html')
    