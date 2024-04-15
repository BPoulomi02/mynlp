import streamlit as st
from newspaper import Article
import spacy
from spacy import displacy

# Load the spaCy model for named entity recognition
nlp = spacy.load("en_core_web_sm")

st.title("Named Entity Recognition")
status = st.radio("Select Option: ", ('URL', 'Text'))
 


# Input for URL
url_input = st.text_input("Enter the URL:")
# Input for paragraph
paragraph_input = st.text_area("Enter the Paragraph:")

# Button to process URL input
if st.button("Process URL"):  # Changed the button label to be more descriptive
    article = Article(url_input)
    article.download()
    article.parse()
    doc = nlp(article.text)
    displacy.render(doc, style='ent')
    st.markdown(displacy.render(doc, style='ent'), unsafe_allow_html=True)

# Button to process paragraph input
if st.button("Process Paragraph"):  # Changed the button label to be more descriptive
    doc = nlp(paragraph_input)
    displacy.render(doc, style='ent')
    st.markdown(displacy.render(doc, style='ent'), unsafe_allow_html=True)
