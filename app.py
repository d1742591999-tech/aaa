
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Placeholder prediction function
def predict_fracture(image_path):
    # In real version, load ML model here
    return {
        "fracture_type": "疑似桡骨骨折",
        "severity": "中度",
        "confidence": 0.78
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "no image uploaded"})

    img = request.files["image"]
    path = os.path.join("uploads", img.filename)
    os.makedirs("uploads", exist_ok=True)
    img.save(path)

    result = predict_fracture(path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
