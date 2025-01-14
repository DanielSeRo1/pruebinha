import streamlit as st
import time

st.set_page_config()

enable = st.checkbox("Activar cámara")
ph = st.empty()
N = 15
picture = st.camera_input("Tomar foto", disabled = not enable)





