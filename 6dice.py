import streamlit as st
import plotly.graph_objects as go
import numpy as np
import random

# Streamlit app title
st.title("3D Dice Roller (1-6)")

# Button to roll the dice
if st.button("Roll Dice", type="primary"):
    dice_number = random.randint(1, 6)
    st.session_state.dice_number = dice_number
    st.session_state.roll_trigger = random.random()  # Trigger rerun for animation

# Get current dice number (default to 1)
dice_number = st.session_state.get('dice_number', 1)

# Define dice faces: dots positions for each number (top face relative)
# Each dot is a small sphere (scatter3d point)
dots = {
    1: [[0.5, 0.5, 0.9]],
    2: [[0.2, 0.2, 0.9], [0.8, 0.8, 0.9]],
    3: [[0.2, 0.2, 0.9], [0.5, 0.5, 0.9], [0.8, 0.8, 0.9]],
    4: [[0.2, 0.2, 0.9], [0.2, 0.8, 0.9], [0.8, 0.2, 0.9], [0.8, 0.8, 0.9]],
    5: [[0.2, 0.2, 0.9], [0.2, 0.8, 0.9], [0.5, 0.5, 0.9], [0.8, 0.2, 0.9], [0.8, 0.8, 0.9]],
    6: [[0.2, 0.2, 0.9], [0.2, 0.5, 0.9], [0.2, 0.8, 0.9], [0.8, 0.2, 0.9], [0.8, 0.5, 0.9], [0.8, 0.8, 0.9]]
}

dot_positions = np.array(dots[dice_number])

# Dice cube vertices (unit cube centered at origin, top face at z=0.5)
vertices_x = np.array([0, 0, 1, 1, 0, 0, 1, 1])
vertices_y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
vertices_z = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Faces for Mesh3d (12 triangles for cube)
faces_i = np.array([0,0,0,0, 4,4,4,4, 2,2,2,2])
faces_j = np.array([1,5,7,3, 1,5,7,3, 6,7,5,1])
faces_k = np.array([2,2,3,3, 6,7,5,1, 6,3,5,3])

# Create figure
fig = go.Figure()

# Add cube mesh (white dice body, semi-transparent)
fig.add_trace(go.Mesh3d(
    x=vertices_x - 0.5,
    y=vertices_y - 0.5,
    z=vertices_z - 0.5,
    i=faces_i, j=faces_j, k=faces_k,
    color='white',
    opacity=0.9,
    lighting=dict(ambient=0.4, diffuse=0.8, fresnel=0.2, specular=0.05),
    lightposition=dict(x=1.5, y=1.5, z=2)
))

# Add black dots on top face
fig.add_trace(go.Scatter3d(
    x=dot_positions[:,0] - 0.5,
    y=dot_positions[:,1] - 0.5,
    z=dot_positions[:,2] - 0.5,
    mode='markers',
    marker=dict(size=20, color='black', symbol='circle'),
    name='Dots'
))

# Update layout for better 3D view (angled to show top face)
fig.update_layout(
    title=f"Rolled: {dice_number} 🎲",
    width=500,
    height=500,
    scene=dict(
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        zaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        camera_eye=dict(x=1.5, y=1.5, z=1.2),
        aspectmode='cube'
    ),
    showlegend=False,
    margin=dict(l=0, r=0, t=50, b=0)
)

# Display the interactive 3D plot
st.plotly_chart(fig, use_container_width=True)

# Instructions
st.info("Click 'Roll Dice' to generate a random number from 1 to 6 and see the 3D dice update with the correct number of dots on top!")
