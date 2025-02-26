# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 0
extra_payment_end_month = 12
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month <= months < extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        total_paid += principal
        principal = 0

    months += 1
    print(months, round(total_paid, 2), round(principal, 2))

print(f'Total paid is ${round(total_paid, 2)} over {months} months')