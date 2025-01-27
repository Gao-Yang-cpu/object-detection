import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Object Detection using YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Object Detection And Tracking using YOLOv8")
st.sidebar.header("ML Model Config")
model_type = st.sidebar.radio(
    "Select Task", ['Detection', 'Segmentation'])
confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 40)) / 100
if model_type == 'Detection':
    model_path = Path('weights/yolov8n.pt')
elif model_type == 'Segmentation':
    model_path = Path('weights/yolov8n-seg.pt')

VIDEOS_DICT = {
    'video_1': 'videos/video_1.mp4',
    'video_2': 'videos/video_2.mp4',
    'video_3': 'videos/video_3.mp4',
}

source_vid = st.sidebar.selectbox(
        "Choose a video...", VIDEOS_DICT.keys())

display_tracker = st.sidebar.radio("Display Tracker", ('Yes', 'No'))
tracker_type = st.sidebar.radio("Tracker", ("bytetrack.yaml", "botsort.yaml"))