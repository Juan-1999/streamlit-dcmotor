import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


st.title("MOTOR DC")
 
option=st.sidebar.selectbox("selecione tipo de conección",("Excitación separada","ES+derivacion","ES+D+serie","ES+D+S+compuesto"))
option1=st.sidebar.selectbox("Generacon del campo magnetico",("Debanado de campo","DC+imanes permanentes"))
