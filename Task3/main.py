from flask import Flask, request

app = Flask(__name__)

def inverseDec(func):

    def wrapper(*args, **kwargs):
        options = request.get_json()
        op1 = options['op1']
        op2 = options['op2']
        op = options['op']
        if op == '+':
            op = '-'
        elif op == '-':
            op = '+'
        return func(op1, op2, op)
    return wrapper




@app.route('/calc', methods=['POST'])
@inverseDec
def calc(op1, op2, op):
    if op == '+':
        return "Response: {}".format(op1+op2)
    elif op == '-':
        return "Response: {}".format(op1-op2)
    else:
        return "Invalid operator"




if __name__ == '__main__':
    app.run(debug=True)


