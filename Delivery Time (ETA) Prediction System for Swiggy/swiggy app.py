import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load trained model
model = joblib.load("swiggy_eta_model.pkl")

st.title("🚴 Swiggy Delivery Time Prediction")

# ======================
# USER INPUTS (MAIN)
# ======================
distance = st.number_input("Distance (km)", min_value=0.1, max_value=50.0)
multiple = st.number_input("Multiple Deliveries", min_value=0, max_value=5)
order_hour = st.slider("Order Time Hour", 0, 23)
pickup_time = st.number_input("Pickup Time (minutes)", min_value=1, max_value=60)

festival = st.selectbox("Festival", ["No", "Yes"])
weekend = st.selectbox("Weekend", ["No", "Yes"])

# ======================
# DERIVED FEATURES
# ======================
festival_val = 1 if festival == "Yes" else 0
weekend_val = 1 if weekend == "Yes" else 0

is_peak_hour = 1 if (12 <= order_hour <= 14 or 19 <= order_hour <= 22) else 0
delivery_load = distance * multiple
high_demand_day = festival_val * weekend_val

# ======================
# BUILD FULL INPUT ROW
# ======================
input_df = pd.DataFrame([{
    # Core features
    "distance": distance,
    "multiple_deliveries": multiple,
    "order_time_hour": order_hour,
    "pickup_time_minutes": pickup_time,

    # Engineered
    "is_peak_hour": is_peak_hour,
    "delivery_load": delivery_load,
    "high_demand_day": high_demand_day,

    # Rider (defaults)
    "rider_id": "R000",
    "age": 30,
    "ratings": 4.5,
    "vehicle_condition": 1,
    "type_of_vehicle": "motorcycle",

    # Order (defaults)
    "type_of_order": "meal",
    "order_time_of_day": "evening",
    "order_day": datetime.now().day,
    "order_month": datetime.now().month,
    "order_day_of_week": datetime.now().strftime("%A"),
    "order_date": datetime.now().strftime("%Y-%m-%d"),

    # Location (defaults)
    "restaurant_latitude": 12.9716,
    "restaurant_longitude": 77.5946,
    "delivery_latitude": 12.9611,
    "delivery_longitude": 77.6387,

    # City & conditions
    "weather": "sunny",
    "traffic": "low",
    "city_type": "urban",
    "city_name": "bang",

    # Flags
    "festival": festival_val,
    "is_weekend": weekend_val,

    # IMPORTANT: DO NOT USE REAL TARGET — safe constant for schema
    "avg_speed_kmph": 20
}])

# ======================
# PREDICTION
# ======================
if st.button("Predict ETA"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")
