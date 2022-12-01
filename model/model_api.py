import joblib
from flask import Flask, request
import json

app = Flask(__name__)

loaded_model = joblib.load("random_forest.joblib")

@app.route("/predict", methods=['POST']) # permet de spécifier quand la fonction juste en dessous doit être appelée
def predict():

    X = json.loads(request.get_json())["X"]
    print("X:", X)
    return json.dumps({"prediction": [round(pred) for pred in loaded_model.predict(X)]})

if __name__ == "__main__":
    app.run("0.0.0.0")
