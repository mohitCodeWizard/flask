from flask import *

app = Flask(__name__)

@app.route('/add')
def add():
    num1 = request.args.get('n1')
    num2 = request.args.get('n2')

    try:
        result = int(num1) + int(num2)
        return f'The additon of {num1} and {num2} is {result}'
        
    except ValueError:
        return 'Please enter valid argument'
    
if __name__ == '__main__':
    app.run(debug=True)