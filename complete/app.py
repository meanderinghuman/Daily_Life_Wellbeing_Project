from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoders
model = pickle.load(open("model.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))
encoder = pickle.load(open("onehot_encoder.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Get form data
        input_data = [request.form.get(field) for field in [
            'age', 'gender', 'routine', 'stress', 'life', 'work',
            'study', 'social', 'media', 'support', 'change'
        ]]

        # One-hot encode input
        input_encoded = encoder.transform([input_data])

        # Predict
        pred = model.predict(input_encoded)
        mood = label_encoder.inverse_transform(pred)[0]

        return jsonify({"prediction": mood})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
