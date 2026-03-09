"""
Helper functions for rendering Streamlit placeholder UI.
Extend with real forms, schedule widgets, and dashboard components as features are added.
"""

import streamlit as st


def render_placeholder_section(title, message="Scaffold placeholder."):
    """
    Render a simple section with a title and placeholder message.
    Replace with real content when the corresponding feature is implemented.
    """
    st.subheader(title)
    st.info(message)
