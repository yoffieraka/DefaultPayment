import streamlit as st
import pandas as pd
import json
import joblib
import pickle

path = "C:\\Users\\Adrian\\projecthacktiv8\\gradedchallenge5deployment\\gc5deployment\\"
# load file
with open("model_scaling.pkl", "rb") as file_1:
  model_scaling = joblib.load(file_1)

with open("model_OE.pkl", "rb") as file_2:
  model_ord = joblib.load(file_2)

with open("model_logreg.pkl", "rb") as file_3:
  logreg = joblib.load(file_3)

with open("model_svm.pkl", "rb") as file_4:
  svm = joblib.load(file_4)  

with open("model_knn.pkl", "rb") as file_5:
  knn = joblib.load(file_5)

with open("list_ord_cols.txt", "r") as file_6:
  ord_cols_oe = json.load(file_6)

with open("list_num_cols.txt", "r") as file_7:
  num_cols = json.load(file_7)

with open("model_selected_features.txt", "r") as file_8:
  sel_features = json.load(file_8)

def run():
    # Membuat Form
    with st.form(key='form_credit_default_check'):
            limit_balance = st.number_input('limit_balance', min_value=0, max_value=1000000, value=5000, help='limit'), 
            sex = st.slider('sex', 1,2,0), 
            education_level = st.slider('education_level', 0,4,2),
            marital_status = st.slider('marital_status', 1,3,2), 
            age = st.number_input('age', min_value=17, max_value=100, value=25, help='Umur'), 
            pay_0 = st.slider('pay_0', -2,9,0), 
            pay_2 = st.slider('pay_2', -2,9,0), 
            pay_3 = st.slider('pay_3', -2,9,0), 
            pay_4 = st.slider('pay_4', -2,9,0), 
            pay_5 = st.slider('pay_5', -2,9,0), 
            pay_6 = st.slider('pay_6', -2,9,0), 
            bill_amt_1 = st.slider('bill_amt_1', 0,10000,5000), 
            bill_amt_2 = st.slider('bill_amt_2', 0,10000,5000), 
            bill_amt_3 = st.slider('bill_amt_3', 0,10000,5000), 
            bill_amt_4 = st.slider('bill_amt_4', 0,10000,5000), 
            bill_amt_5 = st.slider('bill_amt_5', 0,10000,5000), 
            bill_amt_6 = st.slider('bill_amt_6', 0,10000,5000), 
            pay_amt_1 = st.slider('pay_amt_1', 0,10000,5000), 
            pay_amt_2 = st.slider('pay_amt_2', 0,10000,5000), 
            pay_amt_3 = st.slider('pay_amt_3', 0,10000,5000), 
            pay_amt_4 = st.slider('pay_amt_4', 0,10000,5000), 
            pay_amt_5 = st.slider('pay_amt_5', 0,10000,5000), 
            pay_amt_6 = st.slider('pay_amt_6', 0,10000,5000)

            submitted = st.form_submit_button('Predict')

    data_inf = {
              'limit_balance' : limit_balance[0],
              'sex' : sex,
              'education_level' : education_level,
              'marital_status' : marital_status,
              'age' : age,
              'pay_0' : pay_0[0],
              'pay_2' : pay_2[0],
              'pay_3' : pay_3[0],
              'pay_4' : pay_4[0],
              'pay_5' : pay_5[0],
              'pay_6' : pay_6[0],
              'bill_amt_1' : bill_amt_1[0],
              'bill_amt_2' : bill_amt_2[0],
              'bill_amt_3' : bill_amt_3[0],
              'bill_amt_4' : bill_amt_4[0],
              'bill_amt_5' : bill_amt_5[0],
              'bill_amt_6' : bill_amt_6[0],
              'pay_amt_1' : pay_amt_1[0],
              'pay_amt_2' : pay_amt_2[0],
              'pay_amt_3' : pay_amt_3[0],
              'pay_amt_4' : pay_amt_4[0],
              'pay_amt_5' : pay_amt_5[0],
              'pay_amt_6' : pay_amt_6
    } #Key harus sama dengan column di dataset

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    print(data_inf)

    if submitted:
        data_inf_selected = data_inf[sel_features]
        print(data_inf_selected[ord_cols_oe])
        # Feature Scaling and Feature Encoding
        data_inf_selected[ord_cols_oe] = model_ord.transform(data_inf_selected[ord_cols_oe])
        data_inf_selected[num_cols] = model_scaling.transform(data_inf_selected[num_cols])
        # Predict using Linear Regression
        y_pred_inf = logreg.predict(data_inf_selected)
        st.write('# Prediction Logistic Regression: ',str(int(y_pred_inf)))
        y_pred_inf = svm.predict(data_inf_selected)
        st.write('# Prediction SVM: ',str(int(y_pred_inf)))
        y_pred_inf = knn.predict(data_inf_selected)
        st.write('# Prediction KNN: ',str(int(y_pred_inf)))

if __name__ == '__main__':
    run()
