import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Creating a df to plot the Sentiment Analysis prediction
review_data = {
    'Airline': ['Ryanair', 'Airline_Tweets', 'Ryanair', 'Airline_Tweets', 'Ryanair', 'Airline_Tweets'],
    'Sentiment': ['Bad', 'Bad', 'Good', 'Good', 'Neutral', 'Neutral'],
    'Score': [3, 3, 3, 0, 2, 0]
}

review_df = pd.DataFrame(review_data)

# Crosstab to get the data in the required format
review_crosstab = pd.crosstab(review_df['Sentiment'], review_df['Airline'], values=review_df['Score'], aggfunc='sum', margins=False)

# Your data for Supervised Learning
data_supervised = pd.DataFrame({
    'Model': ['Decision Tree Classifier', 'Random Forest', 'KNN', 'SVC', "GridSearchCV('C': 1000, 'gamma': 0.01})",
              "GridSearchCV('C': 1000, 'gamma': 0.001})"],
    'Accuracy (%)': [94.83, 93.10, 86.21, 69.23, 90.88, 0],  # Adjusted length
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
    'Feature_No': [2, 2, 2],
    'Accuracy (%)': [-88.85, 6.15, -70.44],
    'Features_No_Enriched': [16, 14, 17],
    'Accuracy_Enriched (%)': [98.67, 81.54, 89.59]
})

# Bar chart for GridSearchCV Feature Reduction
fig_feature_reduction = px.bar(
    data_feature_reduction,
    x='Country_Vehicle',  # Use 'Country_Vehicle' as the x-axis
    y=['Feature_No', 'Accuracy (%)', 'Features_No_Enriched', 'Accuracy_Enriched (%)'],
    barmode='group',
    title='Cross Validation and Feature Reduction'
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
    title='Unsupervised Learning - Silhouette Score'
)

# Explained variances for CAR
explained_variance_car = [0.77171509, 0.16514322, 0.02878059]

# Explained variances for CAR Enriched
explained_variance_car_enriched = [0.97747751, 0.0174295, 0.00246979]

# Explained variances for BUS
explained_variance_bus = [0.52207334, 0.2149303, 0.09974296]

# Explained variances for BUS Enriched
explained_variance_bus_enriched = [0.78418364, 0.14665355, 0.02593078]

# Explained variances for TRN
explained_variance_trn = [0.44371637, 0.33012741, 0.07419443]

# Explained variances for TRN Enriched
explained_variance_trn_enriched = [0.76860845, 0.16637195, 0.02241525]

# Layout of the app
st.title("Modern Transport Planning Ireland, LTD.")
st.markdown("Summary of the ML results. Please select an option from the dropdown menu to visualize the results.")

# Dropdown for selecting the figure
selected_value = st.selectbox("Select Figure", [
    'Supervised Learning',
    'Cross Validation & Feature Reduction',
    'Unsupervised Learning Silhouette Score',
    'Unsupervised Learning PCA Variance',
    'Sentiment Analysis'
])

# Placeholder for the selected figure
if selected_value == 'Supervised Learning':
    st.plotly_chart(fig_supervised)
elif selected_value == 'Sentiment Analysis':
    # Plotting histograms using plotly for Sentiment Analysis
    fig_sentiment = go.Figure()

    # Plot for Ryanair
    fig_sentiment.add_trace(go.Bar(x=review_crosstab.index, y=review_crosstab['Ryanair'],
                                   marker_color='blue', name='Ryanair'))

    # Plot for Airline_Tweets
    fig_sentiment.add_trace(go.Bar(x=review_crosstab.index, y=review_crosstab['Airline_Tweets'],
                                   marker_color='orange', name='Airline_Tweets'))

    fig_sentiment.update_layout(title='Sentiment Prediction Analysis',
                                xaxis=dict(title='Sentiment'),
                                yaxis=dict(title='Number of Predictions'),
                                barmode='group')  # Combine bars for each sentiment
    st.plotly_chart(fig_sentiment)

elif selected_value == 'Cross Validation & Feature Reduction':
    st.plotly_chart(fig_feature_reduction)
elif selected_value == 'Unsupervised Learning Silhouette Score':
    st.plotly_chart(fig_unsupervised)
elif selected_value == 'Unsupervised Learning PCA Variance':
    fig_pca_variance = go.Figure(
        data=[
            go.Bar(x=['1st Comp Car', '2nd Comp Car', '3rd Comp Car'], y=explained_variance_car, name='Component CAR', marker_color='blue'),
            go.Scatter(x=['1st Comp Car', '2nd Comp Car', '3rd Comp Car'], y=explained_variance_car,
                       mode='lines', marker=dict(color='red'), name='Cumulative Explained Variance CAR'),
            go.Bar(x=['1st Comp Car Enriched', '2nd Comp Car Enriched', '3rd Comp Car Enriched'], y=explained_variance_car_enriched, name='Component CAR Enriched', marker_color='green'),
            go.Scatter(x=['1st Comp Car Enriched', '2nd Comp Car Enriched', '3rd Comp Car Enriched'], y=explained_variance_car_enriched,
                       mode='lines', marker=dict(color='orange'), name='Cumulative Explained Variance CAR Enriched'),
            go.Bar(x=['1st Comp Bus', '2nd Comp Bus', '3rd Comp Bus'], y=explained_variance_bus, name='Component BUS', marker_color='purple'),
            go.Scatter(x=['1st Comp Bus', '2nd Comp Bus', '3rd Comp Bus'], y=explained_variance_bus,
                       mode='lines', marker=dict(color='brown'), name='Cumulative Explained Variance BUS'),
            go.Bar(x=['1st Comp Bus Enriched', '2nd Comp Bus Enriched', '3rd Comp Bus Enriched'], y=explained_variance_bus_enriched, name='Component BUS Enriched', marker_color='gray'),
            go.Scatter(x=['1st Comp Bus Enriched', '2nd Comp Bus Enriched', '3rd Comp Bus Enriched'], y=explained_variance_bus_enriched,
                       mode='lines', marker=dict(color='pink'), name='Cumulative Explained Variance BUS Enriched'),
            go.Bar(x=['1st Comp TRN', '2nd Comp TRN', '3rd Comp TRN'], y=explained_variance_trn, name='Component TRN', marker_color='cyan'),
            go.Scatter(x=['1st Comp TRN', '2nd Comp TRN', '3rd Comp TRN'], y=explained_variance_trn,
                       mode='lines', marker=dict(color='black'), name='Cumulative Explained Variance TRN'),
            go.Bar(x=['1st Comp TRN Enriched', '2nd Comp TRN Enriched', '3rd Comp TRN Enriched'], y=explained_variance_trn_enriched, name='Component TRN Enriched', marker_color='yellow'),
            go.Scatter(x=['1st Comp TRN Enriched', '2nd Comp TRN Enriched', '3rd Comp TRN Enriched'], y=explained_variance_trn_enriched,
                       mode='lines', marker=dict(color='magenta'), name='Cumulative Explained Variance TRN Enriched'),
        ],
        layout=dict(
            title='Unsupervised Learning - Principal Components Variance',
            xaxis=dict(title='Components'),
            yaxis=dict(title='Explained Variance'),
            legend=dict(x=0, y=1),
            margin=dict(l=10, r=10, t=40, b=10),
            showlegend=False  # Turn off the legend
        )
    )
    st.plotly_chart(fig_pca_variance)

# Additional tags
st.markdown("Developed with ❤️ by Student sba23021.")
