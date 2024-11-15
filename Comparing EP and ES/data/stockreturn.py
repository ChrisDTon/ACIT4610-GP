import pandas as pd
import os

def calculate_monthly_returns(file_path):
    df = pd.read_csv(f"data/rawcsv/{file_path}")

    # Parse the 'FormatedTime' column into a datetime object
    df['FormatedTime'] = pd.to_datetime(df['FormatedTime'], format='%d:%B:%Y')

    # Set 'FormatedTime' as the index
    df.set_index('FormatedTime', inplace=True)

    # Sort the data by the date index
    df = df.sort_index()

    # Resample to the month-end and get the closing price for each month
    monthly_prices = df['Close'].resample('M').last()  # Use the last available price for each month

    # Calculate the percentage change from the previous month's closing price
    monthly_returns = monthly_prices.pct_change() * 100  # Multiply by 100 to get percentage

    # Drop the first NaN value (as it has no previous month to compare with)
    monthly_returns = monthly_returns.dropna()

    # Extract the month and year from the index and drop the first month (to match monthly_returns)
    month_year = monthly_prices.index.to_period('M')[1:]  # Drop the first month to match

    # Combine the month-end prices and returns into a DataFrame
    result_df = pd.DataFrame({
        'Month': month_year,
        'Monthly Return (%)': monthly_returns
    })

    return result_df

combined_df = pd.DataFrame()

for file_name in os.listdir("data/rawcsv"):
    # Process only CSV files
    if file_name.endswith('.csv'):
        print(f"Processing {file_name}...")
        
        # Calculate monthly returns for each stock
        stock_df = calculate_monthly_returns(file_name)
       
        # Get stock name from the file path (assuming the file name is the stock ticker)
        stock_name = os.path.splitext(file_name)[0]
        
        # Add the stock's data to the combined DataFrame as a new column
        combined_df[stock_name] = stock_df['Monthly Return (%)']

        
        
       


stock_path = "data/monthlyreturn/monthlyreturnstocks.csv"
 # Export the combined DataFrame to a CSV file
combined_df.to_csv(stock_path, index=True)
print(f"Combined CSV file created: {stock_path}")