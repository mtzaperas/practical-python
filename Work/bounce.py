# bounce.py
#
# Exercise 1.5
height = 100 #meters

for i in range(10):
	bounce_height = round(height*.6, 4)
	print("{} {}".format(i,bounce_height))
	height = bounce_height
