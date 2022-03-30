import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#TITLE
st.title('Dashboard Kelompok 5')

#HEADER
st.header("Ini adalah Data Covid-19 di Indonesia")

#WRITE
st.write("Membuat Tabel dari Data")
data = pd.read_csv('Covid_19_Indonesiaclean.csv')

# BUTTON
if st.button("Lihat Dataframe"):
    st.write(data)

# CHECKBOX
info = data.nunique()
if st.checkbox("Lihat Jumlah Elemen Unik"):
    st.write(info)

# SELECT
Location = st.selectbox("Select Dataframe of Location", data.Location.unique())

# RADIO BUTTON
Island = st.radio("Select Dataframe of Island", data.Island.unique())

st.write(data[
    (data.Location == Location) & (data.Island == Island)])   

# options = st.multiselect('Jumlah Kasus', ['Positif', 'Meninggal', 'Sembuh'], ['Positif', 'Meninggal', 'Sembuh'])

# #displaying the selected options
# if Positif:
#     st.write(data.Total_Cases)
# elif Meninggal:
#     st.write(data.Total_Deaths)
# elif Sembuh:
#     st.write(data.Total_Recovered)
# elif Positif and Meninggal:
#     st.write(data.Total_Cases, data.Total_Deaths)
# elif Positif and Sembuh:
#     st.write(data.Total_Cases, data.Total_Recovered)
# elif Sembuh and Meninggal:
#     st.write(data.Total_Recovered, data.Total_Deaths)


# # CHECKBOX
# st.write("Lihat Jumlah Kasus")
# positif     = st.checkbox("Kasus Positif")
# meninggal   = st.checkbox("Kasus Meninggal")
# sembuh      = st.checkbox("Kasus Sembuh")  
# if positif:
#     st.write(data.Total_Cases)
# elif meninggal:
#     st.write(data.Total_Deaths)
# elif sembuh:
#     st.write(data.Total_Recovered)
# elif positif and meninggal:
#     st.write(data[['Total_Cases', 'Total_Deaths']])
# elif positif and sembuh:
#     st.write(data[['Total_Cases', 'Total_Recovered']])
# else:
#     st.write(data[['Total_Deaths', 'Total_Recovered']])

# # SLIDER
# Age = st.slider('Select The Age', 0, 100)

# st.write(data[
#     (data.Location == Location) & (data.Island == Island) ])

# Membuat PLOT PAKE MATPLOTLIB
st.markdown('Plot Normalisasi')
arr = np.random.normal(1, 1, 100)
st.write(arr)
fig, ax = plt.subplots()
plt.hist(arr, bins=20)
st.pyplot(fig)

# #VISUALISASI DATASET
# # df_airplane_col = st.selectbox("Select column", ['Inflight wifi service', 'Departure/Arrival time convenient', 
# #     'Ease of Online booking', 'Food and drink'])
# # fig = px.line(data,  x='Flight Distance', y=df_airplane_col)
# # st.plotly_chart(fig)

# # df_can = px.data.gapminder().query("country == 'Canada'")
# # st.write(df_can)
# # df_can_col = st.selectbox("Select column", ['lifeExp', 'gdpPercap', 'pop'])

# # fig = px.line(df_can, x='year', y=df_can_col)

# # st.plotly_chart(fig)

# st.header("How many accidents occur during a given time of day?")
# hour = st.slider("Hour to look at", 0, 23)
# original_data = data
# data = data[data['date / time'].dt.hour == hour]

# st.markdown("Vehicle collisions between % i:00 and % i:00" % (hour, (hour + 1) % 24))
# midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))
  
# st.write(pdk.Deck(
#     map_style ="mapbox://styles / mapbox / light-v9",
#     initial_view_state ={
#         "latitude": midpoint[0],
#         "longitude": midpoint[1],
#         "zoom": 11,
#         "pitch": 50,
#     },
#     layers =[
#         pdk.Layer(
#         "HexagonLayer",
#         data = data[['date / time', 'latitude', 'longitude']],