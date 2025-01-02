import streamlit as st
import pandas as pd
import joblib

st.title('User Details Form to predict Salary')

age = st.number_input('Age', min_value = 0, max_value = 120, step = 1, value = None)
gender = st.selectbox('Gender', ['-', 'Male', 'Female', 'Other'])
education_level = st.selectbox('Education Level', ['-', 'nan', 'High School', 'Bachelor"s', 'Master"s', 'PHD'])
job_title = st.text_input('Job Title')
experience = st.number_input('Years of Experience', min_value = 0, max_value = 40, step = 1, value = None)

if st.button('Submit'):
    data = {
        'Age': [age],
        'Gender': [gender],
        'Education Level': [education_level],
        'Job Title': [job_title],
        'Years of Experience': [experience]
    }
    df = pd.DataFrame(data)
    
    st.table(df)

    # model = joblib.load('random_forest_regressor_model.pkl')
    model = joblib.load('model.joblib')
    
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education Level': [education_level],
        'Job Title': [job_title],
        'Years of Experience': [experience]
    })
    
    prediction = model.predict(input_data)
    
    st.write(f'Predicted Salary: {prediction[0]}')