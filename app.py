import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Fill missing values
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
df['odometer'] = df.groupby(['model_year', 'model'])['odometer'].transform(lambda x: x.fillna(x.median()))

# Remove outliers
df = df[(df['price'] >= 500) & (df['price'] <= 50000)]  # Example price range
df = df[(df['model_year'] >= 1990) & (df['model_year'] <= 2022)]  # Example model year range

# Title of the web app
st.title('Car Sales Advertisement Analysis')

# Display the dataset
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(df)

# Header for histograms
st.header('Distribution of Car Prices')
fig_price = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig_price)

st.header('Distribution of Car Model Years')
fig_year = px.histogram(df, x='model_year', title='Distribution of Car Model Years')
st.plotly_chart(fig_year)

st.header('Distribution of Odometer Readings')
fig_odometer = px.histogram(df, x='odometer', title='Distribution of Odometer Readings')
st.plotly_chart(fig_odometer)

# Header for scatter plots
st.header('Scatter Plots')

st.subheader('Price vs Odometer')
fig_price_odometer = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_price_odometer)

st.subheader('Price vs Model Year')
fig_price_year = px.scatter(df, x='model_year', y='price', title='Price vs Model Year')
st.plotly_chart(fig_price_year)



