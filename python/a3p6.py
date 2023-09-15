from flask import *

app = Flask(__name__)

list_subject =['PHP','JAVA','PYTHON']
@app.route('/')

def display_subject():
    return render_template('a3p6list_subject.html',subjects = list_subject)


if __name__ == "__main__":
    app.run(debug=True)