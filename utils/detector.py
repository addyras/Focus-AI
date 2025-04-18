"""
Utility for detecting face and eyes using Mediapipe or OpenCV
"""

import cv2
import mediapipe as mp

class FaceAndEyeDetector:
    def __init__(self):
        # Initialize Mediapipe face mesh solution
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(max_num_faces=1)

        # Draw landmarks on face (for visualization)
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    def detect(self, frame):
        """
        Detects facial landmarks in the input video frame.
        
        Parameters:
            frame (numpy.ndarray): The video frame (BGR format).
        
        Returns:
            frame (numpy.ndarray): Frame with face landmarks drawn.
            landmarks (list): List of landmark coordinates.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        landmarks = []

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                self.mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=self.drawing_spec,
                    connection_drawing_spec=self.drawing_spec
                )
                for lm in face_landmarks.landmark:
                    h, w, _ = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    landmarks.append((x, y))

        return frame, landmarks
