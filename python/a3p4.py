from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("a3p2login.html")

@app.route('/home', methods = ["POST"])
def home():
    upass = request.form['txtpassword']
    if upass == "123" :
        uname = request.form['txtuname']
        return render_template("a3p3home.html",name = uname)
    else:
        return render_template("a3p2login.html")


if __name__ == "__main__":
    app.run(debug=True)