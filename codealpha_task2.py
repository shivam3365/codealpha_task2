import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= shares:
                self.portfolio[symbol] -= shares
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
                print(f"Removed {shares} shares of {symbol}.")
            else:
                print(f"Not enough shares to remove. You only have {self.portfolio[symbol]} shares of {symbol}.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def view_portfolio(self):
        print("Current Portfolio:")
        for symbol, shares in self.portfolio.items():
            print(f"{symbol}: {shares} shares")
    
    def get_stock_price(self, symbol):
        stock = yf.Ticker(symbol)
        price = stock.history(period='1d')['Close'][0]
        return price

    def track_performance(self):
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            value = price * shares
            total_value += value
            print(f"{symbol}: {shares} shares @ ${price:.2f} each, Total Value: ${value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(symbol, shares)
        elif choice == '3':
            portfolio.view_portfolio()
        elif choice == '4':
            portfolio.track_performance()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
