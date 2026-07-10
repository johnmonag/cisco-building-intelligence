import streamlit as st
from streamlit_echarts import st_echarts
import random

def get_live_data(base_value, num_points=10):
    data = [base_value]
    for _ in range(num_points - 1):
        change = random.uniform(-1.5, 1.5)
        data.append(max(0, round(data[-1] + change, 1)))
    return data

def get_sparkline_options(data, color="#00B5E2"):
    options = {
        "xAxis": {"type": "category", "show": False},
        "yAxis": {"type": "value", "show": False},
        "series": [{
            "data": data,
            "type": "line",
            "smooth": True,
            "showSymbol": False,
            "lineStyle": {"width": 2, "color": color},
            "areaStyle": {"color": color, "opacity": 0.1}
        }],
        "grid": {"top": 5, "bottom": 5, "left": 0, "right": 0}
    }
    return options

def render_zone_status(zone_name, occupancy, status_color):
    """
    Renders a compact visual tile for a building zone.
    """
    html_content = f"""
    <div style="
        background-color: #ffffff; 
        padding: 8px 12px; 
        border-radius: 8px; 
        border-left: 4px solid {status_color}; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-family: sans-serif;
    ">
        <div style="font-size: 0.9em; color: #555;">{zone_name}</div>
        <div style="font-size: 1.1em; font-weight: bold; color: #222;">{occupancy}%</div>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)