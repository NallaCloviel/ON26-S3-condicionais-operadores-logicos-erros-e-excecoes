#  Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                     Até 5 Kg             Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre 
# este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o 
# valor a ser pago pelo cliente.

#RACIOCÍNIO: é preciso pedir ao usuário para inserir a quantidade de maça e morango em kg e calcular o valor usando as regras estabelecidas: SE for até x kg ou y reais, 
# o resultado é z, SE NÃO, o resultado é w. 
#O preço do morango/maça se calcula pelo Xkg * Ypreço até tal valor e (Xkg * Ypreço)-(Xkg*Ypreço)*0.10 se atingirmos o parametro estabelecido


# Utilizando função para enumerar o preço de ambos, pois é preciso usar os condicionais, devido a variação
def calculando_valor(numero_de_macas_kg, numero_de_morangos_kg): #Prof Be, acho que não sei 100% ainda definir os parâmetros, fui no feeling
    if numero_de_morangos_kg <= 5:
        preco_morangos = 2.50
    elif numero_de_morangos_kg > 5:
        preco_morangos = 2.20
    
    if numero_de_macas_kg <= 5:
        preco_macas = 1.80
    elif numero_de_macas_kg >5:
        preco_macas = 1.50
    
    preco_total = (numero_de_macas_kg*preco_macas)+(numero_de_morangos_kg*preco_morangos)
    desconto = (preco_total*0.10)

    #Calculando SE for maior que 8kg ou 25 reais, o preço total tem desconto, mas se for menor que isso, o calculo do preço não tem desconto
    if numero_de_macas_kg+numero_de_morangos_kg > 8 or preco_total > 25:
        preco_total_descontado = preco_total - desconto
        return preco_total_descontado #na fé de que tem que usar aqui
    else:
        return preco_total
    
   
apresentacao = "Boas vindas a sua calculadora de contas, nossa missão é lhe ajudar a descobrir o quanto você irá gastar ao comprar suas frutas."
print(apresentacao)

apresentacao2 = print("Por favor, insira a quantidade de maçãs e morangos em kg")

numero_de_macas_kg = float(input("Insira a quantidade de maça em kg: "))
numero_de_morangos_kg = float(input("Insira a quantidade de morangos em kg: "))

preco = calculando_valor(numero_de_macas_kg, numero_de_morangos_kg)

print ("O valor a ser pago, em reais, é:")
print(round(preco,2))
