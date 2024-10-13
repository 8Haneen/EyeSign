# EyeSign
## An intuitive application meant to bridge the gap between ASL and non-ASL users over Zoom conferencing
Created by Fatima Hazime, Jack Wagner, and Haneen Yahfoufi during Hack Dearborn 3 from October 12-13, 2024 at the University of Michigan-Dearborn

## Mission Statement

The goal of EyeSign is to bridge the gap in communication between ASL and non-ASL users and make Zoom meetings accessible to a wider audience. We aim to improve online communication for users who use ASL, are blind, and are neurodivergent through ASL-to-English translation, emotion recognition, and text-to-voice capabilities to increase accessibility of Zoom meetings for wider audiences.

## Integration

Using a Google Chrome extension, users can set up a meeting hosted by a dummy account that acts as the visual input for the recognition model. Once a user begins to sign, the dummy account will take video input from anyone who starts signing and work on translating into English. One letter at a time, it will write out captions for what the user is signing and, once the phrase is complete, an AI voice will read out the message the user signed.

## Software Overview

**OpenCV**: Gathers video input from the user signing to translate into English

**TensorFlow and Keras**: Libraries which incorporate the cloned repository integrated in the project for ASL recognition to 

**DeepFace**: Library for facial emotion recognition

**Zoom SDK**: Integrated with a Google Chrome extension to allow the user to set up the meeting from their browser and authenticate a connection with the dummy account


## Future Improvements

In the future, we would like to incorporate other technologies such as Recall.ai to improve upon the readings from Zoom users. In its current form, the Zoom SDK requires establshing your own domain and extracting raw data in the form of I420 raw video frames and PCM 16LE raw audio format, require us to encode the data. Using software like Recall.ai can improve upon this functionality.

