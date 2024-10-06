from math import degrees
from turtle import bgcolor
import pandas as pd
import plotly.graph_objects as go
import numpy as np

estrellas = pd.read_csv("./stars.csv")

planetas = pd.read_csv("./planetas.csv")

estrellas = estrellas.dropna()

def deg_to_rad(deg):
    return np.radians(deg)

def getCoords(distance, ra,dec):
    ra_rad = deg_to_rad(ra)
    dec_rad = deg_to_rad(dec)
    x = distance*np.cos(dec_rad)*np.cos(ra_rad)
    y = distance*np.cos(dec_rad)*np.sin(ra_rad)
    z = distance*np.sin(dec_rad)
    return x,y,z


x_coords = []
y_coords = []
z_coords = []
names = []

for index,row in planetas.iterrows():
    x,y,z = getCoords(row['sy_dist'], row['ra'], row['dec'])
    x_coords.append(x* 10000)
    y_coords.append(y* 10000)
    z_coords.append(z* 10000)
    names.append(row['pl_name'])


scatterPlanet = go.Scatter3d(
    x = x_coords,
    y = y_coords,
    z = z_coords,


    text = names,
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'blue',
        opacity = 0.4
    )
)


x_coordsStar = []
y_coordsStar = []
z_coordsStar = []
namesStar = []


for index,row in estrellas.iterrows():
    x,y,z = getCoords(row['sy_plx'], row['ra'], row['dec'])
    x_coordsStar.append(x * 10000)
    y_coordsStar.append(y * 10000)
    z_coordsStar.append(z* 10000)
    namesStar.append(row['sy_name'])


scatterStar = go.Scatter3d(
    x = x_coordsStar,
    y = y_coordsStar,
    z = z_coordsStar,

    text = namesStar,
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'red',
        opacity = 1
    )
)

fig = go.Figure(data=[scatterPlanet,scatterStar])
fig2 = go.Figure(data=scatterStar)

fig.update_layout(
    title = 'posición de exoplanetas en el espacio',
    scene = dict(
        xaxis_title = 'X (Años luz)',
        yaxis_title = 'Y (Años luz)',
        zaxis_title = 'Z (Años luz)',
        bgcolor = 'black'
    ),
    
    paper_bgcolor='black',
    margin = dict(l=0, r = 0, b = 0, t = 0)
)

fig.show()
