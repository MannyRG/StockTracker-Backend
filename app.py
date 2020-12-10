
from flask import Flask, g
from flask_cors import CORS
# import requests
import models
from resources.stocks import stock
from resources.tracker import track

DEBUG = True
PORT = 8000


app = Flask(__name__)



# r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol=AAPL&token=bv2ks9v48v6ubfulf760')
# print(r.json())
# import requests
# r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=bv2ks9v48v6ubfulf760')
# print(r.json())



@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response



@app.route('/', methods=["GET"])
def get_public_post():
    # find the dogs and change each one to a dictionary into a new array
    try:
        # posts = [model_to_dict(post) for post in posts]
        print("Hello")
        return jsonify(data={}, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})



CORS(stock, origins=['http://localhost:3000', 'http://localhost:3000/'], supports_credentials=True)
app.register_blueprint(stock, url_prefix='/Vanta')

CORS(track, origins=['http://localhost:3000', 'http://localhost:3000/'], supports_credentials=True)
app.register_blueprint(track, url_prefix='/Vanta')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)





