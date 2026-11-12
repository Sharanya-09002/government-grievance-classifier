
import streamlit as st
import joblib

# Load the trained model
model = joblib.load("grievance_model.pkl")

# Application title
st.title("Government Grievance Classification")

st.write("Enter a complaint to identify the responsible department.")

# Input box
complaint = st.text_area("Enter your complaint:")

# Prediction button
if st.button("Classify Complaint"):

    if complaint.strip():

        prediction = model.predict([complaint])

        st.success("Predicted Department: " + prediction[0])

    else:
        st.warning("Please enter a complaint.")
