# import streamlit as st
# import torch  # PyTorch for model loading
# import cv2
# import os
# from PIL import Image
# import numpy as np

# # Set up directories for saving uploads
# UPLOAD_FOLDER = 'uploads'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # Load YOLOv5 model (use Roboflow-trained version or YOLOv5s)
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# # Title and instructions
# st.title("Object Detection using YOLOv5")
# st.write("Upload an image, and the app will detect objects like cars, bikes, and people using a pre-trained model.")

# # File upload in Streamlit
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     # Save the uploaded file
#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     # Display the uploaded image
#     st.image(file_path, caption="Uploaded Image", use_column_width=True)
    
#     # Perform object detection using YOLOv5
#     results = model(file_path)
    
#     # Extract the bounding boxes and labels
#     results_img = results.render()[0]  # YOLOv5 'render' returns a list of numpy arrays
    
#     # Convert numpy array (OpenCV format) back to PIL image
#     detected_image = Image.fromarray(results_img)

#     # Display the detected objects image
#     st.image(detected_image, caption="Detected Objects", use_column_width=True)


## NEW CODE ##

# import streamlit as st
# import torch  # PyTorch for model loading
# import os
# from PIL import Image

# # Set up directories for saving uploads
# UPLOAD_FOLDER = 'uploads'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # Load a more accurate YOLOv5 model (YOLOv5x is more accurate but slower than YOLOv5s)
# model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

# # Set the confidence threshold
# model.conf = 0.20  # Set confidence threshold to 0.20 to capture more objects

# # Title and instructions
# st.title("Object Detection using YOLOv5")
# st.write("Upload an image, and the app will detect objects like cars, bikes, and people using a pre-trained model.")

# # File upload in Streamlit
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     # Save the uploaded file
#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     # Display the uploaded image
#     st.image(file_path, caption="Uploaded Image", use_column_width=True)
    
#     # Perform object detection using YOLOv5
#     results = model(file_path)
    
#     # Extract the bounding boxes and labels
#     results_img = results.render()[0]  # YOLOv5 'render' returns a list of numpy arrays
    
#     # Convert numpy array (OpenCV format) back to PIL image
#     detected_image = Image.fromarray(results_img)

#     # Display the detected objects image
#     st.image(detected_image, caption="Detected Objects", use_column_width=True)









import streamlit as st
import torch  # PyTorch for model loading
import os
from PIL import Image

# --- Custom CSS for enhanced styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    body {
        background: linear-gradient(to bottom right, #ffffff, #e0eafc);
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    .title h1 {
        font-family: 'Segoe Script', sans-serif;
        font-weight: 600;
        color: #1f77b4;
        text-align: center;
        font-size: 48px;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .upload-area {
        padding: 20px;
        text-align: center;
        border-radius: 15px;
        background-color: #f9f9f9;
        border: 2px dashed #a3c9f1;
        transition: background-color 0.3s ease;
    }
    .upload-area:hover {
        background-color: black;
    }
    .stButton button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        border-radius: 12px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .footer {
        margin-top: 50px;
        font-family: 'Poppins', sans-serif;
        color: #8c8c8c;
        text-align: center;
    }
    .spinner {
        margin-top: 20px;
    }
    .success-msg {
        font-size: 18px;
        font-weight: 500;
        color: #28a745;
        margin-top: 10px;
    }
    .image-box {
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Set up directories for saving uploads ---
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# --- Load the YOLOv5 model ---
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)
model.conf = 0.20  # Set confidence threshold

# --- Title and Instructions ---
st.markdown("<div class='title'><h1 style='text-align: center;'>🔍 DeTeCTifY</h1></div>", unsafe_allow_html=True)
st.write("Upload an image below, and our AI will detect objects like **cars**, **bikes**, and **people**.")

# --- File Upload Section ---
st.markdown("<div class='upload-area'><h3>📤 Browse to upload an image</h3></div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # --- Display the uploaded image ---
    st.markdown("### 🖼️ Uploaded Image")
    st.image(file_path, caption="Uploaded Image", use_column_width=True)

    # Add spinner while object detection is running
    with st.spinner("Detecting objects, please wait..."):
        # Perform object detection using YOLOv5
        results = model(file_path)
    
    # Extract the bounding boxes and labels
    results_img = results.render()[0]  # YOLOv5 'render' returns a list of numpy arrays
    
    # Convert numpy array (OpenCV format) back to PIL image
    detected_image = Image.fromarray(results_img)

    # Display the detected objects image
    st.markdown("### 🎯 Detected Objects")
    st.image(detected_image, caption="Detected Objects", use_column_width=True)

    # Success message
    st.markdown("<div class='success-msg'>✅ Object detection completed successfully!</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>Made with 💻 and ❤️ using YOLOv5 and Streamlit.</div>", unsafe_allow_html=True)
