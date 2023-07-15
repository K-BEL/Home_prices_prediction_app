from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_State_names', methods=['GET'])
def get_State_names():
    response = jsonify({
        'state': util.get_State_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_Type_names', methods=['GET'])
def get_Type_names():
    response = jsonify({
        'type': util.get_Type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    Lot = float(request.form['Lot'])
    State = request.form['State']
    Type = request.form['Type']
    Bathrooms = int(request.form['Bathrooms'])
    Floors = int(request.form['Floors'])
    Garages = int(request.form['Garages'])
    rooms = int(request.form['rooms'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(State,Type, Lot, Bathrooms, Floors, Garages, rooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()