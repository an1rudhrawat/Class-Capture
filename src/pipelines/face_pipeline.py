import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students



@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    shapePredictor = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    faceRecognition = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, shapePredictor, faceRecognition


def get_face_embeddings(image):
    detector, shapePredictor, faceRecognition = load_dlib_models()

    # detector(image, various no of trials for the given image -> used different angles, zoom etc)
    faces = detector(image, 1)
    encoding = []

    for face in faces:
        shape = shapePredictor(image, face)
        face_descriptor = faceRecognition.compute_face_descriptor(image, shape, 1) # 1 is preprocessing number

        encoding.append(np.array(face_descriptor))

    return encoding


@st.cache_resource
def get_trained_model():
    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))
    if len(X) == 0:
        return 0

    classifier = SVC(kernel = 'linear', probability = True, class_weight = 'balanced')

    try:
        classifier.fit(X, y)
    except ValueError:
        st.warning("Fitting failed!")
    return {'classifier': classifier, 'X': X, 'y' : y}

def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image):
    encodings = get_face_embeddings(class_image)

    detected_student = {}
    num_faces = len(encodings)
    if num_faces == 0: # no face detected:
        # student values, student, length of encoding 
        return {}, [], 0
    model_data = get_trained_model()

    # face exists but no student model available
    if not model_data: 
        return {}, [], num_faces
    
    classifier = model_data['classifier']
    X_train = model_data['X']
    y_train = model_data['y']
    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students) >= 2:
            predicted_id = int(classifier.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])

        student_embeddings = X_train[y_train.index(predicted_id)]

        best_match_score = np.linalg.norm(student_embeddings - encoding)

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True
    return detected_student, all_students, len(encodings)
 