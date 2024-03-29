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
    data_load_state.text("Finished loading data! (using st.cache_data)")
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
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["2D", "4D", "8D"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "xAxis": {
      "type": "category",
      "boundaryGap": False,
      "data": xline,
      "name": "Run Number",
      "nameLocation": 'end',
      "nameGap": 0,
      "nameTextStyle": {
      "align": 'right',
      "verticalAlign": 'top',
      "fontWeight": 'bolder',
      "padding": [20, 280, 0, 0]
    }},
    "yAxis": {"type": "value",
      "name": "Fidelity",
      "nameGap": 15,
      "nameLocation": 'end',
      "nameTextStyle": {
      "fontWeight": 'bolder',
      "align": 'right'
    }},
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
st.write('This plot displays the fidelities of Unitary matrices that were solved experimentally using an optical random walk procedure. These unitary matrices are used to cancel noise in a signal and therefore the fidelities are computed by comparing the experimental matrix with a matrix that would theoretically cancel the noise completely.\n \n The system was tested 20 times for 3 dimensions (2D, 4D and 8D), and the fidelities of each run are plotted below.')
events = {
    "click": "function(params) { console.log(params.name); return params.name }",
    "dblclick":"function(params) { return [params.type, params.name, params.value] }"
}

value = st_echarts(options=options, height="400px", events=events)
st.write(value)  # shows name on bar click and type+name+value on bar double click




