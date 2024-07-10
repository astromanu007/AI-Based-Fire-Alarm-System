import cv2
import tensorflow as tf
import numpy as np
import requests

# Load the trained model
model = tf.keras.models.load_model('fire_detection_model.h5')

# Initialize camera
cap = cv2.VideoCapture(0)  # Change the index if you have multiple cameras

def preprocess_frame(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    frame = np.expand_dims(frame, axis=0)
    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        break

    preprocessed_frame = preprocess_frame(frame)
    prediction = model.predict(preprocessed_frame)
    
    if prediction > 0.5:
        cv2.putText(frame, 'Fire Detected!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        requests.get('http://<ESP8266_IP>/light_on')  # Replace <ESP8266_IP> with the actual IP address
    else:
        cv2.putText(frame, 'Conditions Normal', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        requests.get('http://<ESP8266_IP>/light_off')  # Replace <ESP8266_IP> with the actual IP address
    
    cv2.imshow('Fire Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
