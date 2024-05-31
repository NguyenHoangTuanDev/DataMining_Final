import json
import streamlit as st
import joblib
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd

st.set_page_config(
    page_title="Model Logistic_Regression_Covid 19",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
  
tab1, tab2, tab3, tab4 = st.tabs(['Home', 'Visualization', 'Download', 'About us'])

with tab1:
    
    st.write('''
    # Form prediction patient
    ''')

    col1, col2 = st.columns(2)

    with col1:
        USMER = st.number_input('USMER:', value=2, max_value=2)

        MEDICAL_UNIT = st.number_input('MEDICAL_UNIT:', value=1, max_value=13)

        PATIENT_TYPE = st.number_input('PATIENT_TYPE:', value=1,  max_value=2)

        PNEUMONIA = st.number_input('PNEUMONIA:', value=1,  max_value=2)


    with  col2:
        AGE = st.slider('AGE:', value=65, max_value=120)

        DIABETES = st.number_input('DIABETES', value=2, max_value=2)

        HIPERTENSION = st.number_input('HIPERTENSION', value=1, max_value=2)

        RENAL_CHRONIC = st.number_input('RENAL_CHRONIC', value=2, max_value=2)

        CLASIFFICATION_FINAL = st.number_input('CLASIFFICATION_FINAL', value=1, max_value=2)


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
        with open("Artifacts/log_reg_covid.sav", 'rb') as f:
            __log_reg_covid = joblib.load(f)
        predict = str(__log_reg_covid.predict(x)[0])
        return predict

    if st.button('Compute a prediction'):
        predict = predict_covid(
            USMER,
            MEDICAL_UNIT,
            PATIENT_TYPE,
            PNEUMONIA,
            AGE,
            DIABETES,
            HIPERTENSION,
            RENAL_CHRONIC,
            CLASIFFICATION_FINAL)

        st.success('Done')

        if predict == '0':
            st.write('Tỷ lệ tử vong thấp')
        else:
            st.write('Tỷ lệ tử vong cao')


with tab2: 
    
    df = pd.read_csv("Data/Covid Data.csv")

    # Getting rid of the missing values of features except "INTUBED", "PREGNANT", "ICU"
    cols = ['PNEUMONIA', 'DIABETES', 'COPD', 'ASTHMA', 'INMSUPR', 'HIPERTENSION',
            'OTHER_DISEASE', 'CARDIOVASCULAR', 'OBESITY', 'RENAL_CHRONIC', 'TOBACCO']
    for i in cols:
        df = df[(df[i] == 1) | (df[i] == 2)]

    # Preaparing "DATE_DIED" column
    df['DEATH'] = [2 if row == "9999-99-99" else 1 for row in df.DATE_DIED]

    # Droping the columns
    df.drop(columns=["DATE_DIED"], inplace=True)

    # Converting process according to inference above
    df.PREGNANT = df.PREGNANT.replace(97, 2)
    # Getting rid of the missing values
    df = df[(df.PREGNANT == 1) | (df.PREGNANT == 2)]

    df.CLASIFFICATION_FINAL = df.CLASIFFICATION_FINAL.replace([1, 2, 3], 1)
    df.CLASIFFICATION_FINAL = df.CLASIFFICATION_FINAL.replace([4, 5, 6, 7], 2)

    pyg_app = StreamlitRenderer(df, spec='Artifacts/streamlit.json')
    pyg_app.render_explore()
    

with tab3:

    with open('Data\Covid Data.csv') as f:
        st.download_button('Download CSV', f)  

    st.link_button("Download PDF", "https://drive.google.com/file/d/1SztGQBgiJlBq6EM1J6UErkdBkOLsM5_H/view?usp=drive_link")

    st.link_button("Download Project", "https://drive.google.com/file/d/1SztGQBgiJlBq6EM1J6UErkdBkOLsM5_H/view?usp=drive_link")

    st.write('Thanks for downloading!')

with tab4:
    st.write('''
             
- Trường Đại học Sài Gòn (SGU)      
- Họ tên sinh viên: Nguyễn Hoàng Tuấn          
- Mã số sinh viên: 3121410556                             
- Giảng viên hướng dẫn: ThS. Nguyễn Thanh Phước

*******************************************************************************************************
- Môn học: Khai phá dữ liệu và ứng dụng (Data Mining)
- Đề tài: Sử dụng thuật toán Logistic Regression dự đoán tỉ lệ tử vong của bệnh nhân covid 19 ở Mexico
- Năm học: 2023-2024

******************************************************************************************************
1. Các tập tin bao gồm:
	- Folder "Data": chứa dataset file csv 'Covid Data' để training model.

	- Folder "Document":
	    + File "Logistic_Regression_Covid.docx": là tập tin 'word' bản tài liệu báo cáo đề tài gốc.
	    + File "Logistic_Regression_Covid.pdf": là tập tin 'PDF' của báo cáo (Lỡ bản gốc có bị vấn đề).

	- Folder "Model": chứa Notebook chương trình python 'Logistic_Regression_Covid.ipynb'.

	- Folder "Artifacts": gồm những file 'json' và 'sav' để lưu những giá trị cần thiết
	    + File "columns.json": chứa các các tên các đặc trưng (cột) của mô hình đã huấn luyện.
	    + File "artifact.json": chứa các chú thích của các đặc trưng.
	    + File "log_reg_covid.sav": dùng thư viện joblib để luư model đã huấn luyện.

	- Folder "API": Gồm 2 file chương trình .py
	    + File "server": là chương trình chạy 'API' (test trên Postman)
	    + File "util": là chương trình chứa các hàm để chạy API trong 'server'.

	- Folder "App": là chương trình chạy 'web_app' local
	    + File "app.py": là chương trình chính của web_app sử dụng framework 'Streamlit' và nhúng
	                     thư viện 'PyWalker' để trực quan hóa dữ liệu.
	    + File "requirements.txt": chứa các version thư viện cần thiết để cài đặt deploy trên 'Streamlit Cloud'

2. Link dataset:
    - Mexican government: https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico

    - Kaggle: https://www.kaggle.com/datasets/meirnizri/covid19-dataset

3. Link deploy web_app: https://predict-covid.streamlit.app

4. Link Souce code Moddel (ipynb)
    - Github: https://github.com/NguyenHoangTuanDev/ML_Logistic-Regression_Covid19.git

    - Kaggle: https://www.kaggle.com/code/nguyenhoangtuan6103/model-machine-leaning-covid-19-logistic-regression

    - Google Colab: https://colab.research.google.com/drive/1lGwDOiCiIcwmIejJIV03qHhLeoOhi8X6?usp=sharing

5. Các framework đã sử dụng:
    - Streamlit: https://streamlit.io

    - Kanaries: https://kanaries.net/pygwalker

***************************************************************************************************************                          
- Email: hoangtuan6103@gmail.com
- Facebook: https://www.facebook.com/nguyenhoangtuan6103                                                                                          
- Youtube: https://www.youtube.com/@nguyenhoangtuan6103                                                                                          

***************************************************************************************************************                                                                                        
Mọi ý kiến đóng góp của các bạn mình đều ghi nhận.           
Xin chân thành cảm ơn.                                                                             
'''
)