import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_crypto_data(file_path):
    """
    Analyze cryptocurrency price data and visualize correlations.

    Args:
        file_path (str): Path to the CSV file containing price data.
    """
    # Load the data
    data = pd.read_csv(file_path, index_col='timestamp', parse_dates=True)
    print("Data loaded successfully!")
    print("First few rows of the data:")
    print(data.head())
    print("Data info:")
    print(data.info())

    # Data cleaning
    # Drop duplicate timestamps
    data = data[~data.index.duplicated(keep='first')]

    # Fill missing values using interpolation
    data = data.interpolate(method='time')

    # Drop rows with remaining NaN values after interpolation
    data = data.dropna()

    # Ensure there is sufficient data after cleaning
    if data.empty:
        print("No valid data available after cleaning. Exiting...")
        return

    # Calculate daily percentage change
    returns = data.pct_change(fill_method=None).dropna()

    # Compute the correlation matrix
    correlation_matrix = returns.corr()
    print("Correlation matrix calculated:")
    print(correlation_matrix)

    # Plot the correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
    plt.title('Cryptocurrency Price Correlations')
    plt.tight_layout()

    # Save the heatmap to the correct directory
    output_path = r'C:\Users\Mohsen\Desktop\Desktop\AI\crypto-correlation-dashboard\data\correlation_heatmap.png'
    plt.savefig(output_path)
    print(f"Heatmap saved to {output_path}")
    plt.show()


# Run the analysis
file_path = r'C:\Users\Mohsen\Desktop\Desktop\AI\crypto-correlation-dashboard\data\crypto_prices.csv'
analyze_crypto_data(file_path)
