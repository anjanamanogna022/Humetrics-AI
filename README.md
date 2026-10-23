# Humetrics AI

## Multimodal Workplace Stress & Fatigue Detection System

Humetrics AI is an AI-powered workplace monitoring system designed to detect indicators of **stress and fatigue in real time** using computer vision, deep learning, and facial analysis.

The system combines multiple AI-based approaches to analyze facial characteristics and behavioral indicators while providing personalized feedback through an AI-powered coaching component.

## Key Features

- Real-time facial analysis for stress and fatigue monitoring
- Facial landmark detection using MediaPipe Face Mesh
- Facial emotion analysis using DeepFace
- Deep learning-based fatigue/stress classification
- Swin Transformer model trained using the DAiSEE dataset
- AffectNet-based emotion recognition model
- AI-powered coaching and personalized feedback using the Google Gemini API
- Flask-based web application
- User authentication and tracking
- PDF report generation
- Privacy-focused processing with an emphasis on avoiding storage of raw biometric video

## System Architecture

The system follows a pipeline consisting of:

**User → Camera Input → Facial Landmark Detection → Facial/Emotion Analysis → Deep Learning Models → Stress & Fatigue Assessment → AI Coach / Report**

The application uses multiple computer vision and deep learning components to derive meaningful indicators from facial data and provide the user with feedback.

## Technologies Used

### Programming & Frameworks
- Python
- Flask
- HTML
- CSS
- JavaScript

### Artificial Intelligence & Machine Learning
- PyTorch
- Swin Transformer
- DeepFace
- MediaPipe
- OpenCV
- DAiSEE Dataset
- AffectNet

### Other Tools
- SQLite
- Jupyter Notebook
- Google Gemini API

## Project Structure

```text
Humetrics-AI/
│
├── static/                         # Frontend static files
├── templates/                      # HTML templates
│
├── app.py                          # Main Flask application
├── auth.py                         # Authentication functionality
├── email_utils.py                  # Email-related utilities
├── pdf_utils.py                    # PDF report generation
├── swindmodel.py                   # Swin Transformer implementation
│
├── affectnet_efficientnetb0.ipynb  # AffectNet model development
├── swin-daisee_model.ipynb         # DAiSEE/Swin Transformer development
├── swindmodel.ipynb                # Model experimentation
│
├── affectnet_e.pth                 # Trained AffectNet model
├── swinmodel_d.pth                 # Trained Swin model
├── face_landmarker.task            # MediaPipe facial landmark model
│
└── README.md
```

## Models

### Swin Transformer

A Swin Transformer-based model was trained using the **DAiSEE dataset** for analyzing behavioral indicators associated with stress and fatigue.

### AffectNet / Emotion Recognition

An emotion recognition component was developed using the **AffectNet dataset** and an EfficientNet-based architecture to assist with facial emotion analysis.

### Facial Landmark Detection

MediaPipe Face Landmarker is used to detect facial landmarks and provide facial feature information for further analysis.

## AI Coach

Humetrics AI integrates the **Google Gemini API** to provide an AI-based coaching component. Based on the detected indicators, the system can provide personalized suggestions and feedback to the user.

## Privacy Considerations

The project was designed with privacy in mind. The system focuses on processing facial information for analysis rather than maintaining a continuous archive of raw biometric video.

Sensitive credentials such as API keys are intentionally excluded from the repository.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/priscillab9/Humetrics-AI.git
cd Humetrics-AI
```

### 2. Install dependencies

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file locally and add the required API credentials.

**Do not upload the `.env` file or API keys to GitHub.**

### 4. Run the application

```bash
python app.py
```

Open the local Flask server in your browser.

## Project Objective

The primary objective of Humetrics AI is to explore how **multimodal AI, computer vision, and deep learning** can be applied to workplace well-being by identifying potential indicators of stress and fatigue and providing timely, personalized feedback.

## Project Type

**Academic / Final Year Project**

**Domain:** Artificial Intelligence, Machine Learning, Computer Vision & Generative AI

## Authors

**Anjana Mangona P**

B.Tech – Computer Science & Engineering (Artificial Intelligence & Machine Learning)

## Disclaimer

This project is intended for academic and research purposes. The detected stress or fatigue indicators should not be considered a medical or psychological diagnosis.
