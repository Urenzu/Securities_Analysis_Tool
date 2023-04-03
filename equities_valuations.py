# Calculate capital asset pricing model
def calc_stock_capm():
    risk_free_rate = float(input("Enter the risk-free rate: "))
    expected_market_return = float(input("Enter the expected market return: "))
    beta = float(input("Enter the stock's beta: "))
    capm = risk_free_rate + beta * (expected_market_return - risk_free_rate)
    return capm

# Calculate EV/EBITDA ratio
def calc_stock_ev_ebitda():
    total_cash = float(input("Total cash: "))
    total_debt = float(input("Total debt: "))
    net_cash = total_cash - total_debt
    marketcap = float(input("Company market cap: "))
    enterprise_value = marketcap + net_cash
    ebitda = float(input("Enter the EBITDA: "))
    ev_ebitda = enterprise_value / ebitda
    return ev_ebitda