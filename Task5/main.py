from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["calculator"]

mycol = mydb["calculations"]
lastop = mydb["last_operation"]

@app.route('/calc', methods=['POST'])
def _calc():
    opt = request.get_json()

    op1 = opt["op1"]
    op2 = opt["op2"]
    op = opt["op"]

    if op == '+':
        additem1 = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1+op2}
        mycol.insert_one(additem1)
        if lastop.find_one({"op": "+"}) is None:
            additem = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1 + op2}
            lastop.insert_one(additem)
        else:
            lastop.update_one({"op": "+"}, {"$set": {"op1": str(op1)}})
            lastop.update_one({"op": "+"}, {"$set": {"op2": str(op2)}})
            lastop.update_one({"op": "+"}, {"$set": {"op": str(op)}})
            lastop.update_one({"op": "+"}, {"$set": {"Response": op1 + op2}})


    elif op == '-':
        additem1 = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1 - op2}
        mycol.insert_one(additem1)
        if lastop.find_one({"op": "-"}) is None:
            additem = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1 - op2}
            lastop.insert_one(additem)
        else:
            lastop.update_one({"op": "-"}, {"$set": {"op1": str(op1)}})
            lastop.update_one({"op": "-"}, {"$set": {"op2": str(op2)}})
            lastop.update_one({"op": "-"}, {"$set": {"op": str(op)}})
            lastop.update_one({"op": "-"}, {"$set": {"Response": op1 - op2}})
    elif op == '*':
        additem1 = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1 * op2}
        mycol.insert_one(additem1)
        if lastop.find_one({"op": "*"}) is None:
            additem = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1 * op2}
            lastop.insert_one(additem)
        else:
            lastop.update_one({"op": "*"}, {"$set": {"op1": str(op1)}})
            lastop.update_one({"op": "*"}, {"$set": {"op2": str(op2)}})
            lastop.update_one({"op": "*"}, {"$set": {"op": str(op)}})
            lastop.update_one({"op": "*"}, {"$set": {"Response": op1 * op2}})
    elif op == '/' and op2 != 0:
        additem1 = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1 / op2}
        mycol.insert_one(additem1)
        if lastop.find_one({"op" : "/"}) is None:
            additem = {"op1": str(op1), "op2": str(op2), "op": str(op), "Response": op1 / op2}
            lastop.insert_one(additem)
        else:
            lastop.update_one({"op": "/"}, {"$set": {"op1": str(op1)}})
            lastop.update_one({"op": "/"}, {"$set": {"op2": str(op2)}})
            lastop.update_one({"op": "/"}, {"$set": {"op": str(op)}})
            lastop.update_one({"op": "/"}, {"$set": {"Response": op1 / op2}})
    else:
        return "Invalid Operation!"

    return "Operation Successful!!"




if __name__ == '__main__':
    app.run(debug=True)