#pip install -q -U google-generativeai
#pip install ipython
#pip install pillow
#PIP INSTALL STREAMLIT
import streamlit as st
from PIL import Image
import google.generativeai as genai

api = st.text_input('put your api')

API = api

genai.configure(api_key=API)

models = st.selectbox('seletc your model' , ['gemini-pro-vision','gemini-pro'])
model = genai.GenerativeModel(models)

if models == "gemini-pro-vision":
    imageupload = st.file_uploader('upload your image')
    if imageupload:
        pr = st.text_input('Your Prompt here' , value='Write a prompt for me to create an image like this')
        img = Image.open(imageupload)
        response = model.generate_content(['Write a prompt for me to create an image like this' , img])
        st.subheader('Your Image 👇')
        st.image(img)
        st.subheader('Your Prompt to Have Image Like This ☝️️')
        st.write(response.text)

elif models == "gemini-pro":
    inp = st.text_area('write your prompt')
    bt = st.button('Lets Go')
    if inp != "" and bt:
        response = model.generate_content(inp)
        st.write(response.text)








