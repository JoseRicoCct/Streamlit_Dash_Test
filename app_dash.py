import pandas as pd
import streamlit as st
import plotly.express as px

# Your data for Supervised Learning
data_supervised = pd.DataFrame({
    'Model': ['Decision Tree Classifier', 'Random Forest', 'KNN','SVC' ,"GridSearchCV('C': 1000, 'gamma': 0.01})", "GridSearchCV('C': 1000, 'gamma': 0.001})"],
    'Accuracy (%)': [94.83, 93.10, 86.21,69.23 ,90.88, 0],  # Adjusted length
    'Accuracy_Enriched (%)': [87.44, 91.77, 87.44, 87.01, 0, 91.04]  # Adjusted length
})

# Bar chart for Supervised Learning
fig_supervised = px.bar(
    data_supervised,
    x='Model',
    y=['Accuracy (%)', 'Accuracy_Enriched (%)'],
    barmode='group',
    title='Supervised Learning'
)

# Your data for Feature Reduction and GridSearchCV
data_feature_reduction = pd.DataFrame({
    'Country_Vehicle': ['IE_CAR', 'IE_BUS', 'IE_TRN'],
    'Number_of_Features': [4, 2, 2],
    'Number_of_Features_Enriched': [16, 14, 17],
    'Accuracy (%)': [-90.92, 6.15, -70.44],
    'Accuracy_Enriched (%)': [98.67, 81.54, 89.59]
})

# Bar chart for Feature Reduction and GridSearchCV
fig_feature_reduction = px.bar(
    data_feature_reduction,
    x='Country_Vehicle',  # Use 'Country_Vehicle' as the x-axis
    y=['Number_of_Features', 'Number_of_Features_Enriched', 'Accuracy (%)', 'Accuracy_Enriched (%)'],
    barmode='group',
    title='Feature Reduction and GridSearchCV'
)

# Your data for Unsupervised Learning
data_unsupervised = pd.DataFrame({
    'Vehicle': ['CAR', 'BUS', 'TRN'],
    'Silhouetter_Score': [0.49, 0.41, 0.39],
    'Silhouetter_Score_Enriched': [0.67, 0.67, 0.44]
})

# Bar chart for Unsupervised Learning
fig_unsupervised = px.bar(
    data_unsupervised,
    x='Vehicle',
    y=['Silhouetter_Score', 'Silhouetter_Score_Enriched'],
    barmode='group',
    title='Unsupervised Learning'
)

# Dropdown options
options = ['Supervised Learning', 'Unsupervised Learning', 'Feature Reduction and GridSearchCV']

# Streamlit app
st.title("Graph Selector")

# Dropdown for selecting the graph
selected_graph = st.selectbox("Select Graph", options)

# Display the selected graph
if selected_graph == 'Supervised Learning':
    st.plotly_chart(fig_supervised)
elif selected_graph == 'Unsupervised Learning':
    st.plotly_chart(fig_unsupervised)
elif selected_graph == 'Feature Reduction and GridSearchCV':
    st.plotly_chart(fig_feature_reduction)
