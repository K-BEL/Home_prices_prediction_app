import streamlit as st
from pydantic import BaseModel
import util

# Load artifacts (e.g., trained model, state/type data)
util.load_saved_artifacts()

# Title and description
st.title("🏠 Home Price Prediction App")
st.markdown("""
This app predicts home prices based on property details.
Please provide the required inputs below.
""")

# Sidebar for navigation
menu = st.sidebar.selectbox(
    "Navigate",
    ["Home", "States & Types", "Predict Price"]
)

# Home Page
if menu == "Home":
    st.subheader("Welcome to the Home Price Prediction App!")
    st.write("""
    - Navigate to **States & Types** to explore state names and property types.
    - Navigate to **Predict Price** to estimate a property's price.
    """)

# States and Types Page
elif menu == "States & Types":
    st.subheader("States & Property Types")
    col1, col2 = st.columns(2)

    with col1:
        st.write("### States")
        state_names = util.get_State_names()
        for state in state_names:
            st.write(f"- {state}")

    with col2:
        st.write("### Property Types")
        type_names = util.get_Type_names()
        for t_type in type_names:
            st.write(f"- {t_type}")

# Prediction Page
elif menu == "Predict Price":
    st.subheader("Predict Home Price")

    # Input Form
    with st.form("prediction_form"):
        st.write("### Enter Property Details")
        Lot = st.number_input("Lot size (in square meters)", min_value=0.0, value=100.0, step=0.1)
        State = st.selectbox("Select State", util.get_State_names())
        Type = st.selectbox("Select Property Type", util.get_Type_names())
        Bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=1, step=1)
        Floors = st.number_input("Number of Floors", min_value=0, value=1, step=1)
        Garages = st.number_input("Number of Garages", min_value=0, value=0, step=1)
        rooms = st.number_input("Number of Rooms", min_value=1, value=3, step=1)
        
        # Submit button
        submitted = st.form_submit_button("Predict")

    if submitted:
        # Call prediction function
        try:
            estimated_price = util.get_estimated_price(State, Type, Lot, Bathrooms, Floors, Garages, rooms)
            st.success(f"Estimated Price: ${estimated_price:,.2f}")
        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.sidebar.info("Developed with ❤️ using Streamlit")
