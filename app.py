from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import util
import os  # ✅ Import os for environment variables

app = Flask(__name__, static_folder='../client/static', template_folder='../client/templates')
CORS(app)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    return jsonify({'locations': locations})

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    total_sqft = float(data['total_sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])
    location = data['location']

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    return jsonify({'estimated_price': estimated_price})

if __name__ == '__main__':
    print("Starting Flask server...")

    # ✅ Use the assigned Render PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
