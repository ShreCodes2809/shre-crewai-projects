from decimal import Decimal

# Test implementation of get_share_price
share_prices = {
    'AAPL': Decimal('150.00'),
    'TSLA': Decimal('750.00'),
    'GOOGL': Decimal('2800.00')
}

def get_share_price(symbol: str) -> Decimal:
    return share_prices.get(symbol, Decimal('0.00'))

class Account:
    def __init__(self, initial_deposit: float) -> None:
        self.balance = Decimal(initial_deposit)
        self.initial_deposit = Decimal(initial_deposit)
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        amount = Decimal(amount)
        self.balance += amount
        self.transactions.append(('deposit', None, 0, amount))

    def withdraw(self, amount: float) -> bool:
        amount = Decimal(amount)
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(('withdraw', None, 0, amount))
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if total_cost <= self.balance:
            self.balance -= total_cost
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            self.transactions.append(('buy', symbol, quantity, total_cost))
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if symbol in self.holdings and self.holdings[symbol] >= quantity:
            price = get_share_price(symbol)
            total_value = price * quantity
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.balance += total_value
            self.transactions.append(('sell', symbol, quantity, total_value))
            return True
        return False

    def calculate_portfolio_value(self) -> float:
        total_value = Decimal('0.00')
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return float(total_value)

    def calculate_profit_loss(self) -> float:
        current_portfolio_value = self.calculate_portfolio_value()
        total_value = current_portfolio_value + self.balance
        return float(total_value - self.initial_deposit)

    def get_holdings(self) -> dict:
        return self.holdings

    def get_transactions(self) -> list:
        return self.transactions