# 8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
hp = float(input(" Qual o valor da sua hora trabalhada? "))
#print(f" O valor da minha hora de trabalho é de {hp}" + " " + "reais")
ht = float(input(" Quantas horas voce trabalha por semana? "))
#print(f" Eu trabalho {ht} " + "horas por semana")
dm = int(input(" Quantos dias voce trabalhou no mes?"))
#print(f"Eu trabalhei no mes que fechou {dm}" + " dias")
sm = (hp * ht) * dm
print(f" O salario total no mes foi de {sm} " + "reais")