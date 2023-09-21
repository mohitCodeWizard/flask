from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("a3p9registra.html")

@app.route("/addData", )
def addData():
    hobbie =""
    if request.method == "GET":
        nm = request.args['txtname']
        email = request.args['txtemail']
        pas = request.args['txtpass']
        phone = request.args['txtphone']
        gender = request.args['gender']
        if request.args.get('ch1'):
            hobbie += "read,"
        if request.args.get('ch2'):
            hobbie += "write,"
        if request.args.get('xh3'):
            hobbie += "paint"
        city = request.args['txtcity']
        addr = request.args['txtaddr']
        
        data =[{"name" : nm,"email": email, "pass": pas , "phone": phone , "gender": gender , "hobbie" : hobbie ,
                "city": city , "addr":addr}]
        return render_template("a3p9disp.html", data = data)
        

if __name__ == '__main__':
    app.run(debug=True)