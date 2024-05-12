import matplotlib.pyplot as plt

# Define the make_graph function
def make_graph(stock_data, revenue_data, title):
    # Plot stock data
    plt.plot(stock_data['Date'], stock_data['Close'], label='Stock Price')

    # Plot revenue data
    plt.plot(revenue_data['Date'], revenue_data['Revenue'], label='Revenue', linestyle='dashed')

    # Set title and labels
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')

    # Add legend
    plt.legend()

    # Show plot
    plt.show()

# Call the make_graph function
make_graph(tesla_data, tesla_revenue, 'Tesla Stock Data and Revenue')
