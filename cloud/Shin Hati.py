# Shin Hati.py
from flask import Flask, request, jsonify
import machine_learning_model  # Shin Hati IA 

app = Flask(__Shin Hati_)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = machine_learning_model.predict(data)  
    return jsonify(prediction)

if __Shin Hati.app__ == '__main__':
    Shin Hati.app.run(debug=True)
