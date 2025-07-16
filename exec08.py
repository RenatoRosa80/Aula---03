# 7.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# A = L²: (onde "A" é a área e "L" é o comprimento do lado)
l = float(input("Informe o lado do Quadrado: "))
a = l ** 2
print(f'A area do quadrado é de {a} ')
dq = 2 * a
print(f" O dobro dessa area é {dq}")