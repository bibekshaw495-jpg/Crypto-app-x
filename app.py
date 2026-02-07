from flask import Flask, request, jsonify
from binance.client import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "4JrmxODuKzvm0Jq737k6t57ZOk4M6thWNzrqNEid3vuuHX5pVsocIHheMEsHPzf9"
API_SECRET = "xEJEqowTLAlJxEkvTZPRz4r6dzlIr9RpTIf4oemu1VrzJn5cgZ2cHK6fPZ8vxw0N"

client = Client(API_KEY, API_SECRET)

@app.route('/buy', methods=['POST'])
def buy():
    symbol = request.json['symbol']
    quantity = request.json['quantity']
    order = client.order_market_buy(symbol=symbol, quantity=quantity)
    return jsonify(order)

@app.route('/sell', methods=['POST'])
def sell():
    symbol = request.json['symbol']
    quantity = request.json['quantity']
    order = client.order_market_sell(symbol=symbol, quantity=quantity)
    return jsonify(order)

@app.route('/price/<symbol>', methods=['GET'])
def price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return jsonify(ticker)

if __name__ == '__main__':
    app.run()
