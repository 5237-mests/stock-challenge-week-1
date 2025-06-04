# from textblob import TextBlob

# def get_sentiment(text):
#     return TextBlob(text).sentiment.polarity

# def add_sentiment_column(news_df):
#     news_df['sentiment'] = news_df['headline'].apply(get_sentiment)
#     return news_df

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    return sia.polarity_scores(text)['compound']  # compound is a summary score

def add_sentiment_column(news_df):
    news_df['sentiment'] = news_df['headline'].apply(get_sentiment)
    return news_df
