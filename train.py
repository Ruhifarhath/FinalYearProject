import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

# Function to load data
def load_data(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# Function to preprocess data
def preprocess_data(df):
    df = df.copy()
    
    # Handle missing values
    df.dropna(inplace=True)

    # Encode categorical columns
    label_encoders = {}
    categorical_columns = ['Flexibility Level', 'Injury', 'Medical Condition', 'Pose', 'Risk Level']
    
    for column in categorical_columns:
        if column in df.columns:
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            label_encoders[column] = le
    
    X = df.drop(columns=['Risk Level'])
    y = df['Risk Level']
    
    return X, y, label_encoders

# Function to train model
def train_model(X, y):
    if X.empty or y.empty:
        st.error("❌ No valid data available for training. Check dataset formatting.")
        return None, None, None, None, None, None, None
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, scaler, X_train, X_test, y_test, accuracy, X.columns

# Streamlit app
st.title("🧘‍♂️ Yoga Risk Prediction Model")

uploaded_file = st.file_uploader("synthetic_yoga_dataset", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)

    if df is not None:
        st.write("### Dataset Preview")
        st.write(df.head())

        X, y, label_encoders = preprocess_data(df)

        model, scaler, X_train, X_test, y_test, accuracy, feature_names = train_model(X, y)

        if model:
            st.write(f"### ✅ Model Accuracy: {accuracy:.2%}")

            # User input for prediction
            st.sidebar.header("🔍 Make a Prediction")
            user_input = {}

            for col in feature_names:
                user_input[col] = st.sidebar.text_input(f"Enter {col}:", "")

            if st.sidebar.button("Predict"):
                try:
                    input_data = np.array([float(user_input[col]) for col in feature_names]).reshape(1, -1)
                    input_scaled = scaler.transform(input_data)
                    prediction = model.predict(input_scaled)
                    st.sidebar.success(f"Predicted Risk Level: {prediction[0]}")
                except ValueError:
                    st.sidebar.error("⚠️ Please enter valid numerical values.")

# Instructions
st.write("""
### 📌 Instructions:
1. **Upload a CSV file** containing yoga-related data.
2. The app will **preprocess** the data and **train a model**.
3. Enter values in the **sidebar** to make predictions.
""")
