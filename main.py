import cv2
import numpy as np
import tensorflow as tf
from deepface import DeepFace
import keras
from google.cloud import texttospeech
import os

# Load the pre-trained ASL recognition model (binary-weighted)
asl_model = keras.models.load_model("Real-time-Sign-Language-Recognition-Using-OpenCV-and-Deep-Learning/keras_model.h5")

# Function to detect emotion from a frame using DeepFace
def detect_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'])
        return result['dominant_emotion']
    except Exception as e:
        return None

# Function to predict ASL letter from a frame using the pre-trained ASL model
def predict_asl(frame):
    img = cv2.resize(frame, (64, 64))  # Resize to match the model input
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = np.array(img, dtype='float32') / 255.0  # Normalize

    # Predict the class (ASL letter)
    prediction = asl_model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)

    # Map prediction to actual ASL letter (0=A, 25=Z)
    return chr(predicted_class[0] + 65)

# Function for text-to-speech (Google Cloud)
def text_to_speech(text, output_audio_path):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_audio_path, "wb") as out:
        out.write(response.audio_content)

# Function to process a pre-recorded video
def process_video(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    out = None

    all_detected_letters = ""  # Store all the detected ASL letters

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect emotion from the frame
        emotion = detect_emotion(frame)

        # Predict ASL letter from the frame
        letter = predict_asl(frame)
        if letter:
            all_detected_letters += letter

        # Overlay detected emotion and ASL letter on the frame
        if emotion:
            cv2.putText(frame, f"Emotion: {emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if letter:
            cv2.putText(frame, f"ASL: {letter}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Initialize the video writer if it's not already
        if out is None:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (frame.shape[1], frame.shape[0]))

        out.write(frame)  # Write the frame to the output video

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Use Text-to-Speech for the detected letters and save as an audio file
    if all_detected_letters:
        detected_text = "Detected letters: " + all_detected_letters
        text_to_speech(detected_text, 'output/letter_audio.mp3')
        print(f"Text-to-Speech conversion complete. Audio saved to 'output/letter_audio.mp3'.")

# Main function to run the project
if __name__ == "__main__":
    input_video = "input/input_video.mp4"  # Replace with your pre-recorded video path
    output_video = "output/processed_video.avi"

    # Ensure the output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    # Process the video and output the results
    process_video(input_video, output_video)

    print("Video processing complete. Output saved to:", output_video)
