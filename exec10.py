#10.	Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Farenheit.

tempC = float(input(" Qual o valor da Temperatura? "))
print(f" A temperatura hoje e de {tempC} " + "graus Celsius")
tempF = tempC * ((9/5) + 32)
print(f" A temperatura em graus Farenheit e de {tempF}")