import streamlit as st
import multi_agent_lib as ma

st.set_page_config(page_title="News Analysis System")
st.title("News Analysis System")

news = st.text_area("Enter news article:", height=200)

if st.button("Start Analysis"):
    with st.spinner("Analyzing news..."):
        st.subheader("News Summary")
        summary = ma.summarize_news(news)
        st.write(summary)

        st.subheader("Sentiment Analysis Result")
        sentiment = ma.analyze_sentiment(summary)
        st.write(sentiment)

        st.subheader("Topic Classification Result")
        topic = ma.classify_topic(summary)
        st.write(topic)

