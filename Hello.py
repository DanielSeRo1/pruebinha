import streamlit as st
import time

st.set_page_config()

enable = st.checkbox("Activar cámara")
ph = st.empty()
N = 1*60


for secs in range(N,0,-1):
	mm, ss = secs//60, secs%60
	ph.metric("Cuenta regresiva", f"{mm:02d}:{ss:02d}")
	time.sleep(1)
if secs == 0
	st.camera_input
st.image(picture)




