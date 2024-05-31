import joblib
import json
import pandas as pd

__log_reg_covid = None
__columns = None

def predict_covid(
    USMER,
    MEDICAL_UNIT,
    PATIENT_TYPE,
    PNEUMONIA,
    AGE,
    DIABETES,
    HIPERTENSION,
    RENAL_CHRONIC,
    CLASIFFICATION_FINAL):
    

    new_sample = pd.DataFrame({
        "USMER": [USMER],
        "MEDICAL_UNIT": [MEDICAL_UNIT],
        "PATIENT_TYPE": [PATIENT_TYPE],
        "PNEUMONIA": [PNEUMONIA],
        "AGE": [AGE],
        "DIABETES": [DIABETES],
        "HIPERTENSION": [HIPERTENSION],
        "RENAL_CHRONIC": [RENAL_CHRONIC],
        "CLASIFFICATION_FINAL": [CLASIFFICATION_FINAL],
    })

    x = pd.DataFrame(new_sample)
    x.columns = __columns

    predict = str(__log_reg_covid.predict(x)[0])
    if predict == "0":
        result = "Tỷ lệ tử vong thấp"
    else:
        result = "Tỷ lệ tử vong cao"
    return result

def load_saved_artifacts():
    print("Loading saved arrtifact...starting")
    global __columns
    with open('Artifacts/columns.json', ) as f:
            __columns = json.load(f)

    global __log_reg_covid
    if __log_reg_covid is None:
        with open('Artifacts/log_reg_covid.sav', 'rb') as f:
            __log_reg_covid = joblib.load(f)
    print("Loading saved articfacts...done")
    

def get_columns():
    return __columns

if __name__ == '__main__':
    load_saved_artifacts()
    
