import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("Student")
        st.image("student_img_2.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:'):
            st.session_state['login_type']='Student'
            st.rerun()

    with col2:
        st.header("Teacher")
        st.image("teacher_img.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:'):
            st.session_state['login_type']='Teacher'
            st.rerun()

    # footer_home()