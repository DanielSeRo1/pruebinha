import streamlit as st
import time

st.set_page_config()

ph = st.empty()
N = 5*60
for secs i range(N,0,-1):
	mm, ss = secs//60, secs%60
	ph.metric("Cuenta regresiva", f"{mm:02d}:{ss:02d}")
	time.sleep(1)
