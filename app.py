import streamlit as st
import pandas as pd
from PIL import Image
from os import path
from wordcloud import WordCloud
import numpy as np


# Header section
Header_html = """
    <style>
        @keyframes slide_in {
            from {
                margin-left: 100%;
                width: 300%    
            }
            to {
                margin-right: 0%;
                width: 100%  
            }
        }
        
        .title h1 {
            text-align: center;
            color: #6C9ADC;
            font-size: 40px;
            text-shadow: 2px 2px #ABCCFC;
            animation-duration: 4s;
            animation-name: slide_in;  
        }
        .title h2 {
            text-align: center;
            font-style : italic;
            font-size: 20px;
            animation-duration: 4s;
            animation-name: slide_in;
        }
    </style>
    <div class="title"> 
        <h1>WordCloud Generator</h1>
        <h2>fill in the needed information in the sidebar and let us do the rest !</h2>       
    </div>
"""
st.markdown(Header_html, unsafe_allow_html=True)
st.markdown("____")

# empty slot to use later for the wordcloud
empty_place = st.empty()

# User input
st.sidebar.markdown("<h1 style='font-weight: bold; text-align: center'>Configurations</h1>",
                    unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='font-size: 15px; text-align: center; font-style: italic'>"
                    "Customize your wordcloud until you are satisfied !</h2>", unsafe_allow_html=True)
st.sidebar.markdown("____")
# color palette for background and text
st.sidebar.markdown("<h2 style='font-style: italic; font-size: medium'>"
                    "Pick a color for the background of your wordcloud</h2>", unsafe_allow_html=True)
bc = st.sidebar.color_picker(" ", value='#FFFFFF')
st.sidebar.markdown("<h2 style='font-style: italic; font-size: medium'>"
                    "Do you want for the words in your cloud to have a specific color ?</h2>", unsafe_allow_html=True)
text_color = st.sidebar.radio(" ", ["Yes", "No"])
if text_color == "Yes":
    st.sidebar.markdown("<h2 style='font-style: italic; font-size: medium'>Pick a color for your text</h2>",
                        unsafe_allow_html=True)
    c = st.sidebar.color_picker(" ")
    val = True
else:
    val = False

# color palette for contour
st.sidebar.markdown("----")
st.sidebar.markdown("<h2 style='font-style: italic; font-size: medium'>Choose the height in px</h2>",
                    unsafe_allow_html=True)
wid = st.sidebar.slider("Width", 0, 400, 1000)
st.sidebar.markdown("<h2 style='font-style: italic; font-size: medium'>Choose the height in px</h2>",
                    unsafe_allow_html=True)
hei = st.sidebar.slider("Height", 0, 400, 1000)

# Choosing between mask or no mask :
l = pd.DataFrame({'l': ['Simple', 'Shaped']})
st.sidebar.markdown(
    "<h2 style='font-style: italic; font-size: medium'>Do you want your wordcloud to have a certain shape?"
    "</h2>", unsafe_allow_html=True)
logo = st.sidebar.selectbox(" ", l)
if logo == 'Shaped':
    contour = st.sidebar.radio("Do you want your cloud to have a contour? ", ["Yes", "No"])
    if contour == "Yes":
        cd = 0.5
        cd_c = st.sidebar.color_picker("Pick a color for your contour")
    else:
        cd = 0.0
        cd_c = None

t = pd.DataFrame({'s': ['enter a text', 'upload a file']})

# text input
st.sidebar.markdown(
    "<h2 style='font-style: italic; font-size: medium'>how do you want to submit the text ?"
    "</h2>", unsafe_allow_html=True)
Place_holder = st.sidebar.selectbox(" ", t)
if Place_holder == 'enter a text':
    txt = st.sidebar.text_area("enter your text here")
else:
    #  fichier = st.sidebar.file_uploader('test',type='txt',accept_multiple_files=False)
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    try:
        txt = uploaded_file.getvalue().decode("utf-8")
    except AttributeError:
        txt = ''
        st.markdown("<h3 style='font-style: italic; text-align: center'>please upload a text file</h3>",
                    unsafe_allow_html=True)
    except UnicodeDecodeError:
        st.markdown("<h3 style='font-style: italic; text-align: center'>Wrong file format!"
                    " We only accept files with a .txt extension !"
                    "</h3>",unsafe_allow_html=True)
        txt = ''
try:
    if len(txt) == 0:
        raise ValueError("Empty text")
except ValueError:
    ''
else:
    ma = np.array(Image.open(path.join("inpt.png")))
    if val is True and logo == 'Shaped':
        word = WordCloud(width=wid, height=hei, margin=0, background_color=bc, mask=ma, contour_width=cd,
                         color_func=lambda *args, **kwargs: c, contour_color=cd_c).generate(txt)
    elif val is False and logo == 'Shaped':
        word = WordCloud(width=wid, height=hei, margin=0, background_color=bc, mask=ma, contour_width=cd,
                         contour_color=cd_c).generate(txt)
    elif val is False and logo == 'Simple':
        word = WordCloud(width=wid, height=hei, margin=0, background_color=bc).generate(txt)
    else:
        word = WordCloud(width=wid, height=hei, margin=0, background_color=bc,
                         color_func=lambda *args, **kwargs: c).generate(txt)
    word.to_file('wordcld.png')
    st.markdown("\n__Here is your wordcloud :__")
    image = Image.open('wordcld.png')
    st.image(image, caption='Your customized wordcloud')
    st.markdown("____")
    
# About Us Section
information = st.beta_expander("About Us", False)
information_html = """
    <style>
    div {
        font-family: "Gill Sans", sans-serif; 
        font-size: medium;
        color: #92B2DF;
    }
    img {
        float: right;
    }
    </style>
    <div>We are INPT first year students :
        <ul>
            <li><a>Chadli Wiam</a></li>
            <li><a>Zoufir Zineb</a></li>
            <li><a>Hammani Latifa</a></li>
            <li><a>Allam Laila</a></li>
            <li><a>Laaqira Chaima</a></li>
        </ul>
    </div>
    <img src='https://upload.wikimedia.org/wikipedia/commons/9/9a/Logo_inpt.PNG' alt='Logo Inpt' width='250 height='150' style='margin-top:10px; margin-bottom: 10px'>
    <a href='https://github.com/WiamChadli00/ProjetPythonSouissi.git' target='_blank' title='Github Page' style='color: #EE057A; text-decoration: None'>
    Click here to view our web app's code! </a>
"""
information.markdown(information_html, unsafe_allow_html=True)
