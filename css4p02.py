# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:19:51 2024

@author: HadrianBezuidenhout
"""
def load_data():
    df = pandas.read_csv("QPT_Results.csv",sep=";")
    data = df.groupby('Dimension') # Groups data for processing
    return data

data = load_data()
mean_values = data['Fidelity'].mean()

xline = []
for i in range(1,21):
    xline.append(i)
    
yline_2D = data.get_group(2)["Fidelity"]
yline_4D = data.get_group(4)["Fidelity"]
yline_8D = data.get_group(8)["Fidelity"]

fidelity = numpy.array([yline_2D,yline_4D,yline_8D])

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

streamlit.title('Unitary Matrix Fidelity')
streamlit.write('This displays the fidelity of Unitary matrices that were solved for using an optical random walk procedure.')

streamlit.subheader('Fidelity Plot')

events = {
    "click": "function(params) { console.log(params.name); return params.name }",
    "dblclick":"function(params) { return [params.type, params.name, params.value] }"
}

value = st_echarts(options=options, events=events)
streamlit.write(value)  # shows name on bar click and type+name+value on bar double click









