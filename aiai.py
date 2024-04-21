import streamlit as st
st.title("Ai detector")
text_area=st.text_area("Enter ur text");
if text_area is not None:
    if st.button("anylize"):
        st.write("welcome")