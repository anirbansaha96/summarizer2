import streamlit
value = streamlit.text_input("Write a Text")
streamlit.write("You Wrote : ", value)