# 14.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
#  o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
#  que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
#  pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa 
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
#  a quantidade de quilos além do limite e na variável multa o valor da multa que João 
# deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# Programa para calcular o excesso de peso e a multa para João Papo-de-Pescador

# Lê o peso dos peixes
peso = float(input("Digite o peso dos peixes (em kg): "))

# Define o limite estabelecido pelo regulamento
limite = 50.0

# Calcula o excesso, se houver
if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00
else:
    excesso = 0.0
    multa = 0.0

# Imprime os resultados
print("\nRelatório:")
print(f"Peso dos peixes: {peso:.2f} kg")
print(f"Limite estabelecido: {limite:.2f} kg")

if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a pagar: R$ {multa:.2f}")
else:
    print("Não houve excesso de peso. Multa: R$ 0.00")