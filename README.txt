*************************************************
* Trường Đại học Sài Gòn (SGU)                  *
* Họ tên sinh viên: Nguyễn Hoàng Tuấn           *
* Mã số sinh viên: 3121410556                   *
* Khóa: 2021-2026                               *
* Giảng viên hướng dẫn: ThS. Nguyễn Thanh Phước *
* Năm học: 2023-2024                            *
*************************************************

                             Môn học: Khai phá dữ liệu và ứng dụng (Data Mining)

      Đề tài: Sử dụng thuật toán Logistic Regression dự đoán tỉ lệ tử vong của bệnh nhân covid 19 ở Mexico

1. Các tập tin bao gồm:
	- Folder "Data": chứa dataset file csv 'Covid Data' để training model.

	- Folder "Document":
	    + File "Logistic_Regression_Covid.docx": là tập tin 'word' bản tài liệu báo cáo đề tài gốc.
	    + File "Logistic_Regression_Covid.pdf": là tập tin 'PDF' của báo cáo (Lỡ bản gốc có bị vấn đề).

	- Folder "Model": chứa Notebook chương trình python 'Logistic_Regression_Covid.ipynb'.

	- Folder "Artifacts": gồm những file 'json' và 'sav' để lưu những giá trị cần thiết
	    + File "columns.json": chứa các các tên các đặc trưng (cột) của mô hình đã huấn luyện.
	    + File "streamlit.json": chứa các chart để trực quan hóa dữ liệu bằng PyWalker của framework Kanaries
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

4. Link Souce code:
    - Github: https://github.com/NguyenHoangTuanDev/ML_Logistic-Regression_Covid19.git

    - Kaggle:  https://www.kaggle.com/code/nguyenhoangtuan6103/model-machine-leaning-covid-19-logistic-regression

    - Google Colab: https://colab.research.google.com/drive/1lGwDOiCiIcwmIejJIV03qHhLeoOhi8X6?usp=sharing

5. Các framework đã sử dụng:
    - Streamlit: https://streamlit.io

    - Kanaries: https://kanaries.net/pygwalker

