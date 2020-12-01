import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

# We can use this as a Python decorator for routing purposes
# first argument is blueprints name
# second argument is it's import_name
stock = Blueprint('stocks', 'stock')



@stock.route('/', methods=["GET"])
def get_all_stocks():
    ## find the dogs and change each one to a dictionary into a new array
    try:
        stock = [model_to_dict(stock) for stock in models.Stock.select()]
        print(stock)
        return jsonify(data=stock, status={"code": 200, "message": "Success All Stocks"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})



@stock.route('/', methods=["POST"])
def create_stock():
    payload = request.get_json()
    print(type(payload), 'payload')
    stock = models.Stock.create(**payload)
    print(stock.__dict__)
    print(dir(stock))
    print(model_to_dict(stock), 'model to dict')
    stock_dict = model_to_dict(stock)
    return jsonify(data=stock_dict, status={"code": 201, "message": "Success New Ticker"})

