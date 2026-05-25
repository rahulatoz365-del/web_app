# 🩺 Skin Disease Classification Web App

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](#)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](#)
[![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white)](#)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](#) 

An AI-powered web application that leverages Deep Learning and Computer Vision to predict and classify various skin diseases from user-uploaded images. 

---

## 📖 Overview

Early detection of skin conditions is crucial for effective medical treatment. This project bridges the gap between machine learning and healthcare by providing an intuitive web interface for a trained Convolutional Neural Network (CNN). 

Users can upload an image of a skin anomaly, and the backend processes the image, feeds it into a pre-trained Keras/TensorFlow model (`skin_disease_model.h5`), and returns an instant diagnostic prediction.

## ✨ Key Features

* **Instant Predictions:** Real-time inference using a trained deep learning model.
* **Image Preprocessing:** Automatically resizes and scales user-uploaded images to match the model's required input dimensions.
* **User-Friendly Interface:** A clean, accessible web UI that allows users to easily upload images and view results.
* **Secure Local Processing:** Images are processed locally on the server without being stored, ensuring data privacy.

---

## 🧠 The Machine Learning Model

The core of this application is the `skin_disease_model.h5` file. 
* **Architecture:** Convolutional Neural Network (CNN) built with Keras/TensorFlow.
* **Input:** RGB images (Resized to `[Insert Image Size, e.g., 224x224]` pixels).
* **Classes:** The model is trained to classify the following skin conditions:
  * 🔹 *[e.g., Melanoma]*
  * 🔹 *[e.g., Basal Cell Carcinoma]*
  * 🔹 *[e.g., Benign Keratosis]*
  * 🔹 *[e.g., Healthy/Normal]*

---

## 🛠️ Technology Stack

* **Backend & API:** Python, [Flask / FastAPI / Streamlit - *keep the one you used*]
* **Machine Learning:** TensorFlow, Keras, NumPy, Pillow (PIL)
* **Frontend:** HTML, CSS, JavaScript *(remove if you used Streamlit)*

---

## 🚀 Getting Started

Follow these instructions to run the application on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/rahulatoz365-del/web_app.git](https://github.com/rahulatoz365-del/web_app.git)
cd web_app

```

### 2. Set Up a Virtual Environment (Highly Recommended)

Creating a virtual environment ensures that the TensorFlow dependencies do not conflict with your system Python packages.

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

Make sure to install the required libraries to run the server and the ML model:

```bash
pip install tensorflow numpy pillow flask

```

*(If you have a `requirements.txt` file, you can simply run: `pip install -r requirements.txt`)*

### 4. Run the Application

Start the local web server:

```bash
python app.py

```

Once the server is running, open your browser and navigate to `http://localhost:5000` (or the port specified in your terminal) to use the app.

---

## ⚠️ Medical Disclaimer

**This application is for educational and research purposes only.** The predictions made by this deep learning model should *not* be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider or dermatologist with any questions you may have regarding a medical condition.
