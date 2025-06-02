import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_vs_returns(merged_df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x='sentiment', 
        y='daily_return', 
        data=merged_df,
        hue='daily_return',   # Optional: Color by return magnitude
        palette='coolwarm',   # Optional: Color palette
        alpha=0.7             # Transparency to reduce overplotting
    )
    plt.axhline(0, color='gray', linestyle='--', linewidth=1)  # Horizontal line at 0% return
    plt.axvline(0, color='gray', linestyle='--', linewidth=1)  # Vertical line at neutral sentiment
    plt.title("Sentiment vs Daily Return")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Daily Return")
    plt.tight_layout()
    plt.show()


# def plot_correlation_heatmap(merged_df):
#     # Select only numeric columns for correlation
#     numeric_cols = ['Close', 'Volume', 'daily_return', 'sentiment']
#     corr_matrix = merged_df[numeric_cols].corr()

#     plt.figure(figsize=(5, 4))
#     sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
#     plt.title('Correlation Heatmap of Stock Data and Sentiment')
#     plt.show()


def plot_correlation_heatmap(df):
    plt.figure(figsize=(8, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

def plot_boxplot_by_sentiment_group(df):
    # Create sentiment groups: Negative, Neutral, Positive
    df['sentiment_group'] = pd.cut(
        df['sentiment'],
        bins=[-1, -0.05, 0.05, 1],
        labels=['Negative', 'Neutral', 'Positive']
    )
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='sentiment_group', y='daily_return', data=df, palette='Set2')
    plt.title("Daily Return by Sentiment Group")
    plt.xlabel("Sentiment Group")
    plt.ylabel("Daily Return")
    plt.tight_layout()
    plt.show()

def plot_joint_regression(df):
    sns.jointplot(
        x='sentiment',
        y='daily_return',
        data=df,
        kind='reg',
        height=8,
        scatter_kws={'alpha':0.5}
    )
    plt.suptitle("Joint Plot: Sentiment vs Daily Return", y=1.02)
    plt.show()

