#This file contains the script to run our website
#make sure you have Flask installed, use pip install flask

from flask import Flask, render_template    #imports

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')   #for home page

@app.route('/about/')
def about():
    return render_template('about.html') #for about page

if __name__ == "__main__":
    app.run(host="0.0.0.0")  #open your local host e.g. http://localhost:5000/
