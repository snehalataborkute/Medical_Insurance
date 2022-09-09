from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from Project_app.utils import MedicalInsurence


app = Flask(__name__)

########################## Login API ######################################


# @app.route('/') 
# def hello_flask():
#     return 'Welcome to Flask'



# ################################ POST MAN ################################

# @app.route('/predict_charges',methods = ['POST','GET'])
# def get_insurence_charges():

#     data = request.form
#     age = eval(data['age'])
#     sex = data['sex']
#     bmi = eval(data['bmi'])
#     children = eval(data['children'])
#     smoker = data['smoker']
#     region = data['region']

    
#     object = MedicalInsurence(age, sex, bmi,children,smoker, region)
#     prediction = object.get_predicted_charges()

#     return jsonify({"Result": f"Predicted Medical Insurence Charges are : {prediction}"})

    
 
################################# HTML Test ##############################################

@app.route('/') 
def main():
    return render_template('index.html')


@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        
        age = request.form['age']
        sex = request.form['sex']
        bmi = request.form['bmi']
        children = request.form['children']
        smoker = request.form['smoker']
        region = request.form['region']
        
        object = MedicalInsurence(age, sex, bmi,children,smoker, region)
        prediction = object.get_predicted_charges()

        return render_template("result.html", prediction = prediction)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = 5004,debug=False)