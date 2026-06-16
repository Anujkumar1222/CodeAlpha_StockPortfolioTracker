import csv
from datetime import datetime

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 170
}

portfolio = {}
total_value = 0

print("\n===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

print("\n===== PORTFOLIO SUMMARY =====")
for stock, quantity in portfolio.items():
    value = quantity * stock_prices[stock]
    total_value += value
    print(f"{stock} | Qty: {quantity} | Price: ${stock_prices[stock]} | Value: ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Save to CSV
filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Value"])

    for stock, quantity in portfolio.items():
        writer.writerow([
            stock,
            quantity,
            stock_prices[stock],
            quantity * stock_prices[stock]
        ])

    writer.writerow([])
    writer.writerow(["TOTAL", "", "", total_value])

print(f"\nPortfolio saved successfully as {filename}")