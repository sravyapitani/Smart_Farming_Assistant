# app.py — Smart Farming Assistant 🌾

# Import Required Libraries
import streamlit as st
import pickle
import pandas as pd

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Smart Farming Assistant",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------------
# Custom CSS Styling
# -----------------------------------
st.markdown("""
<style>

/* Background Image */
.stApp {
    background-image: url('https://images.unsplash.com/photo-1464226184884-fa280b87c399');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main Title */
.title {
    text-align: center;
    color: #66ff99;
    font-size: 55px;
    font-weight: bold;
    margin-bottom: 10px;
    text-shadow: 2px 2px 10px black;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #d4ffd4;
    font-size: 24px;
    margin-bottom: 35px;
    text-shadow: 1px 1px 5px black;
}

/* Input Labels */
label {
    color: black !important;
    font-weight: bold;
    font-size: 16px !important;
}

/* Button Styling */
.stButton > button {
    background: linear-gradient(90deg, #2e7d32, #43a047);
    color: white;
    border-radius: 12px;
    height: 55px;
    width: 100%;
    font-size: 20px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1b5e20, #2e7d32);
    color: white;
}

/* Result Box */
.result-box {
    background: rgba(0,0,0,0.80);
    padding: 30px;
    border-radius: 20px;
    border: 2px solid #66ff99;
    margin-top: 30px;
    box-shadow: 0px 0px 20px rgba(0,255,100,0.5);
}

/* Crop Text */
.crop {
    color: #66ff99;
    font-size: 34px;
    font-weight: bold;
}

/* Fertilizer Text */
.fertilizer {
    color: #4da6ff;
    font-size: 28px;
    font-weight: bold;
}

/* Tip Text */
.tip {
    color: #ffcc66;
    font-size: 22px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.85);
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("🌱 Smart Farming Assistant")

st.sidebar.info(
    "Enter soil and climate details to get crop and fertilizer recommendations."
)

st.sidebar.success("✅ AI Powered Farming Support")

# -----------------------------------
# Main Heading
# -----------------------------------
st.markdown(
    '<div class="title">🌾 Smart Farming Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Crop Prediction • Fertilizer Recommendation • Farming Tips</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# Load Trained Model
# -----------------------------------
model = pickle.load(open("crop_model.pkl", "rb"))

# -----------------------------------
# Input Section
# -----------------------------------
st.subheader("🧪 Enter Soil and Climate Details")

col1, col2 = st.columns(2)

with col1:

    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        step=1.0,
        key="nitrogen"
    )

    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        step=1.0,
        key="phosphorus"
    )

    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        step=1.0,
        key="potassium"
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        key="temperature"
    )

with col2:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        key="humidity"
    )

    ph = st.number_input(
        "pH Value",
        min_value=0.0,
        key="phvalue"
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        key="rainfall"
    )

# -----------------------------------
# Prediction Button
# -----------------------------------
if st.button("🌱 Predict Crop"):

    # Create DataFrame
    input_data = pd.DataFrame({
        "N": [N],
        "P": [P],
        "K": [K],
        "temperature": [temperature],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rainfall]
    })

    # Predict Crop
    prediction = model.predict(input_data)

    # Get Crop Name
    crop = prediction[0]

    # -----------------------------------
    # Fertilizer Recommendation
    # -----------------------------------
    if N < 50:
        fertilizer = "Urea"

    elif P < 40:
        fertilizer = "DAP"

    elif K < 40:
        fertilizer = "MOP"

    else:
        fertilizer = "Organic Compost"

    # -----------------------------------
    # Farming Tips Dictionary
    # -----------------------------------
    tips = {
        "rice": "Maintain proper irrigation and avoid water stagnation.",
        "wheat": "Use well-drained soil and moderate irrigation.",
        "maize": "Ensure sufficient sunlight and balanced nutrients.",
        "cotton": "Monitor pests regularly and maintain soil fertility.",
        "sugarcane": "Requires high water supply and nutrient-rich soil.",
        "coffee": "Grow in shaded areas with organic-rich soil.",
        "pigeonpeas": "Monitor soil health regularly for better yield.",
        "banana": "Use potassium-rich fertilizers for healthy growth.",
        "mango": "Avoid excess watering and ensure proper sunlight.",
        "coconut": "Maintain proper drainage and adequate irrigation."
    }

    # Get Farming Tip
    crop_tip = tips.get(
        crop.lower(),
        "Monitor soil health regularly for better yield."
    )

    # -----------------------------------
    # Result HTML
    # -----------------------------------
    result_html = f"""
<div class="result-box">

<div class="crop">
🌾 Recommended Crop: {crop}
</div>

<br>

<div class="fertilizer">
🧪 Recommended Fertilizer: {fertilizer}
</div>

<br>

<div class="tip">
💡 Farming Tip: {crop_tip}
</div>

</div>
"""

    # Display Result
    st.markdown(result_html, unsafe_allow_html=True)

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")

st.markdown(
    "<center><b>Developed using Streamlit 🚀</b></center>",
    unsafe_allow_html=True
)