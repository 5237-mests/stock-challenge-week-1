import pandas as pd
import yfinance as yf

def load_stock_data(ticker, start, end):
    """
    Load stock data for a given ticker from Yahoo Finance.
    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)
    :param start: Start date for the data (format: 'YYYY-MM-DD').
    :param end: End date for the data (format: 'YYYY-MM-DD').
    :return: A DataFrame containing the stock data.
    """
    data = yf.download(ticker, start=start, end=end, interval='1d', multi_level_index=False)
    return data
def get_data_yf(ticker, start_date, end_date):
    """
    Fetches historical stock data for a given ticker symbol between specified dates using yfinance.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    start_date (str): The start date in 'YYYY-MM-DD' format.
    end_date (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    pd.DataFrame: A DataFrame containing the stock data with columns for Open, High, Low, Close, Volume, and Adjusted Close.
    """
    df = yf.download(ticker, start=start_date, end=end_date, interval='1d', multi_level_index=False)
    return df
def load_news_data(path):
    """
    Load news data from a CSV file.
    
    Parameters:
    path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: A DataFrame containing the news data.
    """
    df = pd.read_csv(path, parse_dates=['date'])
    return df
def load_stock_data_from_csv(path):
    """
    Load stock data from a CSV file.
    
    Parameters:
    path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: A DataFrame containing the stock data.
    """
    df = pd.read_csv(path)
    df.set_index('Date', inplace=True)
    return df