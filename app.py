import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if prediction>-50:
        return render_template("index.html", prediction_text = "Stay safe  weak storm , DST is {}".format(prediction))
    elif prediction>-100 :
        return render_template("index.html", prediction_text = "Don't worry moderate storm ,DST is {}".format(prediction))
    elif prediction>-200 :
        return render_template("index.html", prediction_text = "Warring, strong storm ,DST is {}".format(prediction))
    elif prediction>-350 :
        return render_template("index.html", prediction_text = "Warring, severe storm ,DST is {}".format(prediction))
    else :
        return render_template("index.html", prediction_text = "Warring, great storm ,DST is {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)
