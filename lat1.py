import streamlit as st
import pandas as pd
#import matplotlib.pyplot as pyplot

st.write("Tabel Coding Puput")
df = pd.DataFrame({
    'No': [1,2,3,4],
    'Nama': ['Anita','Putri','Kiya','Ety'],
    'Nilai': [100,100,100,100]
    })

df