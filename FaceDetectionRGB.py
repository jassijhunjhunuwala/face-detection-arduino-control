import cv2
import serial
import time

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if cascade loaded correctly
if face_cascade.empty():
    print("Error: Could not load Haar Cascade classifier")
    exit()

# Initialize webcam (index 0 as per your code)
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam. Try changing the camera index (e.g., 1)")
    exit()

# Connect to Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)  # Wait for Arduino to initialize
    print("Connected to", arduino.portstr)
except serial.SerialException as e:
    print("Connection Error:", e)
    exit()

try:
    while True:
        # Read frame from webcam
        success, img = cap.read()
        if not success:
            print("Error: Failed to read frame from webcam")
            break

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # If faces detected, send [1, 0, 1], else send [0, 1, 1]
        if len(faces) > 0:
            arduino.write(b'101')  # Send [1, 0, 1] for face detected
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw green rectangle
            time.sleep(0.1)
            response = arduino.readline().decode().strip()
            if response:
                print("Arduino Response:", response)
        else:
            arduino.write(b'011')  # Send [0, 1, 1] for no face
            time.sleep(0.1)
            response = arduino.readline().decode().strip()
            if response:
                print("Arduino Response:", response)

        # Show the image
        cv2.imshow("Image", img)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nProgram terminated by user")
except Exception as e:
    print("Error:", e)
finally:
    arduino.close()
    cap.release()
    cv2.destroyAllWindows()
    print("Port, webcam, and windows closed")