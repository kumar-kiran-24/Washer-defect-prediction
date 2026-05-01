import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras import layers, models
import numpy as np
import cv2
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from src.pipeline.model_loader import ModelLoader

class Predictor:
    def __init__(self):\
        self.model_loader = ModelLoader()
        
    def predict_image(self, img_path):
        model=self.model_loader.model_loader()
        labels = ['defective', 'non-defective']
        # img = load_img(img_path, target_size=(224,224))
        # img_array = img_to_array(img)
        
        img = load_img(img_path, target_size=(224,224))
        img_array = img_to_array(img)


       
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)

        # ----------------------------
        # PREDICT
        # ----------------------------
        pred = model.predict(img_array)

        print("Raw Output:", pred)

        idx = np.argmax(pred[0])
        confidence = pred[0][idx] * 100

        print("Prediction:", labels[idx])
        print("Confidence:", round(confidence,2), "%")
        
        return labels[idx]

if __name__=="__main__":
    predictor = Predictor(model=None)
    predictor.predict_image(r"C:\ml\washer_defect_predctor\Screenshot 2026-04-27 142636.png")

    
    
