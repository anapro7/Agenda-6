#Entrada
valor = float (input("Informe o valor total da sua compra: R$"))

#Processamento
#Informacao de valores de desconto
if valor >= 300.00:
    desconto = 0.15
    print("Você ganhou um desconto de 15%!")
else:
    if valor >= 200.00:
        desconto = 0.10
        print ("Você ganhou um desconto de 10%!")
    else:
        if valor < 200.00:
            desconto = 0.05
            print ("Você ganhou um desconto de 05%!")

#Calculo do valor da compra com desconto
valorDesconto = valor * desconto
totalComDesconto = valor - valorDesconto 

#Saida
print (f"Valor do desconto: R$ {valorDesconto:2f}")
print (f"Valor total com desconto: R$ {totalComDesconto:.2f}")