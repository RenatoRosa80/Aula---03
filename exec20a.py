# Calculo excedente de kg de Peixe


peso = float(input(" Dgite a quantidade em Kilos de peixe: "))
limite = 50.00

if peso  > limite:
    excedente = peso - limite
    multa = excedente * 4.00
else:
    excedente = 0.00
    multa = 0.00

#   Impressao dos Resultados
print("\nRelatorio")
print(f"Peso dos Peixes: {peso:.2f} kg ")
print(f"Limite estabelicdo de Peixes: {limite:.2f} kg")

#Imprimindo resultados do Excesso de Peixes pescado.

if excedente > 0:
    print(f"Excesso de peso: {excedente:.2f} kg")
    print(f"Multa a pagar é de: R$ {multa:.2f}")
else:
    print(" Nao houve excedente no peso de Peixe pescados! ")
