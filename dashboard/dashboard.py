# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# LOAD DATA
@st.cache_resource
def load_data():
    data = pd.read_csv("dashboard/hour.csv")
    return data


data = load_data()

# TITLE DASHBOARD
# Set page title
st.title("Bike Share Dashboard")

# SIDEBAR
st.sidebar.title("Created By:")
st.sidebar.markdown("**• Nama: Labib Yusuf Aditama**")
st.sidebar.markdown("**• Email: labibyusufaditama@gmail.com**")

st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://drive.google.com/drive/folders/1Uk2CDwEwimKPy395dDDqfA8rUc1WCTvI?usp=sharing)")

# VISUALIZATION
# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Number of bicycle shares by season
    # st.subheader("Number of bicycle shares by season")

    # Mapping dari angka ke label musim
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label",
                              y="cnt", title="Number of bicycle shares by season")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Number of Bicycle Rentals Based on Weather Situations
    # st.subheader("Number of Bicycle Rentals Based on Weather Situations")

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Number of Bicycle Rentals Based on Weather Situations")
    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True,height=400, width=800)


# Hourly bike share count
# st.subheader("Hourly Bike Share Count")
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True,
                height=400, width=600)

# Humidity vs. Bike Share Count
# st.subheader("Humidity vs. Bike Share Count")
fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Bike Share Count")
st.plotly_chart(fig_humidity_chart)

# Wind Speed vs. Bike Share Count
# st.subheader("Wind Speed vs. Bike Share Count")
fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count")
st.plotly_chart(fig_wind_speed_chart)

# Temperature vs. Bike Share Count
# st.subheader("Temperature vs. Bike Share Count")
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)