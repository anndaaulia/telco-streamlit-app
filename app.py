import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("WA_FnUseC_TelcoCustomerChurn.csv")

# Title
st.title("📊 Telco Customer Churn Dashboard")

# Sidebar konfigurasi
st.sidebar.header("Pengaturan Visualisasi")

# Tampilkan info dasar
st.write("### Preview Data")
st.dataframe(df.head())

# Pilih kolom numerik
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Dropdown pilihan kolom untuk visualisasi
x_axis = st.sidebar.selectbox("Pilih kolom untuk sumbu X:", numeric_cols)
y_axis = st.sidebar.selectbox("Pilih kolom untuk sumbu Y:", numeric_cols)
hue_col = st.sidebar.selectbox("Kelompokkan berdasarkan (opsional):", ['None'] + categorical_cols)

# Filter churn
churn_filter = st.sidebar.multiselect("Filter Churn:", df["Churn"].unique(), default=df["Churn"].unique())
filtered_df = df[df["Churn"].isin(churn_filter)]

# Plot scatter
st.write("### Scatter Plot")
fig, ax = plt.subplots()
if hue_col != 'None':
    sns.scatterplot(data=filtered_df, x=x_axis, y=y_axis, hue=hue_col, ax=ax)
else:
    sns.scatterplot(data=filtered_df, x=x_axis, y=y_axis, ax=ax)
st.pyplot(fig)

# Slider untuk sample
sample_size = st.slider("Tampilkan berapa banyak data pertama:", 1, len(filtered_df), 5)
st.write(f"Menampilkan {sample_size} data pertama:")
st.dataframe(filtered_df.head(sample_size))
