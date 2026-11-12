import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.db import get_enrolled_students
from datetime import datetime
import pandas as pd
from src.components.attendance_result_dialog import show_attendance_results

@st.dialog("Voice attendance")
def voice_attendance_dialog(subject_id):
    st.write("Record audio of students saying I am present")

    audio_data = st.audio_input("Record classroom audio")

    if st.button("Analyze Audio", width='stretch', type='primary'):

        if audio_data is None:
            st.warning("Please record audio first")
            return

        with st.spinner("Analyzing ..."):
            enrolled_response = get_enrolled_students(subject_id)
            enrolled_students = enrolled_response.data

            if not enrolled_students:
                st.warning("No students enrolled in this course")
                return

            candidates_dict = {
                i['students']['student_id'] : i['students']['voice_embedding']
                for i in enrolled_students if i['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.error("No enrolled students have voice profiles registered")
                return

            audio_bytes = audio_data.read()
            detected_score = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log = [], []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            
            for node in enrolled_students:
                student = node['students']
                score = detected_score.get(student['student_id'], 0.0)
                is_present = bool(score > 0)
                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Source": score if is_present else "-",
                    "Status": "Present" if is_present else "Absent"
                })

                attendance_to_log.append({
                    "student_id": student["student_id"],
                    "subject_id": subject_id,
                    "timestamp": current_timestamp,
                    "is_present": bool(is_present)
                })
            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)
    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_results(df_results, logs)



