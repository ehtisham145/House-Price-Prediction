import streamlit as st
import pandas as pd
#import joblib

# Load your trained model
#model = joblib.load("model.pkl")

# Page configuration
st.set_page_config(page_title="House Prediction Model", page_icon="🏠", layout="wide")

# HEADER
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🏠 House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #555;'>Developed by Ehtisham</h4>", unsafe_allow_html=True)
st.markdown("---")

# CHAT-GPT STYLE SIDEBAR
st.sidebar.markdown("## 📝 Input House Details")

# Grouped sections (like ChatGPT menus)
with st.sidebar.expander("Basic Info", expanded=True):
    overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    gr_liv_area = st.number_input("Ground Living Area (sq ft)", 300, 10000, 1500)

with st.sidebar.expander("Garage & Lot", expanded=False):
    garage_cars = st.slider("Garage Cars", 0, 5, 1)
    lot_area = st.number_input("Lot Area (sq ft)", 500, 20000, 5000)

with st.sidebar.expander("House Year & Neighborhood", expanded=False):
    year_built = st.number_input("Year Built", 1800, 2025, 2000)
    neighborhood = st.selectbox("Neighborhood", ["NAmes", "CollgCr", "OldTown", "Edwards", "Somerst"])

# Predict button at the bottom
if st.sidebar.button("Predict House Price"):
    input_data = pd.DataFrame({
        'OverallQual': [overall_qual],
        'GrLivArea': [gr_liv_area],
        'GarageCars': [garage_cars],
        'LotArea': [lot_area],
        'YearBuilt': [year_built],
        'Neighborhood': [neighborhood]
    })

    # Preprocess categorical variables as needed
    #prediction = model.predict(input_data)[0]

    #st.success(f"🏡 Estimated House Price: ${prediction:,.2f}")

# MAIN CONTENT AREA
st.markdown("## Model Overview")
st.write("""
This **House Price Prediction Model** uses the most important features of a house to predict its selling price.  
Use the sidebar to input your house details and get instant predictions.
""")

# FOOTER
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>© 2025 House Price Prediction App | Developed by Ehtisham</p>", unsafe_allow_html=True)
