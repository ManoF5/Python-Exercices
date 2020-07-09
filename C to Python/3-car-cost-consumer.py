''' 1- Write a code to read the cost of the fabric of a car and inform the cost for the consumer
    2- The cost for a consumer to buy a new car is the sum of the cost of fabric and the percentage of the distributor and taxes
    3- first, apply the taxes on the cost of fabric, then apply the percentage of the distributor 
       TAXES:       45%
       DISTRIBUTOR: 28%      '''
taxes = 1.45
distributor = 1.28
# INPUT
fabric_cost = float(input('Cost of fabric of a car: '))
# MATH
consumer_cost = (fabric_cost * taxes) * distributor
# OUTPUT
print('Cost for the consumer:${:.2f}'.format(consumer_cost))