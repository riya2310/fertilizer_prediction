from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('classifier.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    if request.form['d']=="Black":
     data4= 0
    
    elif request.form['d']=="Clayey":
     data4 = 1
    
    elif request.form['d']=="Loamy":
     data4 = 2
    
    elif request.form['d']=="Red":
     data4 = 3
    
    elif request.form['d']=="Sandy":
     data4 = 4
    

    if request.form['e']=="Barley":
      data5 = 0
    
    elif request.form['e']=="Cotton":
      data5 = 1
    
    elif request.form['e']=="Ground Nuts":
      data5 = 2
    
    elif request.form['e']=="Maize":
      data5 = 3
    
    elif request.form['e']=="Millets":
      data5 = 4
    
    elif request.form['e']=="Oil seeds":
      data5 = 5
    
    elif request.form['e']=="Paddy":
      data5 = 6
    
    elif request.form['e']=="Pulses":
      data5 = 7
    
    elif request.form['e']=="Sugarcane":
      data5 = 8
      
    elif request.form['e']=="Tobacco":
      data5 = 9
    
    elif request.form['e']=="Wheat":
      data5 = 10
    
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)