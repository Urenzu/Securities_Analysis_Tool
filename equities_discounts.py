# Calculate discount rate
def calc_stock_discount_rate():
    # Inputs for cost of equity
    risk_free_rate = float(input("Enter the risk-free rate: "))
    beta = float(input("Enter the beta: "))
    expected_market_return = float(input("Enter the expected market return: "))
    
    # Inputs for cost of debt
    face_value = float(input("Enter the face value of the bond: "))
    coupon_rate = float(input("Enter the coupon rate: "))
    market_price = float(input("Enter the market price of the bond: "))
    years_to_maturity = float(input("Enter the years to maturity of the bond: "))
    tax_rate = float(input("Enter the tax rate: "))
    
    # Inputs for weight of debt and equity
    market_value_of_debt = float(input("Enter the market value of debt: "))
    market_value_of_equity = float(input("Enter the market value of equity: "))
    
    # Calculate the discount rate using Weighted average cost of capital
    cost_of_equity = risk_free_rate + beta * (expected_market_return - risk_free_rate)
    interest_payment = face_value * coupon_rate
    ytm = (interest_payment + (face_value - market_price) / years_to_maturity) / ((face_value + market_price) / 2)
    cost_of_debt = ytm * (1 - tax_rate)
    total_value = market_value_of_debt + market_value_of_equity
    weight_of_debt = market_value_of_debt / total_value
    weight_of_equity = market_value_of_equity / total_value
    discount_rate = cost_of_equity * weight_of_equity + cost_of_debt * weight_of_debt
    return discount_rate

# Calculate discounted cash flow using discount rate function
def calc_stock_dcf():
    expected_cash_flows = input("Enter the expected cash flows (separated by commas): ")
    expected_cash_flows = [float(x.strip()) for x in expected_cash_flows.split(',')]

    # Calling our calculate discount rate function
    discount_rate = calc_stock_discount_rate()
    present_values = []
    for i, cash_flow in enumerate(expected_cash_flows):
        present_value = cash_flow / (1 + discount_rate) ** (i+1)
        present_values.append(present_value)
    dcf = sum(present_values)
    return dcf

# Calculate dividend discount model
def calc_stock_ddm():
    dividend_per_share = float(input("Enter the dividend per share: "))
    required_rate_of_return = float(input("Enter the required rate of return: "))
    dividend_growth_rate = float(input("Enter the dividend growth rate: "))
    ddm = dividend_per_share / (required_rate_of_return - dividend_growth_rate)
    return ddm