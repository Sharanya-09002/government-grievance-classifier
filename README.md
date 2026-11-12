# Government Grievance Classification

## Project Description
This project uses Machine Learning to classify citizen complaints into the appropriate government department.
A simple machine learning application that classifies government complaints into Water, Electricity, and Sanitation departments using Python and Streamlit

The application identifies complaints belonging to one of three departments:

- Water
- Electricity
- Sanitation

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Joblib
- Streamlit
- GitHub

## How It Works
1. A machine learning model is trained using sample complaint data.
2. The trained model is saved as a file.
3. The model is loaded into a Streamlit web application.
4. A user enters a complaint.
5. The application predicts the responsible department.

## Project Files
- `app.py` – Streamlit web application
- `grievance_model.pkl` – Trained machine learning model
- `requirements.txt` – Required Python libraries

## Note
This is a demonstration project using a small sample dataset. Predictions are for educational purposes and should not be used for actual government complaint routing without further validation.
