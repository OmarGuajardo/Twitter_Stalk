
from flask import Flask,render_template,url_for,request
app = Flask(__name__)
from backend.admin import *
from backend.keys import *

user_object = Admin(consumer_key,consumer_secret,access_token,access_token_secret)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods = ["POST"])
def search():
    variables = {}
    
    name = request.form["name"]
    url = user_object.get_profile_pic(name)

    variables["url"] = url
    return render_template('user.html',variables=variables)


if __name__ == '__main__':
    app.run(debug=True)
    