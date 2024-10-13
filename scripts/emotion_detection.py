import cv2
from deepface import DeepFace

class EmotionRecognizer:
    def detect_emotion(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(gray_frame)

        for (x, y, w, h) in faces:
            face_roi = frame[y:y+h, x:x+w]
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            return result['dominant_emotion']

# Capturing webcam input for real-time emotion detection
cap = cv2.VideoCapture(0)
emotion_recognizer = EmotionRecognizer()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    emotion = emotion_recognizer.detect_emotion(frame)
    cv2.putText(frame, f"Emotion: {emotion}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Emotion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
