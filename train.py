import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

def load_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)  # Remove missing values
    return df

def preprocess_data(df):
    label_encoders = {}
    categorical_columns = ['Flexibility Level', 'Injury', 'Medical Condition', 'Pose', 'Risk Level']
    
    for column in categorical_columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    
    X = df.drop(columns=['Risk Level'])
    y = df['Risk Level']
    return X, y, label_encoders

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, scaler, accuracy

def predict_risk(model, scaler, user_input, label_encoders):
    input_df = pd.DataFrame([user_input])
    
    for column in label_encoders:
        if column in input_df.columns:
            if input_df[column][0] not in label_encoders[column].classes_:
                # Handle unseen label by assigning a default known category
                input_df[column] = label_encoders[column].transform([label_encoders[column].classes_[0]])
            else:
                input_df[column] = label_encoders[column].transform([input_df[column][0]])
    
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    
    return prediction


def main():
    st.title("Risk Prediction Model")
    file_path = "synthetic_yoga_dataset.csv"
    df = load_data(file_path)
    
    X, y, label_encoders = preprocess_data(df)
    model, scaler, accuracy = train_model(X, y)
    
    st.sidebar.header("User Input")
    age = st.sidebar.number_input("Age", min_value=10, max_value=100, step=1)
    weight = st.sidebar.number_input("Weight", min_value=30, max_value=200, step=1)
    
    flexibility_options = ['Low', 'Medium', 'High']
    injury_options = ['None', 'Minor', 'Severe']
    medical_options = ['None', 'Hypertension', 'Arthritis', 'Heart Condition']
    pose_options = ['Child’s Pose', 'Downward Dog', 'Tree Pose']
    
    flexibility = st.sidebar.selectbox("Flexibility Level", flexibility_options)
    injury = st.sidebar.selectbox("Injury", injury_options)
    medical_condition = st.sidebar.selectbox("Medical Condition", medical_options)
    pose = st.sidebar.selectbox("Pose", pose_options)
    
    user_input = {
        "Age": age,
        "Weight": weight,
        "Flexibility Level": flexibility,
        "Injury": injury,
        "Medical Condition": medical_condition,
        "Pose": pose
    }
    
    pose_precautions = {
        "Child’s Pose": {
            "Pre-Asana": "Avoid if you have knee injuries, severe back pain, or pregnancy (late stages).",
            "Post-Asana": "Avoid doing intense backbends immediately after this pose."
        },
        "Downward Dog": {
            "Pre-Asana": "Avoid if you have wrist injuries or high blood pressure.",
            "Post-Asana": "Rest in Child’s Pose after holding this posture."
        },
        "Tree Pose": {
            "Pre-Asana": "Avoid if you have balance issues or ankle injuries.",
            "Post-Asana": "Do some ankle stretches after holding this pose."
        }
    }
    
    if st.sidebar.button("Predict Risk"):
        risk_prediction = predict_risk(model, scaler, user_input, label_encoders)
        risk_label = label_encoders['Risk Level'].inverse_transform([risk_prediction])[0]
        
        st.write(f"**Predicted Risk Level:** {risk_label}")
        
        if pose in pose_precautions:
            st.write("**Pre-Asana Precautions:**", pose_precautions[pose]["Pre-Asana"])
            st.write("**Post-Asana Precautions:**", pose_precautions[pose]["Post-Asana"])
        
if __name__ == "__main__":
    main()
