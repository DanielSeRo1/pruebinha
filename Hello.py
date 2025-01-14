import streamlit as st
import time

st.set_page_config()

enable = st.checkbox("Activar cámara")
ph = st.empty()
N = 15
picture = st.camera_input("Tomar foto", disabled = not enable)
ph.metric("Cuenta regresiva", f"{mm:02d}:{ss:02d}")
  





