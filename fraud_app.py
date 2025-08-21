import streamlit as st
import joblib
import pandas as pd

model = joblib.load(r'C:\Users\Hp\Downloads\Fraud\Fraud_pipeline.pkl')

st.title('Fraud Detection Prediction app')

st.markdown('Please enter transaction details and use predict button')

st.divider()

transaction_type = st.selectbox('Transaction Type',['PAYMENT','TRANSFER','CASH_OUT','DEPOSIT'])
amount = st.number_input('amount',min_value=0.0,value=1000.0)
oldbalanceOrg = st.number_input('old balance(sender)', min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input('new balance(sender)', min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input('old balance(recipient)', min_value=0.0, value=0.0)
newbalanceDest = st.number_input('new balance(recipient)', min_value=0.0, value=0.0)

if st.button('predict'):
  input_data = pd.DataFrame([{
      'type':transaction_type,
      'amount':amount,
      'oldbalanceOrg':oldbalanceOrg,
      'newbalanceOrig':newbalanceOrig,
      'oldbalanceDest':oldbalanceDest,
      'newbalanceDest':newbalanceDest
  }])
  prediction = model.predict(input_data)[0]
  st.subheader(f'prediction:{int(prediction)}')

  if prediction ==1:
    st.error('this transaction might be fraud')
  else:
    st.success('this transaction is legitimate')
