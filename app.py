
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓"
)

@st.cache_resource
def load_model():
    return joblib.load("student_performance_model (3) (1).pkl")

model = load_model()

st.title("🎓 Student Performance Prediction")
st.write("Predict student final grades and get personalized learning recommendations.")

studytime = st.selectbox("Study Time", [1, 2, 3, 4])
failures = st.number_input("Failures", min_value=0, max_value=4, value=0)
absences = st.number_input("Absences", min_value=0, max_value=100, value=2)
g1 = st.number_input("G1 Grade", min_value=0, max_value=20, value=10)
g2 = st.number_input("G2 Grade", min_value=0, max_value=20, value=10)

if st.button("Predict Final Grade"):

    student = pd.DataFrame([{
        "school": "GP",
        "sex": "F",
        "age": 17,
        "address": "U",
        "famsize": "GT3",
        "Pstatus": "T",
        "Medu": 2,
        "Fedu": 2,
        "Mjob": "other",
        "Fjob": "other",
        "reason": "course",
        "guardian": "mother",
        "traveltime": 1,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": "no",
        "famsup": "yes",
        "paid": "no",
        "activities": "yes",
        "nursery": "yes",
        "higher": "yes",
        "internet": "yes",
        "romantic": "no",
        "famrel": 4,
        "freetime": 3,
        "goout": 3,
        "Dalc": 1,
        "Walc": 1,
        "health": 3,
        "absences": absences,
        "G1": g1,
        "G2": g2
    }])

    prediction = model.predict(student)[0]

    st.success(f"Predicted Final Grade: {prediction:.2f} / 20")

    if prediction < 10:
        st.warning("Recommendation: Practice basic topics and seek teacher support.")
    elif prediction < 15:
        st.info("Recommendation: Follow a regular study timetable and revise daily.")
    else:
        st.success("Recommendation: Continue regular revision.")
