# dados
soma_total = 0
cont = 0
media = 0
pergunta = "S"
# input
while pergunta != "N":
    num = int(input("Digite um numero: "))
    pergunta = input("Quer continuar? ").upper()
    media += num  # media = media + numero
    cont += 1
    cont
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        
# output
if cont == 1:
    print(f"Ao mesmo tempo o numero {num} é maior e menor")
    print("Não existe media pois so possui um numero")
else:
    print(f"Maior numero: {maior}")
    print(f"Manor numero: {menor}")
    print(f"Media dos numeros: {media/cont}")
