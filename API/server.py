from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/get_artifacts', methods=['GET'])

def get_location_names():
    response = jsonify({
        'columns': util.get_columns()
    })
    
    response.headers.add('Access-Control-Allow_Origin', '*')
    return response 


@app.route('/predict_covid', methods=['GET', 'POST'])

def predict():
    USMER= int(request.form['USMER'])
    MEDICAL_UNIT = int(request.form['MEDICAL_UNIT'])
    PATIENT_TYPE= int(request.form['PATIENT_TYPE'])
    PNEUMONIA= int(request.form['PNEUMONIA'])
    AGE= int(request.form['AGE'])
    DIABETES= int(request.form['DIABETES'])
    HIPERTENSION= int(request.form['HIPERTENSION'])
    RENAL_CHRONIC= int(request.form['RENAL_CHRONIC'])
    CLASIFFICATION_FINAL= int(request.form['CLASIFFICATION_FINAL'])
    
    
    response = jsonify({
        'predict_covid': util.predict_covid(
            USMER,
            MEDICAL_UNIT,
            PATIENT_TYPE,
            PNEUMONIA,
            AGE,
            DIABETES,
            HIPERTENSION,
            RENAL_CHRONIC,
            CLASIFFICATION_FINAL)
    })
    
    response.headers.add('Access-Control-Allow_Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Prediction...")
    util.load_saved_artifacts()
    app.run()