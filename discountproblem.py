Total_cost = float(input("Enter the amount spent for shopping:"))
1 <= Total_cost <= 10000

if Total_cost >= 1000:
	discount = Total_cost * 0.1
	print ("The discount is :", discount)
	discounted_price = Total_cost - discount
	print("Therefore the discounted price is:", discounted_price)
if Total_cost < 1000:
	print("Sorry there is no discount for this amount")