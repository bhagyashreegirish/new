import streamlit as st

def main():
    st.title("Company News Sentiment Analysis")
    
    company_name = st.text_input("Enter Company Name")
    
    if company_name:
        articles = get_news_articles(company_name)
        
        sentiments = []
        for article in articles:
            sentiment = analyze_sentiment(article['summary'])
            sentiments.append(sentiment)
        
        comparative_analysis = comparative_sentiment_analysis(sentiments)
        
        # Display results
        for i, article in enumerate(articles):
            st.write(f"**{article['title']}**")
            st.write(f"Summary: {article['summary']}")
            st.write(f"Sentiment: {sentiments[i]}")
        
        st.write(f"Comparative Sentiment Analysis: {comparative_analysis}")
        
        # Generate TTS report
        report_text = f"Comparative Sentiment Analysis: {comparative_analysis}"
        tts_filename = generate_tts_report(report_text)
        st.audio(tts_filename)
        
if __name__ == "__main__":
    main()
