import unittest
from decimal import Decimal
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = Account(1000.0)  # Initial deposit of 1000
    
    def test_initialization(self):
        self.assertEqual(self.account.balance, Decimal('1000.00'))
        self.assertEqual(self.account.initial_deposit, Decimal('1000.00'))
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])
    
    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, Decimal('1500.00'))
        self.assertIn(('deposit', None, 0, Decimal('500.00')), self.account.transactions)
    
    def test_withdraw_success(self):
        result = self.account.withdraw(200.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, Decimal('800.00'))
        self.assertIn(('withdraw', None, 0, Decimal('200.00')), self.account.transactions)
    
    def test_withdraw_failure(self):
        result = self.account.withdraw(2000.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, Decimal('1000.00'))  # Balance should remain unchanged

    def test_buy_shares_success(self):
        result = self.account.buy_shares('AAPL', 4)  # Cost 600
        self.assertTrue(result)
        self.assertEqual(self.account.balance, Decimal('400.00'))
        self.assertEqual(self.account.holdings['AAPL'], 4)
        self.assertIn(('buy', 'AAPL', 4, Decimal('600.00')), self.account.transactions)
    
    def test_buy_shares_failure(self):
        result = self.account.buy_shares('GOOGL', 1)  # Cost 2800
        self.assertFalse(result)
        self.assertEqual(self.account.balance, Decimal('1000.00'))  # Balance should remain unchanged

    def test_sell_shares_success(self):
        self.account.buy_shares('AAPL', 4)
        result = self.account.sell_shares('AAPL', 2)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, Decimal('700.00'))
        self.assertEqual(self.account.holdings['AAPL'], 2)
        self.assertIn(('sell', 'AAPL', 2, Decimal('300.00')), self.account.transactions)

    def test_sell_shares_failure(self):
        result = self.account.sell_shares('AAPL', 1)  # No initial holdings
        self.assertFalse(result)
        self.assertEqual(self.account.balance, Decimal('1000.00'))

    def test_calculate_portfolio_value(self):
        self.account.buy_shares('AAPL', 4)  # 4 * 150 = 600
        self.account.buy_shares('TSLA', 1)  # 1 * 750 = 750
        portfolio_value = self.account.calculate_portfolio_value()
        self.assertEqual(portfolio_value, 1350.0)
    
    def test_calculate_profit_loss(self):
        self.account.deposit(500.0)
        self.account.buy_shares('AAPL', 4)
        self.account.buy_shares('TSLA', 1)
        profit_loss = self.account.calculate_profit_loss()
        self.assertEqual(profit_loss, 850.0)  # Portfolio value 1350 + Cash 250 - Initial deposit 1000
    
    def test_get_holdings(self):
        self.account.buy_shares('AAPL', 4)
        holdings = self.account.get_holdings()
        self.assertEqual(holdings, {'AAPL': 4})
    
    def test_get_transactions(self):
        self.account.deposit(500.0)
        self.account.buy_shares('AAPL', 4)
        transactions = self.account.get_transactions()
        self.assertIn(('deposit', None, 0, Decimal('500.00')), transactions)
        self.assertIn(('buy', 'AAPL', 4, Decimal('600.00')), transactions)

if __name__ == '__main__':
    unittest.main()