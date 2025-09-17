import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Nifty Stocks Analysis", layout="wide")

# Load the dataset
df = pd.read_csv("../DataSets/Nifty_Stocks.csv")

# Show title
st.title("📊 Nifty Stocks Category-wise Price Range Visualization")

# Show unique categories
categories = df['Category'].unique()
selected_category = st.selectbox("Select Stock Category:", categories)

# Filter dataframe
filtered_df = df[df['Category'] == selected_category]

# Show filtered data (optional)
st.dataframe(filtered_df)

# Plot the barplot
st.subheader(f"Price Range for Category: {selected_category}")
fig, ax = plt.subplots()
sb.barplot(x='Category', y='Price_Range', data=filtered_df, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
