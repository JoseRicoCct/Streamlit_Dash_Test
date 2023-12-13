import streamlit as st
import pandas as pd
import numpy as np
import dash
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_colorscales
import cufflinks as cf
import plotly.express as px
import plotly.graph_objects as go
import json
import re

ufo_df = pd.read_csv('scrubbed.csv.zip', low_memory=False)

ufo_df.dropna(inplace=True)
ufo_df = ufo_df[ufo_df['country'] == 'us']

new_data = pd.read_excel('States.xlsx', engine='openpyxl')

def map_abb(state):
    for row in new_data.index:
        if state == new_data['ABB_lower'][row]:
            return new_data['ABB_upper'][row]
        
new_data['test'] = new_data['ABB_lower'].apply(map_abb)

ufo_df['state'] = ufo_df['state'].apply(map_abb)

ufo_df['datetime'] = ufo_df['datetime'].apply(lambda x: x[-10:-6])

ufo_df['datetime'] = ufo_df['datetime'].apply(lambda x: int(x))

ufo_df

ufo_df['datetime'].max()

def bin_decade(year):
    if year >= 1910 and year <= 1920:
        return "1910-1920"
    elif year >= 1920 and year <= 1930:
        return "1920-1930"
    elif year >= 1930 and year <= 1940:
        return "1930-1940"
    elif year >= 1940 and year <= 1950:
        return "1940-1950"
    elif year >= 1950 and year <= 1960:
        return "1950-1960"
    elif year >= 1960 and year <= 1970:
        return "1960-1970"
    elif year >= 1970 and year <= 1980:
        return "1970-1980"
    elif year >= 1980 and year <= 1990:
        return "1980-1990"
    elif year >= 1990 and year <= 2000:
        return "1990-2000" 
    elif year >= 2000 and year <= 2010:
        return "2000-2010"
    elif year >= 2010 and year <= 2014:
        return "2010-2014"
    
ufo_df['decade'] = ufo_df['datetime'].apply(bin_decade)

ufo_df = ufo_df[ufo_df['datetime'] >= 1950]

ufo_df['sighting'] = 1

ufo_df.to_csv('clean_df.csv')

ufo_df.groupby(['decade', 'state']).sum()['sighting']

ufo_df.to_csv('clean_df.csv')

ufo_df.info()

test = pd.read_csv('clean_df.csv', index_col=0)

another_test = test.groupby(['decade', 'state']).sum()

another_test.groupby('decade').sum()

test = test[test['state'] == 'TX']

new_test = test.groupby(['decade', 'state']).sum()

new_test['avg_encounter'] = new_test['duration (seconds)'] / new_test['sighting']

new_test.reset_index(inplace=True)

new_test

new_test['decade'].values

fig = px.bar(new_test, x='decade', y='sighting')
fig.show()
df = pd.read_csv("clean_df.csv", index_col=0)

colors = {
    'background': '#111111',
    'text': '#C5DB5F'
}

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1("UFO Sightings in the U.S.", style={'text-align': 'center', 'color': colors['text']}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(id="slct_decade",
                        options=[
                            {"label": "1940-1950", "value": "1940-1950"},
                            {"label": "1950-1960", "value": "1950-1960"},
                            {"label": "1960-1970", "value": "1960-1970"},
                            {"label": "1970-1980", "value": "1970-1980"},
                            {"label": "1990-2000", "value": "1990-2000"},
                            {"label": "2000-2010", "value": "2000-2010"},
                            {"label": "2010-2014", "value": "2010-2014"}],
                        multi=False,
                        value="2010-2014", 
                        style={'width': "50%"}
                        ),

            html.Div(id='output_container', style={'color': colors['text']}, children=[]),
            html.Br(),
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Dropdown(id="slct_chart",
                        options=[
                            {"label": "Average Encounter (seconds)", "value": "avg_encounter"},
                            {"label": "UFO Sightings", "value": "sighting"}],
                        multi=False,
                        value="sighting",
                        style={'width': "76"}
                        ),
            html.Br(),
        ], style={'width': '49%', 'text-align': 'center', 'display': 'inline-block'})
    ], style={
        'padding': '10px 5px'
    }),
    html.Div([
        dcc.Graph(id='my_ufo_map',
        hoverData={'points': [{'customdata': ['TX', 0]}]}
        )
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='my_bar_chart'),
    ], style={'display': 'inline-block', 'width': '49%'}),
])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_ufo_map', component_property='figure')],
    [Input(component_id='slct_decade', component_property='value')]
)
def update_map(slct_decade):

    container = "The decade chosen by user was: {}".format(slct_decade)
    
    dff = df.copy()
    dff = dff.groupby(['decade', 'state']).count()[['sighting']]
    dff.reset_index(inplace=True)
    dff = dff[dff["decade"] == slct_decade]

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state',
        scope="usa",
        color='sighting',
        hover_data=['state', 'sighting'],
        color_continuous_scale=px.colors.sequential.Blugrn,
        labels={'sighting': 'UFO sightings'},
        template='plotly_dark'
    )

    return container, fig
    
def create_chart(df_new, slct_chart, hoverData):

    df_new = df_new.groupby('decade').sum()
    df_new.reset_index(inplace=True)
    df_new['avg_encounter'] = df_new['duration (seconds)'] / df_new['sighting']
    x = df_new['decade']

    fig = px.bar(df_new, x='decade', y=slct_chart, title=hoverData['points'][0]['customdata'][0], template='plotly_dark')

    fig.update_layout(title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,})

    return fig 

@app.callback(
    Output(component_id='my_bar_chart', component_property='figure'),
    [Input(component_id='my_ufo_map', component_property='hoverData'),
    Input(component_id='slct_chart', component_property='value')]
)

def update_chart(hoverData, slct_chart):
    state_name = hoverData['points'][0]['customdata'][0]
    df_new = df.copy()
    df_new = df_new[df_new['state'] == state_name]
    print(state_name)
    return create_chart(df_new, slct_chart, hoverData)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
