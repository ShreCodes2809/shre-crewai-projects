from typing import List, Dict

def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.0,
        'TSLA': 700.0,
        'GOOGL': 2700.0
    }
    return prices.get(symbol, 0.0)

class Account:
    def __init__(self, user_id: str, initial_deposit: float) -> None:
        self.user_id = user_id
        self.balance = initial_deposit
        self.initial_deposit = initial_deposit
        self.holdings = {}  # type: Dict[str, int]
        self.transactions = []  # type: List[Dict]

    def deposit_funds(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw_funds(self, amount: float) -> bool:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if price > 0 and self.balance >= total_cost and quantity > 0:
            self.balance -= total_cost
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            self.transactions.append({'action': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price})
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if symbol in self.holdings and self.holdings[symbol] >= quantity and quantity > 0:
            price = get_share_price(symbol)
            self.balance += price * quantity
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({'action': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price})
            return True
        return False

    def get_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_profit_loss(self) -> float:
        return self.get_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> Dict[str, int]:
        return self.holdings

    def get_transaction_history(self) -> List[Dict]:
        return self.transactions