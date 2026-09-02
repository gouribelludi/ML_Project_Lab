import streamlit as st

# Page settings
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Performance Predictor")
st.write("Enter the student's details below to estimate their exam performance.")

# Sidebar
st.sidebar.header("Student Information")

name = st.sidebar.text_input("Student Name")
age = st.sidebar.number_input("Age", min_value=10, max_value=30, value=18)
study_hours = st.sidebar.slider("Daily Study Hours", 0, 12, 4)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 75)

# Main section
st.header("📊 Student Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Age", age)

with col2:
    st.metric("Study Hours", study_hours)

with col3:
    st.metric("Attendance", f"{attendance}%")

# Prediction
st.header("🔮 Performance Prediction")

# Simple calculation
predicted_marks = (
    study_hours * 5
    + attendance * 0.3
    + age * 1
)

# Keep marks between 0 and 100
predicted_marks = min(100, max(0, predicted_marks))

st.subheader(f"Predicted Marks: {predicted_marks:.1f}%")

# Progress bar
st.progress(int(predicted_marks))

# Result
if predicted_marks >= 75:
    st.success("🌟 Excellent Performance!")
elif predicted_marks >= 50:
    st.info("👍 Good Performance. Keep studying!")
else:
    st.warning("⚠️ More study is recommended.")

# Student name
if name:
    st.write(f"### Hello, {name}! 👋")
else:
    st.write("### Please enter the student's name in the sidebar.")

# Study analysis
st.header("📚 Study Analysis")

if study_hours < 3:
    st.write("You should try to study at least 3 hours per day.")
elif study_hours < 6:
    st.write("Your study time is reasonable. Keep it consistent.")
else:
    st.write("Excellent study schedule! Keep maintaining it.")

# Attendance analysis
if attendance >= 85:
    st.success("Attendance is excellent.")
elif attendance >= 75:
    st.info("Attendance is good.")
else:
    st.warning("Try to improve attendance.")

# Chart data
st.header("📈 Performance Factors")

chart_data = {
    "Study Hours": study_hours * 8,
    "Attendance": attendance,
    "Predicted Marks": predicted_marks
}

st.bar_chart(chart_data)

# Footer
st.markdown("---")
st.write("🎓 Student Performance Prediction App")
st.write("Created using Python and Streamlit")