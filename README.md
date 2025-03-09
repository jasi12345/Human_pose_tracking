
# Pose Detection using MediaPipe and OpenCV

This project uses MediaPipe's Pose module to perform real-time human pose detection in videos. It draws pose landmarks on the input video and prints the detected landmarks to the console.

# Prerequisites
Before running the project, make sure you have the following dependencies installed:

Python 3.x
OpenCV
MediaPipe

You can install the required libraries using pip:
pip install opencv-python mediapipe

# Project Overview
This project captures a video input, processes the video frames to detect human pose landmarks, and visualizes the results using OpenCV. The pose landmarks are drawn on each frame, showing connections between body parts.

# Features
Video input from a file (robot.mp4 in this case).
Pose landmarks detection with confidence thresholds.
Display pose landmarks on the video frame.
Real-time processing and visualization of pose landmarks.
Exit the video by pressing the 'q' key.

#  Usage
Clone this repository or download the Python script to your local machine.
Place your video file in the appropriate directory, or modify the script to point to your video file.
Run the Python script:

python pose_detection.py

The video will open, and you will see the detected pose landmarks drawn on each frame.
Press the q key to quit and close the window.

# Code Explanation
Loading the video:
The video is loaded using OpenCV's cv2.VideoCapture() function.

Pose Detection:
MediaPipe's Pose model is used to detect human body landmarks. It is initialized with a confidence level for both detection and tracking. The landmarks are drawn using mp_drawing.draw_landmarks().

Display:
The cv2.imshow() function is used to display the frame with the drawn landmarks in real-time. Press the q key to exit.

Cleanup:
The video is released using video.release() and all OpenCV windows are destroyed using cv2.destroyAllWindows().

Troubleshooting
Video Not Loading:
If you encounter the error "Error: Video is not Loaded," check the path to the video file to ensure it is correct and accessible.

Slow Processing:
If the video is lagging, consider lowering the resolution or reducing the video length for faster processing.


![1](https://github.com/user-attachments/assets/49605ca6-f799-4fca-ae8e-c17560bd291c)
