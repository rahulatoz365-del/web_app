import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow_hub as hub  # <-- New import
import numpy as np
from PIL import Image

# --- DEFINE YOUR CUSTOM COLAB LAYER ---
class HubLayer(tf.keras.layers.Layer):
    # Added a default model_url so Keras doesn't crash when loading the saved file
    def __init__(self, model_url="https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4", **kwargs):
        super(HubLayer, self).__init__(**kwargs)
        self.hub_layer = hub.KerasLayer(
            model_url,
            trainable=False
        )
    def call(self, inputs, training=None):
        return self.hub_layer(inputs, training=training)
# --------------------------------------

# 1. Page Configuration
st.set_page_config(page_title="Skin Disease Classifier", layout="centered")
st.title("🩺 Skin Disease Classification App")
st.write("Upload an image of the affected skin area, and the model will predict the condition.")

# 2. Load the model (Cached for performance)
@st.cache_resource
def load_my_model():
    # <-- Pass custom_objects so Keras knows how to read your HubLayer
    model = load_model(
        'skin_disease_model.h5', 
        custom_objects={'HubLayer': HubLayer, 'KerasLayer': hub.KerasLayer}
    )
    return model

model = load_my_model()

# 3. Your exact class names from Colab
class_names = [
    'BA- cellulitis', 'BA-impetigo', 'Eczema', 'FU-athlete-foot', 
    'FU-nail-fungus', 'FU-ringworm', 'Melanoma', 'Monkeypox', 
    'Nail_psoriasis', 'PA-cutaneous-larva-migrans', 'SJS-TEN', 
    'VI-chickenpox', 'VI-shingles', 'Vitiligo', 'acne', 'hyperpigmentation'
] 

# 4. File Uploader
uploaded_file = st.file_uploader("Choose a skin image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    st.write("Analyzing...")

    # 5. Preprocess the image to match MobileNetV2 input
    img = image.resize((224, 224)) 
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  
    
    # 6. Make Prediction
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    confidence = np.max(predictions) * 100
    predicted_disease = class_names[predicted_class_index]
    
    # 7. Show Results
    st.success(f"**Prediction:** {predicted_disease}")
    st.info(f"**Confidence:** {confidence:.2f}%")