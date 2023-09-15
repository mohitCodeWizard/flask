from flask import *

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("a3p2login.html")

@app.route('/home', methods = ["POST"])
def home():
    upass = request.form['txtpassword']
    if upass == "123" :
        return render_template("a3p2home.html")
    else:
        return render_template("a3p2login.html")

if __name__ == "__main__":
    app.run(debug=True)