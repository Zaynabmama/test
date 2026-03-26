
import streamlit as st
from budg.ui_old_tool import render_old_tool
from budg.ui_new_bud2026 import render_new_bud_tool

st.set_page_config(page_title="AR Backlog", layout="wide")
st.title("AR Backlog")

tab_old, tab_new = st.tabs(["AR Backlog → 3 sheets", "BUD2026 from By_Customer"])

with tab_old:
    render_old_tool()

with tab_new:
    render_new_bud_tool()
