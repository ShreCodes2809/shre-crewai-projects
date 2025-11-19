import gradio as gr
from accounts import Account, get_share_price

def create_account(initial_deposit):
    global account
    account = Account(initial_deposit)
    return f"Account created with initial deposit: ${initial_deposit}"

def deposit_funds(amount):
    account.deposit(amount)
    return f"Deposited: ${amount}\nCurrent Balance: ${account.balance}"

def withdraw_funds(amount):
    if account.withdraw(amount):
        return f"Withdrew: ${amount}\nCurrent Balance: ${account.balance}"
    else:
        return "Withdrawal failed. Insufficient funds."

def buy_shares(symbol, quantity):
    if account.buy_shares(symbol, quantity):
        return f"Bought {quantity} shares of {symbol}\nCurrent Balance: ${account.balance}"
    else:
        return "Purchase failed. Insufficient funds or invalid symbol."

def sell_shares(symbol, quantity):
    if account.sell_shares(symbol, quantity):
        return f"Sold {quantity} shares of {symbol}\nCurrent Balance: ${account.balance}"
    else:
        return "Sale failed. Not enough shares."

def view_portfolio():
    value = account.calculate_portfolio_value()
    holdings = account.get_holdings()
    return f"Portfolio Value: ${value}\nHoldings: {holdings}"

def view_profit_loss():
    profit_loss = account.calculate_profit_loss()
    return f"Profit/Loss: ${profit_loss}"

def view_transactions():
    transactions = account.get_transactions()
    return f"Transactions: {transactions}"

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Account Management")
            initial_deposit_input = gr.Number(label="Initial Deposit")
            create_button = gr.Button("Create Account")
            create_output = gr.Textbox()
            create_button.click(create_account, initial_deposit_input, create_output)
            
            deposit_input = gr.Number(label="Deposit Amount")
            deposit_button = gr.Button("Deposit Funds")
            deposit_output = gr.Textbox()
            deposit_button.click(deposit_funds, deposit_input, deposit_output)
            
            withdraw_input = gr.Number(label="Withdraw Amount")
            withdraw_button = gr.Button("Withdraw Funds")
            withdraw_output = gr.Textbox()
            withdraw_button.click(withdraw_funds, withdraw_input, withdraw_output)
            
            gr.Markdown("### Trading")
            symbol_input = gr.Textbox(label="Share Symbol (AAPL, TSLA, GOOGL)")
            quantity_input = gr.Number(label="Quantity")
            
            buy_button = gr.Button("Buy Shares")
            buy_output = gr.Textbox()
            buy_button.click(buy_shares, [symbol_input, quantity_input], buy_output)
            
            sell_button = gr.Button("Sell Shares")
            sell_output = gr.Textbox()
            sell_button.click(sell_shares, [symbol_input, quantity_input], sell_output)
            
            gr.Markdown("### Reports")
            portfolio_button = gr.Button("View Portfolio")
            portfolio_output = gr.Textbox()
            portfolio_button.click(view_portfolio, None, portfolio_output)
            
            profit_loss_button = gr.Button("View Profit/Loss")
            profit_loss_output = gr.Textbox()
            profit_loss_button.click(view_profit_loss, None, profit_loss_output)
            
            transactions_button = gr.Button("View Transactions")
            transactions_output = gr.Textbox()
            transactions_button.click(view_transactions, None, transactions_output)

if __name__ == "__main__":
    demo.launch()