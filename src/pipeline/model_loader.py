import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras import layers, models
import numpy as np
import cv2

class ModelLoader:
    def __init__(self):
        self.model_path="models\washer_defect_model.keras"
    
    def model_loader(self):
        
        self.model=models.load_model(self.model_path)
        print(self.model.summary())
        return self.model

if __name__ == "__main__":
    object=ModelLoader()
    object.model_loader()
        
       