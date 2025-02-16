import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.ensemble import RandomForestRegressor

# Load datasets
ds1_path = "DS1.xlsx"  # Early Melt
ds2_path = "DS2.xlsx"  # Late Melt
ds3_path = "DS3.xlsx"  # Early Freeze
ds4_path = "DS4.xlsx"  # Late Freeze
countries_path = "Countries affected.xlsx"  # Region to Countries Mapping

# Read datasets
ds1 = pd.read_excel(ds1_path)
ds2 = pd.read_excel(ds2_path)
ds3 = pd.read_excel(ds3_path)
ds4 = pd.read_excel(ds4_path)
countries_df = pd.read_excel(countries_path)

# Standardize column names
ds1.columns = ds1.columns.str.strip().str.lower()
ds2.columns = ds2.columns.str.strip().str.lower()
ds3.columns = ds3.columns.str.strip().str.lower()
ds4.columns = ds4.columns.str.strip().str.lower()
countries_df.columns = countries_df.columns.str.strip().str.lower()

# Extract available years & regions
historical_years = ds1["yyyy"].astype(int).unique().tolist()
future_years = list(range(historical_years[-1] + 1, historical_years[-1] + 31))  # Predict 30 years ahead
all_years = historical_years + future_years  # Combine past & future years
available_regions = ds1.columns[1:].tolist()

# Streamlit UI
st.title("🌍 Polar Ice Melt & Freeze Prediction (Next 30 Years)")
st.sidebar.header("Select Inputs")
selected_year = st.sidebar.selectbox("📅 Select Year:", all_years)
selected_region = st.sidebar.selectbox("🌎 Select Arctic Region:", available_regions)
selected_region = selected_region.strip().lower()  # Normalize input

# Retrieve historical data
def get_data(dataset, year, region):
    if year in dataset["yyyy"].values:
        return dataset.loc[dataset["yyyy"] == year, region].values[0]
    return None  # Return None for future years

early_melt = get_data(ds1, selected_year, selected_region)
late_melt = get_data(ds2, selected_year, selected_region)
early_freeze = get_data(ds3, selected_year, selected_region)
late_freeze = get_data(ds4, selected_year, selected_region)

# **Optimized Prediction Using ARIMA & Random Forest**
@st.cache_data
def predict_future(data, forecast_horizon=30):
    """ Predicts future values using ARIMA & Random Forest (Faster than LSTM). """
    try:
        model = ARIMA(data, order=(2, 1, 2))  # ARIMA is much faster than SARIMA
        model_fit = model.fit()
        arima_forecast = model_fit.forecast(steps=forecast_horizon)

        rf_model = RandomForestRegressor(n_estimators=50, random_state=42)  # Faster execution
        historical_time = np.arange(len(data)).reshape(-1, 1)
        rf_model.fit(historical_time, data)
        
        future_time = np.arange(len(data), len(data) + forecast_horizon).reshape(-1, 1)
        rf_adjustments = rf_model.predict(future_time)

        # Return only the **first prediction value**
        return float(arima_forecast[0] + rf_adjustments[0])  
    except Exception as e:
        st.error(f"Prediction Error: {e}")
        return None  # Return None if prediction fails

# Generate Future Predictions
future_values = []
if selected_year in future_years:
    future_values = [
        predict_future(ds1[selected_region].values, 30),
        predict_future(ds2[selected_region].values, 30),
        predict_future(ds3[selected_region].values, 30),
        predict_future(ds4[selected_region].values, 30),
    ]
else:
    future_values = [early_melt, late_melt, early_freeze, late_freeze]

# **Ensure no None values in future_values and remove np.float64**
future_values = [float(val) if isinstance(val, np.generic) else val for val in future_values]
future_values = [val if val is not None else 0 for val in future_values]

# Debugging: Print values before plotting
st.write(f"Values for {selected_region} in {selected_year}: {', '.join(map(str, future_values))}")

# **Plot Historical & Future Data**
fig, ax = plt.subplots(figsize=(10, 6))
labels = ["Early Melt", "Late Melt", "Early Freeze", "Late Freeze"]
colors = ['blue', 'red', 'cyan', 'orange']

ax.bar(labels, future_values, color=colors)
ax.set_title(f"Ice Melt & Freeze for {selected_region} in {selected_year}")

ax.set_ylabel("Day of the Year (1-365)")
ax.set_ylim(0, 365)
st.pyplot(fig)

# **Fix 'Countries Affected' Section**
st.sidebar.subheader("🌍 Countries Affected:")
region_matched = countries_df.columns.str.lower().str.replace(" ", "") == selected_region.replace(" ", "")

# Extract the first matching column correctly
matched_column_name = countries_df.columns[region_matched].tolist()

if matched_column_name:
    affected_countries = countries_df[matched_column_name[0]].dropna().tolist()
    if affected_countries:
        st.sidebar.write(", ".join(affected_countries))
    else:
        st.sidebar.write("No affected countries listed.")
else:
    st.sidebar.write("Region not found in country data.")

st.markdown("**Note:** Predictions use ARIMA + Random Forest (Optimized for Speed).")
