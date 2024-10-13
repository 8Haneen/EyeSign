from flask import Flask, request, jsonify
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load your ASL recognition model
model = tf.keras.models.load_model('models/asl_model.h5')

@app.route('/translate_asl', methods=['POST'])
def translate_asl():
    # Get the image frame from the request
    img_file = request.files['frame'].read()
    npimg = np.frombuffer(img_file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Preprocess the image and predict the ASL sign
    processed_img = preprocess_frame(img)  # Define preprocessing as needed
    prediction = model.predict(processed_img)
    asl_text = get_sign_from_prediction(prediction)  # Map to ASL label

    return jsonify({"translated_text": asl_text})

# Utility functions for preprocessing and mapping prediction to sign
def preprocess_frame(frame):
    frame_resized = cv2.resize(frame, (64, 64))  # Assuming 64x64 input size
    frame_normalized = frame_resized / 255.0
    return np.expand_dims(frame_normalized, axis=0)

def get_sign_from_prediction(prediction):
    class_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # Update with real labels
    predicted_class = np.argmax(prediction)
    return class_labels[predicted_class]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
