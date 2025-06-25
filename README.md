
# ISL Gesture Recognition

A real-time hand gesture recognition system using [MediaPipe] and [OpenCV] to interpret basic Indian Sign Language (ISL) signs via webcam.

✨ Features
- Real-time video capture and hand tracking
- Landmark smoothing for stable predictions
- Gesture recognition for:
  - HELLO (all fingers extended)
  - I LOVE YOU (index and pinky extended)
  - YES (fist)
  - STOP (index and middle fingers only)
- Gesture stability via rolling buffer voting

📦 Requirements
- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

Install Dependencies
bash
pip install opencv-python mediapipe numpy


🚀 Usage

Run the script:

bash
python isl_gesture_recognition.py


Press `q` to quit the application.

🧠 How It Works
- Captures video feed from your webcam.
- Detects and tracks one hand using MediaPipe.
- Applies landmark smoothing to reduce jitter.
- Recognizes static hand gestures based on finger states.
- Uses a buffer (`deque`) to ensure consistent gesture classification.

🖐️ Supported Gestures

| Gesture        | Description                             |
|----------------|-----------------------------------------|
| HELLO          | All fingers extended                    |
| I LOVE YOU     | Index and pinky extended only           |
| YES            | All fingers folded (fist)               |
| STOP           | Index and middle extended only          |

📌 Notes
- Designed for single-hand gestures.
- Works best in well-lit conditions.
- May require fine-tuning for different hand orientations or lighting environments.

🙌 Acknowledgements
- MediaPipe Hands by Google
- OpenCV for video handling and drawing

