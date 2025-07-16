# 9.Faça um Programa que peça a temperatura em graus Farenheit, 
# transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

tempF = float(input(" Qual o valor da Temperatura? "))
print(f" A temperatura hoje e de {tempF} " + "graus Farenheit")
tempC = (5 * (tempF-32) / 9)
print(f" A temperatura em graus Celsius e de {tempC}")