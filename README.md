# 🩺 Skin Disease Classification Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](#)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](#)
[![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](#)

An AI-powered web application built with Streamlit that leverages Deep Learning and Computer Vision to predict and classify various skin diseases from user-uploaded images.

---

## 📖 Overview

Early detection of skin conditions is crucial for effective medical treatment. This project bridges the gap between machine learning and healthcare by providing an intuitive, interactive web interface powered by Streamlit for a trained Convolutional Neural Network (CNN). 

Users can upload an image of a skin anomaly, and the application processes the image, feeds it into a pre-trained Keras/TensorFlow model (`skin_disease_model.h5`), and displays an instant diagnostic prediction with confidence intervals directly in the browser.

## ✨ Key Features

* **Instant Predictions:** Real-time, server-side inference using a trained deep learning model.
* **Interactive UI:** A highly responsive dashboard built entirely in Python using Streamlit's file-uploader and layouts.
* **Image Preprocessing:** Automatically resizes and scales user-uploaded images to match the model's required input dimensions.
* **Secure Local Processing:** Images are processed locally on the runtime environment without being permanently stored, ensuring user data privacy.

---

## 🧠 The Machine Learning Model

The core of this application is the `skin_disease_model.h5` file. 
* **Architecture:** Convolutional Neural Network (CNN) built with Keras/TensorFlow.
* **Input:** RGB images (Resized to match the model's expected input shape).
* **Classes:** The model is trained to classify multiple skin conditions:
  * 🔹 *[e.g., Melanoma]*
  * 🔹 *[e.g., Basal Cell Carcinoma]*
  * 🔹 *[e.g., Benign Keratosis]*
  * 🔹 *[e.g., Healthy/Normal]*

---

## 🛠️ Technology Stack

* **Frontend & Backend Framework:** Streamlit (Python-native web framework)
* **Machine Learning & Vision:** TensorFlow, Keras, NumPy, Pillow (PIL)

---

## 🚀 Getting Started

Follow these instructions to run the application on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/rahulatoz365-del/web_app.git](https://github.com/rahulatoz365-del/web_app.git)
cd web_app

```

### 2. Set Up a Virtual Environment (Highly Recommended)

Creating a virtual environment ensures that your machine learning dependencies stay isolated and organized.

```bash
# Create the environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

Install the required libraries to run both the Streamlit web interface and the underlying ML model:

```bash
pip install tensorflow numpy pillow streamlit

```

### 4. Run the Streamlit App

Instead of standard script execution, launch the application using the Streamlit CLI:

```bash
streamlit run app.py

```

Once initialized, Streamlit will automatically open your local browser to `http://localhost:8501`.

---

## ⚠️ Medical Disclaimer

**This application is for educational and research purposes only.** The predictions made by this deep learning model should *not* be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider or dermatologist with any questions you may have regarding a medical condition.
