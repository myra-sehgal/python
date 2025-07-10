actual_cost =float(input("please enter the actual amount"))
sales_cost = float(input("please enter the sales amount"))
if (sales_cost >actual_cost):
 amount = sales_cost - actual_cost
 print("total profit = ", amount)
else:
 print("no profit!!!!")
