# 4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = float(input(" Qual a nota do Primeiro Bimestre? "))
n2 = float(input(" Qual a nota do Segundo Bimestre? "))
n3 = float(input(" Qual a nota do Terceiro Bimestre? "))
n4 = float(input(" Qual a nota do Quarto Bimestre? "))
m = ( n1 + n2 + n3 + n4 ) / 4
print(f' A média anual é {m} ')

if m >= 7:
    print(" O aluno foi Aprovado! ")
else:
    print('O Aluno foi Reprovado! ')

