import cv2
import mediapipe as mp
import time
import os
from datetime import datetime

# Create the screenshots folder if it doesn't exist
screenshot_dir = "cheating_screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Initialize Mediapipe face and eye detection
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

# Start capturing webcam feed
cap = cv2.VideoCapture(0)

# Function to save screenshot with timestamp
def save_screenshot(frame):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
    cv2.imwrite(filename, frame)
    print(f"[!] Cheating detected! Screenshot saved: {filename}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get eye coordinates
            left_eye = face_landmarks.landmark[33]  # Left eye corner
            right_eye = face_landmarks.landmark[263]  # Right eye corner

            eye_x = (left_eye.x + right_eye.x) / 2
            # Check if user is looking too far left or right
            if eye_x < 0.4 or eye_x > 0.6:
                save_screenshot(frame)

            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

    cv2.imshow("Focus-AI Anti-Cheating Tool", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
