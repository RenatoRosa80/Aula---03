""" 15.	Faça um Programa que pergunte quanto você ganha por hora e o 
 número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
 referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
"""
"""
•	salário bruto.
•	quanto pagou ao INSS.
•	quanto pagou ao sindicato.
•	o salário líquido.
•	calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$ IR (11%) : R$ INSS (8%) : R$ Sindicato ( 5%) : R
$ Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

"""

hp = float(input(" Qual o valor da sua hora trabalhada? "))
#print(f" O valor da minha hora de trabalho é de {hp}" + " " + "reais")
#ht = float(input(" Quantas horas voce trabalha por semana? "))
#print(f" Eu trabalho {ht} " + "horas por semana")
dm = int(input(" Quantas Horas voce trabalha no mes?"))
#print(f"Eu trabalhei no mes que fechou {dm}" + " dias")

# Salário Bruto
sb = hp *  dm
print(f" O salario Bruto no mes foi de R$ {sb:.2f}  ")

# INSS

inss = sb * 0.08
print(f" Valor descontado do INSS R$ {inss:.2f} ")

# Sindicato

sd = sb * 0.05
print(f" Valor descontado pelo Sindicato R$ {sd:.2f}")

# Salário Líquido

sl = sb - ( inss + sd )
print(f" Salário Líquido R$ {sl:.2f} ")
