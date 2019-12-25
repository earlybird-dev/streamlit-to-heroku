import streamlit as st
import numpy as np
st.title('A random chart')
chart = st.bar_chart(np.random.rand(10,5))
btn = st.button('Randomise!')
if btn:
    chart.bar_chart(np.random.rand(10,5))