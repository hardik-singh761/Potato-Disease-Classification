import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

# Load your trained model
model = load_model("saved_models/1.keras")

# Update based on how you trained the model
class_names = [
    "Potato - Early_blight",
    "Potato - Late_blight",
    "Potato - Healthy"
]

IMAGE_SIZE = (256, 256)

def predict(image_bytes):
    # Convert bytes to image
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMAGE_SIZE)

    # Convert to numpy array and expand dims
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch

    # Make prediction
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = round(100 * np.max(predictions[0]), 2)

    return predicted_class, confidence
