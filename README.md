# Face Detection Based Arduino Control

This project implements a real-time face detection system using Python and OpenCV, integrated with an Arduino Uno through USB serial communication. Based on the presence of a human face detected via a webcam, control signals are sent to the Arduino to operate external hardware such as LEDs.

## Features
- Real-time face detection using Haar Cascade
- Webcam-based live video processing
- USB serial communication with Arduino
- Hardware control based on face presence

## Technologies Used
- Python
- OpenCV
- PySerial
- Arduino Uno
- Haar Cascade Classifier

## How It Works
- The webcam captures live video frames
- Faces are detected using OpenCV
- If a face is detected, a control signal is sent to Arduino
- Arduino processes the signal and controls connected hardware

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python`)
- PySerial (`pip install pyserial`)
- Arduino Uno
- Webcam
- USB cable

## How to Run
1. Upload the Arduino sketch to the board
2. Connect Arduino to the laptop via USB
3. Update the COM port in the Python script if required
4. Run the Python file
5. Press `q` to exit the program

## Applications
- Smart automation systems
- Human presence detection
- Basic security systems
- IoT and embedded system projects
