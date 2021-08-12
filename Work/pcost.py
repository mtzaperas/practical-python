# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv','rt') as portfolio:
	cost = 0
	file_header = next(portfolio)
	for stock in portfolio:
		name, num_shares, purchase_price = stock.split(',')
		cost += int(num_shares) * float(purchase_price)

print(f'Total cost {round(cost,2)}')