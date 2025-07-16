# 13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
#  seu peso ideal, utilizando as seguintes fórmulas:
# •	Para homens: (72.7*h) - 58
# •	Para mulheres: (62.1*h) - 44.7

a = float(input(" Informe a Altura em metros: "))
h = "Masculino"
m = "Feminino"
s= str(input(" Informe o sexo, sendo h para Masculino e m para Feminino: "))
pm = (72.7*a) - 58
pf = (62.1*a) - 44.7
if s == "h" :
    print( " Sexo Masculino")
    print(f" O Peso ideal é de {pm}")

else:
    print(" Sexo Feminino")
    print(f" O Peso ideal é de {pf}")

