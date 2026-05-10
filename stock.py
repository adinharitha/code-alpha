
stock_prices = {
    "DMART": 180,
    "REALINCE": 250,
    "TATA": 140,
    "STAR HEALTH": 330
}

portfolio = {}
total_investment = 0

# Number of stocks user wants to add
n = int(input("Enter number of stocks: "))

# Taking stock inputs
for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    portfolio[stock_name] = quantity

# Calculating total investment
print("\nPortfolio Summary")
print("---------------------")

for stock, quantity in portfolio.items():
    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock} : {quantity} shares × ${stock_prices[stock]} = ${investment}")
    else:
        print(f"{stock} price not available")

print("---------------------")
print(f"Total Investment Value = ${total_investment}")

# Optional: Save result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("---------------------\n")

    for stock, quantity in portfolio.items():
        if stock in stock_prices:
            investment = stock_prices[stock] * quantity
            file.write(f"{stock} : {quantity} shares = ${investment}\n")

    file.write("---------------------\n")
    file.write(f"Total Investment Value = ${total_investment}")

print("\nPortfolio summary saved to portfolio_summary.txt")