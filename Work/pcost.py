# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
	'Calculates purchase cost of portfolio from csv file'

	with open(filename,'rt') as portfolio:
		cost = 0
		file_header = next(portfolio)
		for stock in portfolio:
			name, num_shares, purchase_price = stock.split(',')
			cost += int(num_shares) * float(purchase_price)
	
	return round(cost,2)

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')