import cv2
import mediapipe as mp

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# Check if finger is straight
def finger_extended(landmarks, tip, pip):
    return landmarks[tip].y < landmarks[pip].y

# Gesture recognition function
def recognize_gesture(landmarks):
    # Thumb: tip.x < ip.x means thumb pointing left
    thumb = landmarks[mp_hands.HandLandmark.THUMB_TIP].x < landmarks[mp_hands.HandLandmark.THUMB_IP].x

    index_finger = finger_extended(landmarks,
                                   mp_hands.HandLandmark.INDEX_FINGER_TIP,
                                   mp_hands.HandLandmark.INDEX_FINGER_PIP)

    middle_finger = finger_extended(landmarks,
                                    mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                                    mp_hands.HandLandmark.MIDDLE_FINGER_PIP)

    ring_finger = finger_extended(landmarks,
                                  mp_hands.HandLandmark.RING_FINGER_TIP,
                                  mp_hands.HandLandmark.RING_FINGER_PIP)

    pinky_finger = finger_extended(landmarks,
                                   mp_hands.HandLandmark.PINKY_TIP,
                                   mp_hands.HandLandmark.PINKY_PIP)

    # Check patterns
    if thumb and index_finger and middle_finger and ring_finger and pinky_finger:
        return "HELLO"

    if index_finger and not middle_finger and pinky_finger:
        return "I LOVE YOU"

    if not (thumb or index_finger or middle_finger or ring_finger or pinky_finger):
        return "YES"

    if index_finger and middle_finger and not ring_finger and not pinky_finger and not thumb:
        return "STOP"

    return None

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gesture = recognize_gesture(hand_landmarks.landmark)

            if gesture:
                cv2.putText(frame, f"Gesture: {gesture}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Simple ISL Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
