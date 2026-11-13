# ClassCapture – AI-Powered Attendance Management System

ClassCapture is an AI-assisted attendance management system that automates classroom attendance using **facial recognition and voice recognition**. Built with Python and Streamlit, it provides separate portals for teachers and students, making attendance tracking and classroom management more efficient.

## Overview

Traditional attendance-taking is time-consuming, particularly in classrooms with a large number of students. ClassCapture addresses this by using biometric recognition techniques to identify students and record their attendance.

Teachers can manage subjects, view enrolled students, and process attendance, while students can register, enroll in subjects, and access their dashboard.

## Features

### 1. Facial Recognition
- Detects faces from classroom images.
- Extracts 128-dimensional facial embeddings using Dlib.
- Uses a Support Vector Machine (SVM) classifier for student identification.
- Compares facial embeddings to verify recognition.

### 2. Voice Recognition
- Extracts speaker embeddings using a pretrained Resemblyzer model.
- Uses Librosa for audio loading, preprocessing, and segmentation.
- Compares voice embeddings using cosine similarity.
- Identifies registered students based on voice similarity scores.

### 3. Student Portal
- Student registration using facial and voice information.
- Face-based student identification.
- Subject enrollment using subject codes.
- Student dashboard displaying enrolled subjects and attendance information.

### 4. Teacher Portal
- Teacher registration and login.
- Subject creation and management.
- Student enrollment management.
- Facial and voice-based attendance processing.
- Attendance records and summaries.

### 5. Subject Enrollment
- Generates QR codes for subject enrollment.
- Allows students to join subjects using enrollment codes.
- Checks existing enrollment to prevent duplicate entries.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / UI | Streamlit |
| Database | Supabase |
| Face Detection & Recognition | Dlib, Face Recognition Models |
| Machine Learning | Scikit-learn, SVM |
| Voice Recognition | Resemblyzer |
| Audio Processing | Librosa |
| Image Processing | Pillow, NumPy |
| Data Processing | Pandas |
| Authentication | Bcrypt |
| QR Code Generation | Segno |

## System Workflow

### Facial Recognition Pipeline

1. Capture or upload a classroom image.
2. Detect faces using Dlib.
3. Extract facial landmarks.
4. Generate 128-dimensional facial embeddings.
5. Classify detected faces using the trained SVM model.
6. Verify the predicted identity using embedding distance.
7. Record the identified students' attendance.

### Voice Recognition Pipeline

1. Record classroom audio.
2. Load and preprocess the audio using Librosa.
3. Separate non-silent audio segments.
4. Extract speaker embeddings using Resemblyzer.
5. Compare the extracted embeddings with registered student embeddings.
6. Calculate cosine similarity scores.
7. Identify matching students and process attendance.

## Installation and Setup

### Prerequisites

- Python installed on your system.
- Git.
- A Supabase project.

### 1. Clone the Repository

```bash
git clone https://github.com/an1rudhrawat/Class-Capture.git
```

Navigate to the project directory:

```bash
cd Class-Capture
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Some audio and face-recognition dependencies include native components. Their installation may require compatible Python versions or additional build tools.

### 4. Configure Supabase

Create a Supabase project and obtain your project URL and publishable API key.

Create a `.streamlit` directory in the project root if it does not already exist.

Inside it, create a file named `secrets.toml`:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_publishable_key"
```

Ensure that your Supabase database contains the tables and columns expected by the application.

**Important:** Never commit `secrets.toml` or expose your database credentials publicly.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## Project Structure

The application is organized into separate modules for its user interface, database operations, reusable components, and recognition pipelines.

```text
Class-Capture/
│
├── app.py
├── requirements.txt
│
├── .streamlit/
│   └── secrets.toml
│
└── src/
    ├── ui
        ├──base_layout.py 
    ├── components/
    │   ├── Subject cards and dialogs
    │   └── Reusable UI components
    │
    ├── database/
    │   ├── config.py
    │   └── db.py
    │
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    │
    └── screens/
        ├── home_screen.py
        ├── teacher_screen.py
        └── student_screen.py


## Important Notes

- Facial and voice recognition depend on the quality of registered biometric samples and the recording environment.
- Similarity thresholds should be calibrated using representative classroom data.
- Voice segmentation based on silence does not provide full speaker diarization.
- Biometric information is sensitive. Obtain appropriate consent, restrict database access, and implement suitable security and retention policies before using the application with real students.

## Future Improvements

- Improve recognition accuracy under varying classroom conditions.
- Introduce more robust speaker diarization for overlapping classroom conversations.
- Add detailed attendance analytics and reporting.
- Improve biometric data security and access control.
- Optimize recognition performance for larger classrooms.
