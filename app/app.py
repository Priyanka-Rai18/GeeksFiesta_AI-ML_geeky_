# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def PM2():
   # return render_template('input.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
   # if request.method == 'POST':
      # result = request.form
      # return render_template("PM2.html",result = result)

# if __name__ == '__main__':
   # app.run(debug = True)
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = reg.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='PM2.5 concentration {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
