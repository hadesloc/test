import streamlit as st
import pandas as pd
import numpy as np

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title("Text Analyzer")
st.subheader("Paste your text below and click 'Analyze'")

text = st.text_area("Paste your text here")

if st.button("Analyze"):
    st.subheader("Word Cloud")

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    st.subheader("Most Common Words")

    # Create a dataframe with the text
    df = pd.DataFrame({'text': text.split()})

    # Get the top 10 most common words
    most_common_words = df['text'].value_counts()[:10]

    # Convert the top 10 words to a list
    most_common_words_list = most_common_words.index.tolist()

    # Convert the top 10 words to a list of tuples
    most_common_words_tuples = [(word, count) for word, count in zip(most_common_words_list, most_common_words)]

    # Create a bar chart
    st.bar_chart(most_common_words)

    st.subheader("Most Common Bigrams")

    # Get the top 10 most common bigrams
    most_common_bigrams = df['text'].value_counts()[:10]

    # Convert the top 10 bigrams to a list
    most_common_bigrams_list = most_common_bigrams.index.tolist()

    # Convert the top 10 bigrams to a list of tuples
    most_common_bigrams_tuples = [(bigram, count) for bigram, count in zip(most_common_bigrams_list, most_common_bigrams)]

    # Create a bar chart
    st.bar_chart(most_common_bigrams)