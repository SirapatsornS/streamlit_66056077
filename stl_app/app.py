import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from st_pages import Page, show_pages, add_page_title

show_pages([
    Page("pages/05_iris_data/app.py", "IRIS Data"),
    Page("pages/05_iris_data/map.py", "Map Layout"),
])

add_page_title()

