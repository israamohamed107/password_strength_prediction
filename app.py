import streamlit as st
import joblib 

def split(statment):
    return [ch for ch in statment]

model=joblib.load('model.h5')
vectorizer = joblib.load('vectorizer.h5')
selected_features_indices= joblib.load('selected_features_indices.h5')

st.title('Password Strength Prediction')

password=st.text_input('Enter Your Password')
password=vectorizer.transform([password])

prediction=model.predict(password.toarray()[0][selected_features_indices].reshape((1,-1)))[0]
if st.button('Predict'):
    if prediction==0:
        st.success('This is a week pasword , suggest using another one')
    elif prediction==1:
        st.success('This is a medium strength password')
    else:
        st.success('This is a strong password')