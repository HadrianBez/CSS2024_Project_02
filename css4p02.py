# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:19:51 2024

@author: HadrianBezuidenhout
"""
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_echarts import st_echarts

def load_data():
   # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    df = pd.read_csv("QPT_Results.csv",sep=";")
    data = df.groupby('Dimension') # Groups data for processing
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("Done! (using st.cache_data)")
    return data

data = load_data()
mean_values = data['Fidelity'].mean()

xline = []
for i in range(1,21):
    xline.append(i)
    
yline_2D = data.get_group(2)["Fidelity"]
yline_4D = data.get_group(4)["Fidelity"]
yline_8D = data.get_group(8)["Fidelity"]

fidelity = np.array([yline_2D,yline_4D,yline_8D])

options = {
    "title": {"text": "Unitary Matrix Fidelity"},
   "y": "Fidelity",
   "x": "Run Number",
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["2D", "4D", "8D"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": xline,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "2D",
            "type": "line",
            "stack": "1",
            "data": fidelity[0,:].tolist(),
        },
        {
            "name": "4D",
            "type": "line",
            "stack": "2",
            "data": fidelity[1,:].tolist(),
        },
        {
            "name": "8D",
            "type": "line",
            "stack": "3",
            "data": fidelity[2,:].tolist(),
        },
    ],
}

st.title('Unitary Matrix Fidelity')
st.write('This displays the fidelity of Unitary matrices that were solved for using an optical random walk procedure.')

st.subheader('Fidelity Plot')

events = {
    "click": "function(params) { console.log(params.name); return params.name }",
    "dblclick":"function(params) { return [params.type, params.name, params.value] }"
}

value = st_echarts(options=options, events=events)
st.write(value)  # shows name on bar click and type+name+value on bar double click


import altair as alt

chart = (
        alt.Chart(
            title="Your title",
        )
        .mark_line()
        .encode(
            x=alt.X("capacity 1", axis=alt.Axis(title="Capacity 1")),
            y=alt.Y("capacity 2", axis=alt.Axis(title="Capacity 2")),
        )
)

st.altair_chart(chart)









