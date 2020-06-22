# INPUT
price = float(input("What is the price of the product:$"))
discount = float(input("With the discount of(%):"))
# MATH
final_price = price * (discount/100)
# OUTPUT
print("The final price:${}".format(final_price))
