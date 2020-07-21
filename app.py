import streamlit as st


def main():
    st.title("Question Answering POC")
    Question= st.text_input("Please Input the Question")
    if Question=='Who am I?':
        st.write("The Answer to : \n ", Question)
        st.write("\n\n Anirban Saha")

if __name__ == '__main__':
    main()
