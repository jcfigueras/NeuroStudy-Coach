"""
NeuroStudy Coach – Streamlit entry point.
Scaffold only: placeholder sections for Assignments, Study Schedule, Learning Materials, Progress Dashboard.
"""

import sys
from pathlib import Path

# Allow importing from src when running from project root
sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
from src.config import APP_NAME
from src.ui.components import render_placeholder_section

# Page config
st.set_page_config(page_title=APP_NAME, page_icon="📚", layout="wide")

# Sidebar navigation
SECTION_OPTIONS = [
    "Assignments",
    "Study Schedule",
    "Learning Materials",
    "Progress Dashboard",
]
st.sidebar.title(APP_NAME)
st.sidebar.markdown("Adaptive study planning and learning support for neurodivergent students.")
selected = st.sidebar.radio("Section", SECTION_OPTIONS, label_visibility="collapsed")

# Main area: title and description
st.title(APP_NAME)
st.markdown(
    "A local, privacy-first app for adaptive study scheduling, pacing, and learning materials. "
    "This is the initial scaffold; features will be added by the team."
)

# Placeholder sections
if selected == "Assignments":
    render_placeholder_section("Assignments", "Coming soon. Add assignments with course, due date, and estimated time here.")

elif selected == "Study Schedule":
    render_placeholder_section("Study Schedule", "Scaffold placeholder. Day-by-day study plan will appear here.")

elif selected == "Learning Materials":
    render_placeholder_section("Learning Materials", "Coming soon. Upload and search course materials here.")

elif selected == "Progress Dashboard":
    render_placeholder_section("Progress Dashboard", "Scaffold placeholder. Completed time, remaining workload, and deadlines will appear here.")
