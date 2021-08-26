import streamlit as st
from encryption import encryption
from decryption import decryption

st.write("""# ENTER THE MESSAGE YOU WANT TO ENCRYPT """)
mssg = st.text_input("")

if mssg:
    st.write("""### YOUR ENCRYPTED MESSAGE""")
    st.write(encryption(mssg))



st.write("""# ENTER THE MESSAGE YOU WANT TO DECRYPT """)
encrptd_mssg = st.text_input(" ")

if encrptd_mssg:
    st.write("""# YOUR DECRYPTED MESSAGE""")
    st.write(decryption(encrptd_mssg))
