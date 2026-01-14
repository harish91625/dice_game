import streamlit as st
import random

st.title("Random Number Generator (1-6)")

if st.button("Generate 6 Different Numbers"):
    numbers = random.sample(range(1, 7), 6)
    st.metric("Generated Numbers", " | ".join(map(str, numbers)))
