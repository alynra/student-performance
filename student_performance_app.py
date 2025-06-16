import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from prediction import prediction  

from data_preprocessing import (
    encoder_Application_mode, encoder_Course, encoder_Daytime_evening_attendance,
    encoder_Debtor, encoder_Displaced, encoder_Educational_special_needs,
    encoder_Fathers_occupation, encoder_Fathers_qualification, encoder_Gender,
    encoder_International, encoder_Marital_status, encoder_Mothers_occupation,
    encoder_Mothers_qualification, encoder_Nacionality,
    encoder_Previous_qualification, encoder_Scholarship_holder,
    encoder_Tuition_fees_up_to_date
)

st.set_page_config(page_title="Student Status Predictor", layout="wide")

# Custom Style
st.markdown("""
    <style>
        .title { font-size:40px !important; color: #4B8BBE; }
        .stSelectbox, .stSlider, .stNumberInput { margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Student Status Predictor</h1>", unsafe_allow_html=True)

with st.expander("ℹ️ About this app"):
    st.write("""
        This app predicts a student's academic status (Graduate, Dropout, or Enrolled)
        based on their academic and socio-demographic profile.
    """)

# Create empty DataFrame
data = pd.DataFrame()

# Tabs for grouping input
tab1, tab2, tab3 = st.tabs(["🧍 Personal Info", "📚 Academic Info", "📈 Economic Info"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        data["Gender"] = [st.selectbox("Gender", encoder_Gender.classes_)]
        data["Marital_status"] = [st.selectbox("Marital Status", encoder_Marital_status.classes_)]
        data["Nacionality"] = [st.selectbox("Nationality", encoder_Nacionality.classes_)]
    
    with col2:
        data["Displaced"] = [st.selectbox("Displaced", encoder_Displaced.classes_)]
        data["Scholarship_holder"] = [st.selectbox("Scholarship Holder", encoder_Scholarship_holder.classes_)]
        data["Educational_special_needs"] = [st.selectbox("Special Educational Needs", encoder_Educational_special_needs.classes_)]

    with col3:
        data["International"] = [st.selectbox("International Student", encoder_International.classes_)]
        data["Debtor"] = [st.selectbox("Debtor", encoder_Debtor.classes_)]
        data["Tuition_fees_up_to_date"] = [st.selectbox("Tuition Fees Up to Date", encoder_Tuition_fees_up_to_date.classes_)]

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        data["Application_mode"] = [st.selectbox("Application Mode", encoder_Application_mode.classes_)]
        data["Application_order"] = [st.slider("Application Order", 0, 9, 1)]
        data["Admission_grade"] = [st.slider("Admission Grade", 0, 200, 150)]

    with col2:
        data["Course"] = [st.selectbox("Course", encoder_Course.classes_)]
        data["Previous_qualification"] = [st.selectbox("Previous Qualification", encoder_Previous_qualification.classes_)]
        data["Previous_qualification_grade"] = [st.slider("Previous Qualification Grade", 0, 200, 150)]

    with col3:
        data["Daytime_evening_attendance"] = [st.selectbox("Attendance Type", encoder_Daytime_evening_attendance.classes_)]
        data["Age_at_enrollment"] = [st.slider("Age at Enrollment", 17, 60, 25)]

with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        data["Mothers_qualification"] = [st.selectbox("Mother's Qualification", encoder_Mothers_qualification.classes_)]
        data["Fathers_qualification"] = [st.selectbox("Father's Qualification", encoder_Fathers_qualification.classes_)]

    with col2:
        data["Mothers_occupation"] = [st.selectbox("Mother's Occupation", encoder_Mothers_occupation.classes_)]
        data["Fathers_occupation"] = [st.selectbox("Father's Occupation", encoder_Fathers_occupation.classes_)]

    with col3:
        data["Unemployment_rate"] = [st.number_input("Unemployment Rate", value=85)]
        data["Inflation_rate"] = [st.number_input("Inflation Rate", value=20)]
        data["GDP"] = [st.number_input("GDP", value=200)]

# Preview Input
with st.expander("📄 View Input Data"):
    st.dataframe(data)

# Prediction
if st.button("Predict Student Status"):
    preprocessed_data = data_preprocessing(data)
    with st.expander("🔍 Preprocessed Data"):
        st.dataframe(preprocessed_data)
    pred = prediction(preprocessed_data)
    st.success(f"🎓 Predicted Student Status: {pred}")
