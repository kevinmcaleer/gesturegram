import cv2
import pandas as pd
import numpy as np
from os import path

from keras import load_model
model = load_model(path) # open saved model/weights from .h5 file

gesture_names = {0: 'Fist',
                 1: 'L',
                 2: 'Okay',
                 3: 'Palm',
                 4: 'Peace'}

def predict_image(image):
    image = np.array(image, dtype='float32')
    image /= 255
    pred_array = model.predict(image)

    # model.predict() returns an array of probabilities - 
    # np.argmax grabs the index of the highest probability.
    result = gesture_names[np.argmax(pred_array)]
    
    # A bit of magic here - the score is a float, but I wanted to
    # display just 2 digits beyond the decimal point.
    score = float("%0.2f" % (max(pred_array[0]) * 100))
    print(f'Result: {result}, Score: {score}')
    return result, score

camera = cv2.VideoCapture(0)

while camera.isOpened():
    #ret returns True if camera is running, frame grabs each frame of the video feed
    ret, frame = camera.read()
    
    k = cv2.waitKey(10)
    if k == 32: # if spacebar pressed
        frame = np.stack((frame,)*3, axis=-1)
        frame = cv2.resize(frame, (224, 224))
        frame = frame.reshape(1, 224, 224, 3)
        prediction, score = predict_image(frame)