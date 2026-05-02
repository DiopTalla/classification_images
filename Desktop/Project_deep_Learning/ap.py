from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path

app = Flask(__name__)

# Charger modèle
model_path = Path("C:/Users/HP/Desktop/Project_deep_Learning/model_chien_chat.keras")
model = tf.keras.models.load_model(model_path)

# Prétraitement
def preprocess(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Route test
@app.route("/")
def home():
    return "API OK 🚀"

# Route prédiction
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier envoyé"}), 400

    file = request.files["file"]

    try:
        image = Image.open(file).convert("RGB")
        img = preprocess(image)

        pred = model.predict(img)[0][0]

        if pred > 0.5:
            label = "chien"
            confidence = float(pred)
        else:
            label = "chat"
            confidence = float(1 - pred)

        return jsonify({
            "classe": label,
            "confiance": round(confidence, 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Lancer serveur
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)