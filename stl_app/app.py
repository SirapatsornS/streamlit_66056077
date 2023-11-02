import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from st_pages import Page, show_pages, add_page_title

show_pages([
    Page("pages/05_iris_data/app.py", "IRIS Data"),
    #Page("pages/06_iris_ml/app_ml.py", "IRIS ML"),
    Page("pages/06_iris_ml/app_st.py", "IRIS ST")
])

add_page_title()

st.markdown('สวัสดี! *Streamlit*')
st.title('IRIS Data')
