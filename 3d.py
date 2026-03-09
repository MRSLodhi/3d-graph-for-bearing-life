import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Bearing Life Prediction Model")

# Constants
L0 = 100
a = 1.5
b = 1.2

# Sliders
mechanical_load = st.slider("Mechanical Load (kN)", 1.0, 10.0, 5.0)
electrical_load = st.slider("Electrical Load (A)", 1.0, 5.0, 2.0)

# Create surface data
m = np.linspace(1,10,50)
e = np.linspace(1,5,50)

M,E = np.meshgrid(m,e)

Life = L0/((M**a)*(E**b))

# Current life
life_current = L0/((mechanical_load**a)*(electrical_load**b))

# 3D Surface Plot
fig = go.Figure()

fig.add_surface(
    x=M,
    y=E,
    z=Life,
    opacity=0.8
)

# Current operating point
fig.add_scatter3d(
    x=[mechanical_load],
    y=[electrical_load],
    z=[life_current],
    mode='markers+text',
    marker=dict(size=6),
    text=[f"{life_current:.2f} Mrev"],
    textposition="top center"
)

fig.update_layout(
    scene=dict(
        xaxis_title='Mechanical Load',
        yaxis_title='Electrical Load',
        zaxis_title='Bearing Life (Million Revolutions)'
    ),
    height=700
)

st.plotly_chart(fig, use_container_width=True)

st.metric("Predicted Bearing Life (Million Revolutions)", f"{life_current:.2f}")