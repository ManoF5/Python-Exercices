# INPUT
brl = float(input("How much money do you have in your wallet:R$"))
# MATH
usd = brl / 5.22
eur = brl / 5.88
# OUTPUT
print("Dolar:\t \t${:.2f} \nEuro:\t \t${:.2f}".format(usd, eur))
