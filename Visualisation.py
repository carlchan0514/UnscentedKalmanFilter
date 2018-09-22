import plotly.offline as py
py.init_notebook_mode(connected=True)
import pandas as pd
from plotly.graph_objs import *
import plotly.graph_objs as go
import math

#input file fields as they are saved into the UKF output file
my_cols=['timestamp','px_est','py_est','v_est','yaw_angle_est','yaw_rate_est','sensor_type','px_meas','py_meas','NIS','px_ground_truth', 'py_ground_truth', 'vx_ground_truth','vy_ground_truth']

with open('./output/output.txt') as f:
    ukf_df = pd.read_table(f, sep='\t', header=None, names=my_cols, lineterminator='\n')

# print(ukf_df.head(10))

#Ground Truth
trace1 = go.Scatter(
    x=ukf_df['px_ground_truth'],
    y=ukf_df['py_ground_truth'],
    xaxis='x2',
    yaxis='y2',
    name = 'ground truth position',
    mode = 'markers'
)

#estimations
trace2 = go.Scatter(
    x=ukf_df['px_est'],
    y=ukf_df['py_est'],
    xaxis='x2',
    yaxis='y2',
    name='UKF position estimation',
    mode = 'markers'
)

#Measurements
trace3 = go.Scatter(
    x=ukf_df['px_meas'],
    y=ukf_df['py_meas'],
    xaxis='x2',
    yaxis='y2',
    name = 'position measurements',
    #mode = 'markers'
)


data = [trace1, trace2, trace3]

layout = Layout(
    xaxis2=dict(
        anchor='x2',
        title='px in m'
    ),
    yaxis2=dict(
        anchor='y2',
        title='py in m'
    )
)

fig = Figure(data=data, layout=layout)
py.plot(fig, filename= 'UKF.html', image='png', image_filename='UKF')
