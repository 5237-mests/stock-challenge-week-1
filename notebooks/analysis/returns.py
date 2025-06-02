def calculate_daily_returns(stock_df):
    stock_df['daily_return'] = stock_df['Close'].pct_change()
    return stock_df
