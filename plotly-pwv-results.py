from plotly import tools as tls
import numpy as np
import plotly.graph_objs as go

# Define the x-axis time labels
x = ['00:00', '02:00', '04:00','06:00', '08:00', '10:00','12:00', '14:00', '16:00','18:00', '20:00','22:00']

# Load the data for PWV (precipitable water vapor) and TPS (temperature)
a1, a2, a3, a4 = [], [], [], []
for i in range(12):
    a1.append(np.array(np.loadtxt('pwvsummeru.txt')).reshape(12,4)[i][0])
    a2.append(np.array(np.loadtxt('pwvsummeru.txt')).reshape(12,4)[i][1])
    a3.append(np.array(np.loadtxt('pwvsummeru.txt')).reshape(12,4)[i][2])
    a4.append(np.array(np.loadtxt('pwvsummeru.txt')).reshape(12,4)[i][3])

t1, t2, t3, t4 = [], [], [], []
for i in range(12):
    t1.append(np.array(np.loadtxt('tps-sum23.txt')).reshape(12,4)[i][0])
    t2.append(np.array(np.loadtxt('tps-sum23.txt')).reshape(12,4)[i][1])
    t3.append(np.array(np.loadtxt('tps-sum23.txt')).reshape(12,4)[i][2])
    t4.append(np.array(np.loadtxt('tps-sum23.txt')).reshape(12,4)[i][3])

# Create traces for Plotly scatter plots
trace1 = go.Scatter(x=x, y=a1, mode='lines', name='Trace 1')
trace2 = go.Scatter(x=x, y=a2, mode='lines', name='Trace 2')
trace3 = go.Scatter(x=x, y=a3, mode='lines', name='Trace 3')
trace4 = go.Scatter(x=x, y=a4, mode='lines', name='Trace 4')

# Create a layout for the plot
layout = go.Layout(
    title='PWV and Temperature Data',
    xaxis=dict(title='Time'),
    yaxis=dict(title='Values'),
    showlegend=True
)

# Create the figure and display the plot
fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
fig.show()
