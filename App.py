from flask import Flask
from flask import request
from flask import render_template
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Chirag@29"
)

## Home Route
@app.route("/")
def helloWorld():
    return render_template("index.html")

@app.route("/store")
def storeInfo():
    if request.method=='POST':
        name = request.form('Name')
        email = request.form('Email')
        branch=request.form('Branch')
        collage=request.form('Collage')
        
    
    
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
