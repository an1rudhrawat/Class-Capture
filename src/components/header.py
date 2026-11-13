import streamlit as st


def header_home():
    st.header("Class Capture")

def header_dashboard():

    logo_url = "https://th.bing.com/th/id/OIP.GjHfHrgJy99y_ll2dS0hEgHaHa?w=200&h=200&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:red'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)