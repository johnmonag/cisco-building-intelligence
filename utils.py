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
    return {
        "xAxis": {"type": "category", "show": False},
        "yAxis": {"type": "value", "show": False},
        "series": [{
            "data": data, "type": "line", "smooth": True, "showSymbol": False,
            "lineStyle": {"width": 2, "color": color},
            "areaStyle": {"color": color, "opacity": 0.1}
        }],
        "grid": {"top": 5, "bottom": 5, "left": 0, "right": 0}
    }

def render_zone_status(zone_name, occupancy, status_color):
    html_content = f"""
    <div style="
        background-color: #ffffff; padding: 8px 12px; border-radius: 8px;
        border-left: 4px solid {status_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 8px; display: flex; justify-content: space-between;
        align-items: center; font-family: sans-serif;
    ">
        <div style="font-size: 0.9em; color: #555;">{zone_name}</div>
        <div style="font-size: 1.1em; font-weight: bold; color: #222;">{occupancy}%</div>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

def get_hvac_raw_datasets():
    """
    Returns multiple raw sensor feeds to illustrate data complexity.
    Mirrors the incident window from the report.
    """
    times = ["20:10", "20:15", "20:20", "20:25", "20:30", "20:35", "20:40", "20:45", "20:50", "20:55"]
    datasets = {
        "CHW Inlet Temp (°C)": [11.2, 11.4, 206.0, 205.9, 205.9, 206.0, 206.1, 206.1, 11.7, 11.5],
        "LTHW Inlet Temp (°C)": [47.8, 47.9, 49.0, 148.8, 101.2, 86.6, 148.7, 85.7, 49.2, 48.9],
        "Aircoil Temp (°C)": [11.1, 11.3, 3276.7, 3276.7, 3276.7, 3276.7, 3276.7, 3276.7, 11.4, 11.2],
        "Discharge Pressure (bar)": [9.1, 9.2, 35.6, 35.5, 35.6, 35.4, 35.6, 35.5, 9.3, 9.1],
        "Suction Pressure (bar)": [2.2, 2.2, 1.3, 1.2, 1.4, 1.8, 1.5, 1.2, 2.2, 2.1],
        "Mains Power (kW)": [14.8, 15.1, 35.4, 35.4, 35.4, 35.4, 35.4, 35.4, 15.2, 14.9],
    }
    return times, datasets

def get_single_line_options(times, data, color):
    """Generates a simple, standalone line chart for a single raw sensor feed."""
    return {
        "tooltip": {"trigger": "axis"},
        "xAxis": {"type": "category", "data": times, "axisLabel": {"fontSize": 9}},
        "yAxis": {"type": "value"},
        "series": [{
            "data": data, "type": "line", "smooth": False,
            "itemStyle": {"color": color},
            "lineStyle": {"width": 2, "color": color},
            "areaStyle": {"color": color, "opacity": 0.08}
        }],
        "grid": {"top": 20, "bottom": 25, "left": 40, "right": 15}
    }