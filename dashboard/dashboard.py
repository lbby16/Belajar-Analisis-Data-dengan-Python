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
df_bsd_day = pd.read_csv("data/day.csv")
df_bsd_hour = pd.read_csv("data/hour.csv")
# df_bsd_day
df_bsd_day["dteday"] = pd.to_datetime(df_bsd_day["dteday"])
# df_bsd_hour
df_bsd_hour["dteday"] = pd.to_datetime(df_bsd_hour["dteday"])



st.subheader("Pertanyaan 1")
# Filter tahun 2011 dan musim dingin (season 4)
filtered_data = df_bsd_day[(df_bsd_day["yr"] == 0) & (df_bsd_day["season"] == 4)]

# Filter tahun 2011 dan musim dingin (season 4)
# Hitung jumlah total sewa sepeda (cnt)
total_sewa_sepeda = filtered_data["cnt"].sum()

# Visualisasi dengan Plotly Express
fig = px.bar(filtered_data, x='dteday', y='cnt', title='Jumlah total sewa sepeda untuk tahun 2011 selama musim dingin (musim 4)')
fig.update_xaxes(title="Tanggal")
fig.update_yaxes(title="Jumlah Sewa Sepeda")

# Tampilkan plot menggunakan Streamlit
st.plotly_chart(fig, use_container_width=True)



st.subheader("Pertanyaan 2")
# Filter tahun 2011, musim dingin (season 4), dan hari libur (holiday = 0)
filtered_data = df_bsd_day[(df_bsd_day["yr"] == 0) & 
                            (df_bsd_day["season"] == 4) & 
                            (df_bsd_day["holiday"] == 1)]

# Hitung jumlah total sepeda sewaan
total_sepeda_sewaan = filtered_data["cnt"].sum()


# Visualisasi dengan Plotly Express
fig = px.bar(filtered_data, x='dteday', y='cnt',
             title='Jumlah total sepeda sewaan per hari libur pada musim dingin tahun 2011')
fig.update_xaxes(title="Tanggal")
fig.update_yaxes(title="Jumlah Sewa Sepeda")

# Tampilkan plot menggunakan Streamlit
st.plotly_chart(fig, use_container_width=True)


st.subheader("Pertanyaan 3")
# Filter pengguna casual (casual) pada hari kerja (workingday = 1)
filtered_data = df_bsd_day[(df_bsd_day["workingday"] == 1) & (df_bsd_day["casual"] > 0)]

# Visualisasikan jumlah sewa sepeda casual pada hari kerja
fig = px.bar(filtered_data, x="weekday", y="casual", title="Jumlah Sewa Sepeda Casual pada Hari Kerja")
fig.update_xaxes(title="Hari Kerja")
fig.update_yaxes(title="Jumlah Sewa Sepeda Casual")

# Tampilkan plot menggunakan Streamlit
st.plotly_chart(fig, use_container_width=True)


st.subheader("Pertanyaan 4")
# Filter musim gugur (season 3)
filtered_data = df_bsd_day[df_bsd_day["season"] == 3]

# Buat plot dengan Plotly untuk menganalisis pengaruh cuaca terhadap jumlah sewa sepeda
fig = px.bar(filtered_data, x="weathersit", y="cnt", title="Pengaruh Cuaca terhadap Jumlah Sewa Sepeda (Musim Gugur)")
fig.update_xaxes(title="Cuaca (weathersit)")
fig.update_yaxes(title="Jumlah Sewa Sepeda (cnt)")

# Tampilkan plot menggunakan Streamlit
st.plotly_chart(fig, use_container_width=True)



st.subheader("Pertanyaan 5")
# Filter data tahun 2011 (yr = 0), Hari Natal (holiday = 0), dan musim dingin (season 4)
filtered_data = df_bsd_hour[(df_bsd_hour["yr"] == 0) & 
                             (df_bsd_hour["holiday"] == 0) & 
                             (df_bsd_hour["season"] == 4)]

# Hitung distribusi per jam sewa sepeda (cnt)
distribusi_per_jam = filtered_data.groupby("hr")["cnt"].sum()

# Visualisasi dengan Plotly Express
fig = px.bar(x=distribusi_per_jam.index, y=distribusi_per_jam.values,
             labels={'x': 'Jam', 'y': 'Jumlah Sewa Sepeda'},
             title="Distribusi per Jam Sewa Sepeda pada Hari Natal tahun 2011 (Musim Dingin)")
fig.update_xaxes(title="Jam")
fig.update_yaxes(title="Jumlah Sewa Sepeda")

# Tampilkan plot menggunakan Streamlit
st.plotly_chart(fig, use_container_width=True)