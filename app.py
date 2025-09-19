# app.py

import gradio as gr
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json

# Load trained model
model = load_model("butterfly_model.h5")

# Load class indices
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)
labels = {v: k for k, v in class_indices.items()}

def predict_species(img):
    """
    Predicts butterfly species from uploaded image.
    """
    # Resize and preprocess
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    pred = model.predict(img_array)
    class_idx = np.argmax(pred, axis=1)[0]
    species = labels[class_idx]

    return species

interface = gr.Interface(
    fn=predict_species,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Predicted Species"),
    title="Butterfly Species Classifier",
    description="Upload an image of a butterfly and the model will predict its species."
)

interface.launch()
