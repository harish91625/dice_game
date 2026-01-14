import streamlit as st
import random
import time

st.title("Random Number Generator (1-6)")

if st.button("Generate Random Number"):
    number = random.randint(1, 6)
    st.metric("Your Number", str(number), delta=None)
    
    # Optional: Dice emoji visualization
    emojis = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    st.subheader(emojis[number] + f"  {number}")
    
    st.balloons()  # Fun celebration effect
