Detectify: An Object Detection Web Application
![Detectify Banner](C:\Users\Sunny\Pictures\banner.png)
Overview
Detectify is an intuitive and robust web application for real-time object detection powered by YOLOv5 and Streamlit. It allows users to upload images or capture photos using their webcam to detect and highlight objects such as cars, bikes, and people. Designed with user-friendliness and performance in mind, Detectify provides an interactive experience for exploring machine learning in object detection.

Features
Real-time Object Detection: Upload images or capture photos from the webcam for AI-based object detection.
YOLOv5 Integration: Leverages the YOLOv5 model for high-accuracy detection.
User-Friendly Interface: Designed with Streamlit for seamless interaction.
Customization: Easily extendable to include more object categories or features.
Responsive Design: Includes dynamic styling for an enhanced user experience.
Technologies Used
Backend: Python, Streamlit, PyTorch
Frontend: HTML, CSS, Bootstrap
Machine Learning Model: YOLOv5
Libraries: OpenCV, PIL, NumPy
How It Works
Image Input: Upload an image or capture one using your webcam.
Object Detection: Detects objects using the pre-trained YOLOv5 model.
Result Visualization: Highlights detected objects in the image and displays the processed result.
Installation
Clone the Repository

git clone https://github.com/your-username/Detectify.git
cd Detectify
Install Dependencies Ensure you have Python 3.7+ installed.

pip install -r requirements.txt
Run the Application

streamlit run app.py
Access the Application Open your browser and navigate to http://localhost:8501.

Directory Structure
php
Copy code
Detectify/
│
├── app.py           # Main application logic
├── templates/       # HTML templates
│   ├── index.html
│   ├── upload.html
│   ├── result.html
│
├── static/          # Static assets (CSS, JS, images)
├── uploads/         # Uploaded images for processing
├── README.md        # Project documentation
├── requirements.txt # Python dependencies
Screenshots

Home Page
![image](https://github.com/user-attachments/assets/98362e3f-e137-4c50-a1d6-4a75531eaf10)

Object Detection Results
1. Image
   ![image](https://github.com/user-attachments/assets/7de543b0-d50d-4b2b-b9b9-2c360e43d8d7)
   ![image](https://github.com/user-attachments/assets/4a9604be-caf1-440a-a2cc-d19ada7d8854)
   
2. Webcam
   ![image](https://github.com/user-attachments/assets/77ca08ee-fe1b-410f-a1e0-98a663969b4a)

Future Enhancements
Support for video file input.
Object tracking in real-time video streams.
Integration with cloud services for scalability.

License
This project is not licensed. This is completely free except the bootstrap website template.

Acknowledgments
We would like to thank all contributors for their efforts in developing and improving this project.
