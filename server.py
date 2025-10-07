from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/order', methods='POST')
def save_order():
    pizza = request.json.get('pizza')
    orders.append(pizza)
    return jsonify({'message': f'новый заказ {pizza} сохранен'})

if __name__ == "__main__"
    app.run(debug=True)