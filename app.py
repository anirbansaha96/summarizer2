import streamlit as st
import bs4 as bs  
import urllib.request  
import re
from wiki_end import wiki_end

def main():
    st.title("Wikipedia Summarizer")
    url_topull= st.text_input("Enter the Wikipedia URL to pull - ")
    if url_topull!='':
        article_text=get_wiki_data(url_topull)
        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')
        import heapq
        number=st.text_input('How many sentences long do you want your summary to be?')
        if number!='':    
            sent_num = int(number)
            formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
            formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
            sentence_list = nltk.sent_tokenize(article_text)  

            stopwords = nltk.corpus.stopwords.words('english')
            word_frequencies = {}  
            for word in nltk.word_tokenize(formatted_article_text):  
                if word not in stopwords:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1

            maximum_frequncy = max(word_frequencies.values())

            for word in word_frequencies.keys():  
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
            sentence_scores = {}  
            for sent in sentence_list:  
                for word in nltk.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]

            summary_sentences = heapq.nlargest(sent_num, sentence_scores, key=sentence_scores.get)
            summary = ' '.join(summary_sentences)  
            st.markdown("# Summary: ")
            st.write(summary)   
    
if __name__ == '__main__':
    main()
