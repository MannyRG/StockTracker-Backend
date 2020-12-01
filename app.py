
from flask import Flask, g
from flask_cors import CORS
# import requests
import models
from resources.stocks import stock
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

@app.route('/')
def index():
    return 'Route works'

CORS(stock, origins=['http://localhost:3000', 'http://localhost:3000/'], supports_credentials=True)
app.register_blueprint(stock, url_prefix='/stock_tracker/v1')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)





