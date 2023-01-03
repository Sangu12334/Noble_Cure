import json
import pickle
import math
import numpy as np
import webbrowser as wb
from flask import Flask, request, render_template

app = Flask(__name__)
Model1 = open('model123.pkl', 'rb')
model = pickle.load(Model1)
Model1.close()



@app.route("/")
def home():
    return render_template('front.html')


@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == "POST":
        age = int(request.form.get("AGE"))
        height = int(request.form["HEIGHT"])
        weight = int(request.form["weight"])
        gender = int(request.form["GENDER"])
        travelled = int(request.form["TRAVELLED/NOT"])
        Tiredness = int(request.form["TIERDNESS"])
        F_days = int(request.form["F_DAYS"])
        f_temp = int(request.form["F_TEMP"])
        cold_t = int(request.form["COLD_TYPE"])
        cold_d = int(request.form["COLD_DAYS"])
        cough_t = int(request.form.get("COUGH_TYPE",False))
        cough_days = int(request.form["COUGH_DAYS"])
        DIARRHEA = int(request.form["DIARRHEA_TYPE"])
        vomit = int(request.form["VOMIT"])
        Bodyache = int(request.form["BODYACHE"])

        x_test = [age,height,weight,gender,travelled,Tiredness,F_days,f_temp,cold_t,cold_d,cough_t,cough_days,DIARRHEA,vomit,Bodyache]
        x_test = np.asarray(x_test).astype(np.int64)
        prediction = model.predict([x_test])
        pres_value = print(prediction)

        return render_template('front.html',prediction_text="Here is your prescription  is : {}".format(prediction))



if __name__ == "__main__":
    app.run(debug=True)
