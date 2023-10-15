import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')
st.backgroundColor="#FFFFFF"
data=pd.read_csv('C:/Users/Pratik/Desktop/project2/India.csv')
st.sidebar.title('Indian States')
list_of_states=list(data['State'].unique())
list_of_states.insert(0,'Overall India')
select_state=st.sidebar.selectbox('Select a States',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parametre',data.columns[5:])
secondary=st.sidebar.selectbox('Select Secondary Parametre',data.columns[5:])
plot=st.sidebar.button('Plot Graph')
if plot:
    st.text('Size represent Primary parametre')
    st.text('Color represent Secondary parametre')
    if select_state=='Overall India':
        fig = px.scatter_mapbox(data, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                  size_max=22, zoom=4,width=1000,height=900,color_continuous_scale='Inferno',hover_name='State',
                  hover_data=["State", "District"],mapbox_style="carto-positron")
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_data=data[data['State']==select_state]
        fig = px.scatter_mapbox(state_data, lat="Latitude", lon="Longitude", color=secondary, size=primary,
                  size_max=20, zoom=4,width=1000,height=900,color_continuous_scale='Inferno',hover_name='District',
                  mapbox_style="carto-positron")
        st.plotly_chart(fig,use_container_width=True)