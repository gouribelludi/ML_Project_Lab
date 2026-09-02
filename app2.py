import streamlit as st

# Page settings
st.set_page_config(
    page_title="Calories Calculator",
    page_icon="🍎",
    layout="wide"
)

# Title
st.title("🍎 Daily Calories Calculator")
st.write("Enter your details to estimate your daily calorie requirements.")

# Sidebar
st.sidebar.header("👤 Your Details")

name = st.sidebar.text_input("Enter your name")

age = st.sidebar.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=60.0
)

height = st.sidebar.number_input(
    "Height (cm)",
    min_value=100.0,
    max_value=220.0,
    value=170.0
)

activity = st.sidebar.selectbox(
    "Activity Level",
    [
        "Sedentary - Little exercise",
        "Lightly Active - 1 to 3 days/week",
        "Moderately Active - 3 to 5 days/week",
        "Very Active - 6 to 7 days/week",
        "Extremely Active - Hard exercise"
    ]
)

# Calculate BMI
height_m = height / 100
bmi = weight / (height_m ** 2)

# Calculate BMR
if gender == "Male":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

# Activity multiplier
if activity == "Sedentary - Little exercise":
    multiplier = 1.2
elif activity == "Lightly Active - 1 to 3 days/week":
    multiplier = 1.375
elif activity == "Moderately Active - 3 to 5 days/week":
    multiplier = 1.55
elif activity == "Very Active - 6 to 7 days/week":
    multiplier = 1.725
else:
    multiplier = 1.9

# Daily calorie calculation
daily_calories = bmr * multiplier

# Main section
st.header("📊 Your Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("BMI", f"{bmi:.1f}")

with col2:
    st.metric("BMR", f"{bmr:.0f} kcal")

with col3:
    st.metric("Daily Calories", f"{daily_calories:.0f} kcal")

# BMI result
st.header("⚖️ BMI Result")

if bmi < 18.5:
    st.info("Your BMI is in the underweight range.")
elif bmi < 25:
    st.success("Your BMI is in the normal range.")
elif bmi < 30:
    st.warning("Your BMI is in the overweight range.")
else:
    st.error("Your BMI is in the obesity range.")

# Calories information
st.header("🔥 Calorie Information")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Maintain Weight")
    st.write(f"Approximately **{daily_calories:.0f} kcal/day**")

with col2:
    st.subheader("Basic BMR")
    st.write(f"Approximately **{bmr:.0f} kcal/day**")

# Calorie chart
st.header("📈 Calorie Comparison")

chart_data = {
    "BMR": bmr,
    "Daily Calories": daily_calories
}

st.bar_chart(chart_data)

# Personalized message
st.header("💡 Summary")

if name:
    st.write(f"Hello **{name}**! 👋")
else:
    st.write("Hello! 👋")

st.write(
    f"Based on the information entered, your estimated daily "
    f"calorie requirement is **{daily_calories:.0f} kcal**."
)

st.write(
    "These calculations are estimates and should not be considered "
    "medical advice."
)

# Footer
st.markdown("---")
st.write("🍎 Calories Calculator | Built with Python & Streamlit")
