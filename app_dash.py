import streamlit as st
import plotly.express as px

# Load Data
df = px.data.tips()

# Streamlit App
st.title("Streamlit Demo")

# Dropdown for selecting colorscale
colorscale = st.selectbox("Select Colorscale", px.colors.named_colorscales())

# Scatter plot
fig = px.scatter(
    df, x="total_bill", y="tip", color="size",
    color_continuous_scale=colorscale,
    render_mode="webgl", title="Tips"
)

# Display the plot using Streamlit
st.plotly_chart(fig)
