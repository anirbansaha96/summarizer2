import streamlit as st
from transformers import pipeline
summarizer = pipeline("summarization")

def main():
    st.title("Summarizer")
    article_text= st.text_input("Please Input the Article To Summarize")
    if article_text!='':
        summary=summarizer(article_text, max_length=130, min_length=30)
        st.write("The Summary is : \n ", summary)
        
if __name__ == '__main__':
    main()
