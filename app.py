import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import sklearn

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()  # fo lower_case
    text = nltk.word_tokenize(text)  # tokenization

    # removing special characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words(
                "english") and i not in string.punctuation:  # this code will remove the stopwords and punctuations
            y.append(i)

    # stemmimg
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open("vectorizer.pkl","rb"))
model = pickle.load(open("model.pkl","rb"))


st.title("Email/Spam Classifier")
input_sms = st.text_area("Enter the message")
if st.button("Predict"):

    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vecotorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Disply
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")