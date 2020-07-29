import streamlit as st
import bs4 as bs  
import urllib.request  
import re
from summa import summarizer
from summa import keywords

def main():
    st.title("Wikipedia Summarizer")
    url_topull= st.text_input("Enter the Wikipedia URL to pull - ")
    if url_topull!='':
        scraped_data = urllib.request.urlopen(url_topull)  
        article = scraped_data.read()

        parsed_article=bs.BeautifulSoup(article,'lxml')

        paragraphs = parsed_article.find_all('p')

        article_text = ""

        for p in paragraphs:  
            article_text += p.text
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
        article_text = re.sub(r'\s+', ' ', article_text)
        
        summary=summarizer.summarize(article_text,ratio=0.025)        
        st.markdown("# Summary: ")
        st.write(summary) 
        st.markdown("# Keywords: ")
        st.write(keywords.keywords(article_text,ratio=0.005))   
    
if __name__ == '__main__':
    main()
