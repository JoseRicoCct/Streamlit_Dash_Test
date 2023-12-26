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

# Your data for GridSearchCV Feature Reduction
data_feature_reduction = pd.DataFrame({
    'Country_Vehicle': ['IE_CAR', 'IE_BUS', 'IE_TRN'],
    'Number_of_Features': [4, 2, 2],
    'Number_of_Features_Enriched': [16, 14, 17],
    'Accuracy (%)': [-90.92, 6.15, -70.44],
    'Accuracy_Enriched (%)': [98.67, 81.54, 89.59]
})

# Bar chart for GridSearchCV Feature Reduction
fig_feature_reduction = px.bar(
    data_feature_reduction,
    x='Country_Vehicle',  # Use 'Country_Vehicle' as the x-axis
    y=['Number_of_Features', 'Number_of_Features_Enriched', 'Accuracy (%)', 'Accuracy_Enriched (%)'],
    barmode='group',
     title='GridSearchCV Feature Reduction'
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

# Your DataFrame
data_pca = pd.DataFrame({
    'Vehicle': ['CAR', 'BUS', 'TRN'],
    'PCA': [
        [0.77171509, 0.16514322, 0.02878059],
        [0.52207334, 0.2149303, 0.09974296],
        [0.44371637, 0.33012741, 0.07419443]
    ],
    'PCA Enriched': [
        [0.97747751, 0.0174295, 0.00246979],
        [0.97557712, 0.01888167, 0.00272318],
        [0.76860845, 0.16637195, 0.02241525]
    ]
})

# Reshape the DataFrame for the table
data_pca_long = pd.melt(data_pca, id_vars=['Vehicle'], var_name='Method', value_name='Values')

# Convert the 'Values' column to strings for display in DataTable
data_pca_long['Values'] = data_pca_long['Values'].apply(lambda x: ', '.join(map(str, x)))

# Streamlit app
st.title("PCA and PCA Enriched Values")

# Display the DataTable
st.dataframe(data_pca_long)

# Display the plots
st.plotly_chart(fig_supervised)
st.plotly_chart(fig_feature_reduction)
st.plotly_chart(fig_unsupervised)
