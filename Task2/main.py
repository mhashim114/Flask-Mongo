from flask import Flask, request

app = Flask(__name__)


@app.route('/calc', methods=['POST'])
def calc():
    options = request.get_json()

    op1 = options['op1']
    op2 = options['op2']
    op = options['op']

    if op == '+':
        return '''Response = {}'''.format(op1+op2)
    else:
        return '''Invalid Operator'''


if __name__ == '__main__':
    app.run(debug=True)