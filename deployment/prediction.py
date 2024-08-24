import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from keras.models import load_model 

# Load the TensorFlow model
model = load_model('best_model.h5')

class_names = ['Wayang Beber', 'Wayang Gedog', 'Wayang Golek', 'Wayang Krucil', 'Wayang Kulit', 'Wayang Suluh']

def predict_from_file(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(400, 400))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_batch = img_batch / 255.0
    prediction_inf = model.predict(img_batch)
    result_max_proba = prediction_inf.argmax(axis=-1)[0]
    result_class = class_names[result_max_proba]
    return prediction_inf, result_class

def run():
    st.title("Identify Your Emotion")
    uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg'])
    if uploaded_file is not None:
        prediction, result_class = predict_from_file(uploaded_file)
        st.write('Prediction result is:', result_class)
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

if __name__ == '__main__':
    run()