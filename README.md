# 🎯 Focus AI - Anti-Cheating Tool

An AI-powered face and eye tracking tool built to detect potential cheating during online exams.  
This is my first project exploring OpenCV, Mediapipe, and real-time video processing.

---

## 🚀 Features

- 🔍 Face detection using OpenCV or Mediapipe
- 👀 Eye gaze tracking to detect off-screen behavior
- ⚠️ Warning alerts when user looks away
- 🧠 Easily extendable for more features (multi-face detection, phone detection, logging, etc.)

---

 🛠️ Setup Instructions
Follow these steps to set up and run the project locally:

Clone the Repository
git clone https://github.com/yourusername/anti-cheating-tool.git
cd anti-cheating-tool

Create and Activate a Virtual Environment
python -m venv venv
.\venv\Scripts\activate      # On Windows

Install Dependencies
pip install -r requirements.txt

Run the Tool
python main.py

🚧 To-Do
- [ ] Improve accuracy of eye gaze detection
- [ ] Add alert sound when the user looks away
- [ ] Implement screenshot saving when cheating is detected
- [ ] Maintain a log file of alerts with timestamps
- [ ] Detect if face disappears from the frame
- [ ] Explore adding mobile phone detection
- [ ] Clean up UI for alert messages
- [ ] Package the tool as an executable (.exe) for easy sharing

