# 11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# •	o produto do dobro do primeiro com metade do segundo .
# •	a soma do triplo do primeiro com o terceiro.
# •	o terceiro elevado ao cubo.

n1 = int(input(" Informe o primeiro numero inteiro: "))
n2 = int(input(" informe o segundo numero inteiro: "))
nr = float(input(" Informe um numero real: "))
p = (n1 + n1) * ( n2 / 2 )
print(f" O produto do dobro do primeiro com metade do segundo é {p}  ")
s = ( 3 * n1 ) + nr 
print(f" A soma do triplo do primeiro com o terceiro é {s}  ")
c = nr * nr * nr
print(f" O terceiro elevado ao cubo. é {c}  ")


