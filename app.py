import streamlit as st


def main():
    st.title("Question Answering POC")
    Question= st.text_input("Please Input the Question")
    if Question!='':
        st.write("The Answer to : \n ", Question)
        st.write("\n\n The Correct Answer")

if __name__ == '__main__':
    main()
