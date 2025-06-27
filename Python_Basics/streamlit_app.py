import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px

# Load dataset
df = pd.read_csv("/Users/vrunda/Library/CloudStorage/GoogleDrive-shahvrunda231296@gmail.com/.shortcut-targets-by-id/1If4Xq7JBYnZ3iRTOYUU8DDWlZlr7e5rJ/Dataset, Assignments, Interview Prep - D1/dataset/india.csv")

# List of States
list_of_states = list(df.State.unique())
list_of_states.insert(0, 'Overall India')

# Sidebar
st.sidebar.title('India state wise Viz')
selected_state = st.sidebar.selectbox("Select State", list_of_states)
primary= st.sidebar.selectbox('Select Primary parameter', sorted(df.columns[5:]))
secondary= st.sidebar.selectbox('Select Secondary parameter', sorted(df.columns[5:]))

plot= st.sidebar.button('Plot Graph')

if plot== True: 
    st.text('Size represents Primary parameter')
    st.text('Color represents Secondary Paramter')

    if selected_state=='Overall India': 

        fig= px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size= primary, color= secondary, zoom = 4, size_max= 35, width= 1200, height= 700, hover_name='State')
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True )

    else: 
        state_df= df[df.State== selected_state]
        fig= px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size= primary, color= secondary, zoom = 4,  size_max= 35, width= 1200, height= 700, hover_name= 'District')
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True )
