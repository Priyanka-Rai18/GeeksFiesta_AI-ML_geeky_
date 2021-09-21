import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import model as p


app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
      year=request.form.get("year")
      month=request.form.get("month")
      day=request.form.get("day")
      hour=request.form.get("hour")
      temperature=request.form.get("temperature")
      pressure=request.form.get("pressure")
      rain=request.form.get("rain")
      wind_direction=request.form.get("wind_direction")
      wind_speed=request.form.get("wind_speed")
      pm_pred=p.prediction(year,month,day,hour,temperature,pressure,rain,wind_direction,wind_speed)
      pm=pm_pred
  
    return render_template('input.html',output=pm)
'''
@app.route('/predict',methods=['GET','POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('input.html', prediction_text='PM2.5 prediction {}'.format(output))
    '''
'''
@app.route('/predict_api',methods=['GET','POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
    '''

if __name__ == "__main__":
    app.run(debug=True)
        
