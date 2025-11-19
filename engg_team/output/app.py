import gradio as gr
from accounts import Account

# Initialize account
account = Account(user_id="user_1", initial_deposit=10000.0)

def create_account(initial_deposit):
    global account
    account = Account(user_id="user_1", initial_deposit=initial_deposit)
    return f"Account created with initial deposit of {initial_deposit}"

def get_balance():
    return f"Current balance: {account.balance}"

def deposit(amount):
    if account.deposit_funds(amount):
        return f"Deposited {amount}. New balance: {account.balance}"
    else:
        return "Failed to deposit."

def withdraw(amount):
    if account.withdraw_funds(amount):
        return f"Withdrawn {amount}. New balance: {account.balance}"
    else:
        return "Failed to withdraw."

def buy_shares(symbol, quantity):
    if account.buy_shares(symbol, quantity):
        return f"Bought {quantity} shares of {symbol}."
    else:
        return "Failed to buy shares."

def sell_shares(symbol, quantity):
    if account.sell_shares(symbol, quantity):
        return f"Sold {quantity} shares of {symbol}."
    else:
        return "Failed to sell shares."

def get_portfolio_value():
    value = account.get_portfolio_value()
    return f"Total portfolio value: {value}"

def get_profit_loss():
    pl = account.get_profit_loss()
    return f"Profit/Loss: {pl}"

def get_holdings():
    holdings = account.get_holdings()
    return f"Current holdings: {holdings}"

def get_transaction_history():
    transactions = account.get_transaction_history()
    return f"Transaction history: {transactions}"

iface = gr.Interface(
    fn={
        "Create Account": create_account,
        "Check Balance": get_balance,
        "Deposit Funds": deposit,
        "Withdraw Funds": withdraw,
        "Buy Shares": buy_shares,
        "Sell Shares": sell_shares,
        "Portfolio Value": get_portfolio_value,
        "Profit/Loss": get_profit_loss,
        "Check Holdings": get_holdings,
        "Transaction History": get_transaction_history,
    },
    inputs={
        "Create Account": gr.inputs.Number(label="Initial Deposit"),
        "Deposit Funds": gr.inputs.Number(label="Deposit Amount"),
        "Withdraw Funds": gr.inputs.Number(label="Withdraw Amount"),
        "Buy Shares": [gr.inputs.Textbox(label="Symbol"), gr.inputs.Number(label="Quantity")],
        "Sell Shares": [gr.inputs.Textbox(label="Symbol"), gr.inputs.Number(label="Quantity")],
    },
    outputs={
        "Create Account": "text",
        "Check Balance": "text",
        "Deposit Funds": "text",
        "Withdraw Funds": "text",
        "Buy Shares": "text",
        "Sell Shares": "text",
        "Portfolio Value": "text",
        "Profit/Loss": "text",
        "Check Holdings": "text",
        "Transaction History": "text"
    },
    live=False
)

iface.launch()