import pandas as pd 
import dash 
import seaborn as sns 
import plotly.express as px
from dash import html
import dash_core_components as dcc
import plotly.graph_objects as go

# importing data 
gap= px.data.gapminder()

app=dash.Dash()

# app.layout= html.H1(children= 'My First Dashboard', style={'color':'red', 'text-align':'center'})

app.layout= html.Div([
        html.Div(children= [html.H1(children= 'My First Dashboard', style={'color':'red', 'text-align':'center'})], style= {'border': '1px black solid', 'float':'left', 'width':'100%', 'height':'50px'}),

        html.Div(children= [
            dcc.Graph(id='scatter-plot', 
                        figure= {'data':[go.Scatter(x= gap['pop'],
                                                     y= gap['gdpPercap'],
                                                     mode='markers')],
                        'layout': go.Layout(title='Scatter plot')})],
                        style= {'border': '1px black solid', 'float':'left', 'width':'49.5%', 'height':'350px'}),

        html.Div(style= {'border': '1px black solid', 'float':'left', 'width':'49.5%', 'height':'350px'}),
        
])

if __name__== '__main__':
    app.run(debug=True)