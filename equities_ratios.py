# Calculate P/E ratio
def calc_stock_pe_ratio():
    stock_price = float(input("Enter the stock price: "))
    eps = float(input("Enter the earnings per share: "))
    pe_ratio = stock_price / eps
    return pe_ratio

# Calculate P/B ratio
def calc_stock_pb_ratio():
    stock_price = float(input("Enter the stock price: "))
    companies_total_equity = float(input("Enter the companies total equity: "))
    companies_shares_outstanding = float(input("Enter the companies shares outstanding: "))
    book_value_per_share = companies_total_equity / companies_shares_outstanding
    pb_ratio = stock_price / book_value_per_share
    return pb_ratio