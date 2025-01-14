import streamlit as st
import time

st.set_page_config()

enable = st.checkbox("Activar cámara")
picture = st.camera_input("Tomar foto", disabled = not enable)

ph = st.empty()
N = 1*60
if picture:
	for secs in range(N,0,-1):
		mm, ss = secs//60, secs%60
		ph.metric("Cuenta regresiva", f"{mm:02d}:{ss:02d}")
	st.image(picture)

