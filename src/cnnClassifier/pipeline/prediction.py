import numpy as np 
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os
from pathlib import Path

# Project root (same repo as training pipeline)
ROOT = Path(__file__).resolve().parent.parent.parent.parent

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load the same model the pipeline trains (artifacts/training/trained_model.h5)
        model_path = ROOT / "artifacts" / "training" / "trained_model.h5"
        if not model_path.exists():
            model_path = ROOT / "model" / "model.h5"  # fallback
        model = load_model(str(model_path))

        # Load image (absolute path = where decodeImage wrote it, usually cwd)
        imagename = os.path.abspath(self.filename)
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0

        preds = model.predict(test_image, verbose=0)
        result = np.argmax(preds, axis=1)
        print("Prediction probabilities:", preds[0].tolist(), "-> class index:", int(result[0]))
        
        if result[0] == 1:
            prediction='Tumor'
            return [{"image": prediction}]
            
        else:
            prediction='Normal'
            return [{"image": prediction}]
        
        
        
