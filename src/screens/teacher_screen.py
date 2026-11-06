import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_home, header_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if st.session_state.get('teacher_login_type', 'login') == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()



def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to home", type = 'secondary', key ='teacher_login_back'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header("Login using password", text_alignment='center')
    st.space()
    teacher_username = st.text_input("Enter username", placeholder="John Doe")
    teacher_password = st.text_input("Enter password", type = 'password', placeholder='Enter Password')
    st.divider()

    btnc1, btnc2 = st.columns(2)
    with btnc1:
        if st.button('Login', width='stretch'):
            st.warning('Teacher login is not connected yet.')
    with btnc2:
        if st.button('Register', width='stretch', type='primary'):
            st.session_state.teacher_login_type = 'register'


# def teacher_screen_register():
#     c1, c2 = st.columns(2, vertical_alignment='center')

#     with c1:
#         header_dashboard() 
#     with c2:
#         if st.button("Go Back to home", type = 'secondary', key ='homebtn'):
#             st.session_state.teacher_login_type = None
#             st.rerun()

#     st.header("Register you teacher profile")
#     st.space()
#     teacher_username = st.text_input(
#         "Enter username",
#         placeholder="johndoe",
#         key="teacher_reg_username"
#     )

#     teacher_name = st.text_input(
#         "Enter name",
#         placeholder="John Doe",
#         key="teacher_reg_name"
#     )

#     teacher_password = st.text_input(
#         "Enter password",
#         type="password",
#         placeholder="Enter Password",
#         key="teacher_reg_password"
#     )

#     teacher_password_confirm = st.text_input(
#         "Confirm password",
#         type="password",
#         placeholder="Enter Password",
#         key="teacher_reg_confirm_password"
#     )
#     st.divider()
    
#     btnc1, btnc2 = st.columns(2)
#     with btnc1:
#         st.button('Register', width='stretch')
#     with btnc2:
#         if st.button('Login', width='stretch'):
#             st.session_state.teacher_login_type = 'login'


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='teacher_register_back'):
            st.session_state['login_type'] = None
            st.rerun()



    st.header('Register your teacher profile')

    st.space()
    st.space()

    
    teacher_username = st.text_input("Enter username", placeholder='ananyaroy')

    teacher_name = st.text_input("Enter name", placeholder='Ananya Roy')

    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

    teacher_pass_confirm = st.text_input("Confirm your password", type='password', placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Register", width='stretch'):
            st.warning('Teacher registration is not connected yet.')


    with btnc2:
        if st.button('Login Instead', type="primary", icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'login'

