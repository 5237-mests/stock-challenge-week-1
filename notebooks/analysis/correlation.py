import pandas as pd
def merge_and_correlate(stock_df, news_df):
    news_daily = news_df.groupby('date')['sentiment'].mean().reset_index()
    merged = pd.merge(stock_df, news_daily, left_on='Date', right_on='date')
    correlation = merged['daily_return'].corr(merged['sentiment'])
    return merged, correlation
