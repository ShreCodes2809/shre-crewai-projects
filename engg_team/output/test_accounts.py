import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):

    def test_get_share_price(self):
        self.assertEqual(get_share_price('AAPL'), 150.0)
        self.assertEqual(get_share_price('TSLA'), 700.0)
        self.assertEqual(get_share_price('GOOGL'), 2700.0)
        self.assertEqual(get_share_price('MSFT'), 0.0)  # Stock not listed

    def test_deposit_funds(self):
        account = Account('user1', 100.0)
        self.assertTrue(account.deposit_funds(50.0))
        self.assertEqual(account.balance, 150.0)
        self.assertFalse(account.deposit_funds(-50.0))  # Negative deposit

    def test_withdraw_funds(self):
        account = Account('user1', 100.0)
        self.assertTrue(account.withdraw_funds(50.0))
        self.assertEqual(account.balance, 50.0)
        self.assertFalse(account.withdraw_funds(100.0))  # Insufficient funds

    def test_buy_shares(self):
        account = Account('user1', 1000.0)
        self.assertTrue(account.buy_shares('AAPL', 2))
        self.assertEqual(account.holdings['AAPL'], 2)
        self.assertEqual(account.balance, 700.0)
        self.assertFalse(account.buy_shares('AAPL', 0))  # Zero quantity

    def test_sell_shares(self):
        account = Account('user1', 1000.0)
        account.buy_shares('AAPL', 2)
        self.assertTrue(account.sell_shares('AAPL', 1))
        self.assertEqual(account.holdings['AAPL'], 1)
        self.assertEqual(account.balance, 850.0)
        self.assertFalse(account.sell_shares('AAPL', 2))  # Insufficient holdings

    def test_get_portfolio_value(self):
        account = Account('user1', 1000.0)
        account.buy_shares('AAPL', 2)
        self.assertEqual(account.get_portfolio_value(), 1000.0)

    def test_get_profit_loss(self):
        account = Account('user1', 1000.0)
        account.buy_shares('AAPL', 2)
        self.assertEqual(account.get_profit_loss(), 0.0)

    def test_get_holdings(self):
        account = Account('user1', 1000.0)
        account.buy_shares('AAPL', 2)
        self.assertEqual(account.get_holdings(), {'AAPL': 2})

    def test_get_transaction_history(self):
        account = Account('user1', 1000.0)
        account.buy_shares('AAPL', 2)
        history = account.get_transaction_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]['action'], 'buy')

if __name__ == '__main__':
    unittest.main()