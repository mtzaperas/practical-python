# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
	'Calculates purchase cost of portfolio from csv file'
	with open(filename,'rt') as portfolio:
		cost = 0
		stocks = csv.reader(portfolio)
		file_header = next(portfolio)
		for stock in stocks:
			try:
				name, num_shares, purchase_price = stock
				cost += int(num_shares) * float(purchase_price)
			except ValueError:
				print('Couldnt parse: ', stock)
	
	return round(cost,2)

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {cost}')