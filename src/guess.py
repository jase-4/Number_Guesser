
import tensorflow as tf 
import cv2
import numpy as np
from src.popup import popup
from src.draw import draw_window


def prepare(number):
    IMG_SIZE = 28
    img_array = cv2.imread(number, cv2.IMREAD_GRAYSCALE)
    inverted_img = cv2.bitwise_not(img_array)
    new_array = cv2.resize(inverted_img,(IMG_SIZE,IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE, 1)

def guess_num():
    model = tf.keras.models.load_model('model/num_model.model')

    if(draw_window()) == False:
        return

    prediction = model.predict([prepare('img/screenshot.jpg')])
    num_predicton = np.argmax(prediction)

    popup(num_predicton)

