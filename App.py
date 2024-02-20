from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

## Home Route
@app.route("/")
def helloWorld():
    return render_template("index.html")
    
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
