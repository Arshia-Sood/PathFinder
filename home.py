import streamlit as st 
import base64
from streamlit_option_menu import option_menu
from views import Free_Chat,Quiz_Mode,Career_Roadmap,Resume

st.set_page_config(page_title="Path Finder",layout="wide")

def add_background(image_url):
    with open(image_url,"rb") as f:
        encoded=base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp{{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: 1400px 700px;
            background-position: center,center;
            background-repeat: no-repeat;
            background-attachment: local;
        }}
        </style>
        """,unsafe_allow_html=True)
    
add_background("background3.jpg")

st.markdown(
    """
    <h1 style='text-align: center;
            color: black;
            font-size: 45px;
            font-weight: bold;'>
            Path Finder
    </h1>
    """,
    unsafe_allow_html=True)

st.markdown(
    """
    <h2 style='text-align: center;
            color: #CD7F32;
            font-size: 24px;
            font-weight: italic;
            margin-top: -10px;'>
            Choose your path with confidence.
    </h2>
    """,
    unsafe_allow_html=True
)


selected=option_menu(
    menu_title=None,
    options=["Free Chat","Career Roadmap","Quiz Mode","Resume Reviewer"],
    icons=["chat","map","question-circle","bi-search-heart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "5px", "background-color": "#947070"},
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link":{
            "color":"black",
            "font-size":"18px",
            "text-align":"left",
            "margin":"5px",
        },
        "nav-link-selected":{
            "background-color":"#f0f0f0",
            "color":"black",
        }
    }
)


if selected == "Free Chat":
    Free_Chat.main()

elif selected == "Career Roadmap":
    Career_Roadmap.main()

elif selected == "Quiz Mode":
    Quiz_Mode.main()

elif selected== "Resume Reviewer":
    Resume.main()