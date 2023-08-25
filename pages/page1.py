import streamlit as st
import requests
import numpy as np

import streamlit as st

st.write('This is page 1')

#api_key='1KMPHCBIOe3hOjJwCJQX49sRc6cM0oIm'

url='https://api.giphy.com/v1/gifs/search'

if st.button('click me ;)'):
    st.image('raw_data/le_wagon.png')

query=st.text_input('Search a GIF')
params={'api_key':st.secrets.api_key,'q':query,'limit':10}

response=requests.get(url=url,params=params).json()

while not query:
    st.stop()

gif_url=response['data'][np.random.randint(0,10)]['embed_url']

st.write(
    f'<iframe src="{gif_url}" width="480" height="240">',
    unsafe_allow_html=True,
)
