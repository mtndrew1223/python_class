#function that print a welcome message (no arguments)

#print_welcome()
#print_welcome()


def calc_investments(monthly_investment,years,yearly_interest):
    monthly_interest_rate=yearly_interest/12/100
    months = years * 12
    future_value = 0
    for i in range (0,months): 
        future_value+= monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

total_investments = calc_investments(200,20,8)
print(total_investments)