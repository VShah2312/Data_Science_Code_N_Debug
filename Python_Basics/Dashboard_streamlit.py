
# ---- Dashboard 1------

# import streamlit as st
# import plotly.express as px
# import seaborn as sns
# import pandas as pd

# # Load dataset
# df = sns.load_dataset("tips")

# # Create interactive Plotly plot
# fig = px.scatter(df, x="total_bill", y="tip", color="sex")

# # Show in Streamlit
# st.plotly_chart(fig)

# # streamlit run Dashboard_streamlit.py to run streamlit.


# ---- Dashboard 2------


import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = sns.load_dataset("tips")

# --- Header ---
st.title("Tips Dashboard")
st.markdown("Analyze tip trends based on various features in the dataset.")

# --- Filter Sidebar ---
st.sidebar.header("Filter")
selected_day = st.sidebar.selectbox("Select Day", df["day"].unique())
filtered_df = df[df["day"] == selected_day]

# --- Seaborn Chart 1 ---
st.subheader("1. Total Bill vs Tip (Seaborn)")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x="total_bill", y="tip", hue="sex", ax=ax1)
st.pyplot(fig1)

# --- Plotly Chart 2 ---
st.subheader("2. Total Bill Distribution (Plotly)")
fig2 = px.histogram(filtered_df, x="total_bill", color="sex", barmode="overlay")
st.plotly_chart(fig2)

# --- Columns Layout ---
st.subheader("3. Tips by Smoker Status")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Boxplot")
    fig3, ax2 = plt.subplots()
    sns.boxplot(data=filtered_df, x="smoker", y="tip", ax=ax2)
    st.pyplot(fig3)

with col2:
    st.markdown("### Average Tip (Bar Chart)")
    avg_tip = filtered_df.groupby("smoker")["tip"].mean().reset_index()
    fig4 = px.bar(avg_tip, x="smoker", y="tip", color="smoker", title="Avg Tip by Smoker")
    st.plotly_chart(fig4)
