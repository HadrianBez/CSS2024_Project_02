# CSS2024_Project_02
Option 2: Streamlit App - Project 2 for Coding Summer School

The values being plotted are the fidelities of unitary matrices that were solved for using an optical random walk procedure.

The data is first read from a .csv file in a dataframe and is grouped according the the dimensions of the matrix. The fidelity values of each dimension/group are then extracted and placed into an array named "fidelity". These values are then plotted for each of the 20 runs using a stacked line plot which show the fidelity on the y-axis and the run number on the x-axis. The plot was made using the st_echarts package included in streamlit.

The plot was uniquely formatted to include a legend with each dimension displaying in a different colour, in addition to this the lines for each dimension can be toggled by clicking on the appropriate legend entry.

Some additional features were added such as the line "@st.cache_data" which allows the data to be loaded from an existing cache to speed up processing, as well as update messages for when the data being retrieved and when it is finished loading.
