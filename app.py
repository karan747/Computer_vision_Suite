import streamlit as st
from pathlib import Path
import importlib

# Page configuration
st.set_page_config(
    page_title="OpenCV Explorer",
    page_icon="📸",
    layout="wide",
)

# Dictionary to hold page names and corresponding module paths
PAGES = {
    "Home": "pages.home",
    "Arithmetic Operations": "pages.arithmetic",
    "Object Detection": "pages.object_detection",
    "Lane Detection": "pages.lane_detection",
}

# Sidebar for navigation
st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Dynamic page loader
def load_page(page_name):
    page_module = importlib.import_module(PAGES[page_name])
    page_module.app()

# Load the selected page
load_page(page_selection)