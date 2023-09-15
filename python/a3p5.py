from flask import *

app = Flask(__name__)

@app.route('/')
def user():
    return render_template('a3p3home.html',name = "user")


@app.route('/<name>')
def home(name):
    if name == "Admin":
       return render_template('a3p3home.html',name = name)
    else:
        return "Please enter valid user!"
if __name__ == '__main__':
    app.run(debug=True)