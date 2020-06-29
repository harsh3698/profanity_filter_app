# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:41:11 2020

@author: harsh
"""
from nudity import Nudity
import streamlit as st
from PIL import Image
import os
st.title("obsenity filter")
def nudity_filter(file):
    nudity = Nudity()
    if nudity.has(file) == True:
        statement = 'image is above obsenity threshold'
        return(nudity.score(file), statement)
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
#uploaded_file = st.file_uploader("Choose a file", type=['txt', 'jpg'])
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    #image  = tf.keras.preprocessing.image.img_to_array(image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    a, m = nudity_filter(uploaded_file)
    st.write(a*100, m)

        
