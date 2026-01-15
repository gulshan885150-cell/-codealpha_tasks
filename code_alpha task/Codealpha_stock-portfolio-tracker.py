# Manually defined stock prices (per share)
stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 320,
    "TSLA": 250
}

# User's stock holdings (shares owned)
portfolio = {
    "AAPL": 10,
    "GOOGL": 5,
    "MSFT": 8,
    "TSLA": 4
}

def calculate_portfolio_value(prices, holdings):
    total_value = 0

    print("📈 Stock Portfolio Summary")
    print("-" * 35)

    for stock, shares in holdings.items():
        if stock in prices:
            value = prices[stock] * shares
            total_value += value
            print(f"{stock}: {shares} shares × ${prices[stock]} = ${value}")
        else:
            print(f"{stock}: Price not available")

    print("-" * 35)
    print(f"💰 Total Portfolio Value: ${total_value}")

calculate_portfolio_value(stock_prices, portfolio)