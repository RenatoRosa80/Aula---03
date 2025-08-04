# 17.	Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. Considere que a cobertura 
# da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#  Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 
# 3 situações:
"""
•	comprar apenas latas de 18 litros;
•	comprar apenas galões de 3,6 litros;
•	misturar latas e galões, de forma que o preço seja o menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
 considere latas cheias.
"""

# Programa para Cálculo de Tintas

import math

def calcular_tintas():
    # Solicita a área a ser pintada em metros quadrados
    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
    
    # Adiciona 10% de folga
    area_com_folga = area * 1.1
    
    # Calcula a quantidade de litros de tinta necessária
    litros_necessarios = area_com_folga / 6
    
    # 1. Cálculo apenas com latas de 18L
    latas_18 = math.ceil(litros_necessarios / 18)
    preco_latas_18 = latas_18 * 80
    
    # 2. Cálculo apenas com galões de 3.6L
    galoes_36 = math.ceil(litros_necessarios / 3.6)
    preco_galoes_36 = galoes_36 * 25
    
    # 3. Cálculo otimizado misturando latas e galões
    latas_18_otimizado = math.floor(litros_necessarios / 18)
    resto = litros_necessarios % 18
    galoes_36_otimizado = math.ceil(resto / 3.6)
    
    # Verifica se é melhor comprar uma lata extra em vez de 
    # vários galões
    if galoes_36_otimizado > 5:
        latas_18_otimizado += 1
        galoes_36_otimizado = 0
    
    preco_otimizado = (latas_18_otimizado * 80) + (galoes_36_otimizado * 25)
    
    # Exibe os resultados
    print("\nOpções de compra:")
    print(f"1. Apenas latas de 18L: {latas_18} lata(s) - R$ {preco_latas_18:.2f}")
    print(f"2. Apenas galões de 3.6L: {galoes_36} galão(ões) - R$ {preco_galoes_36:.2f}")
    print(f"3. Mistura otimizada: {latas_18_otimizado} lata(s) e {galoes_36_otimizado} galão(ões) - R$ {preco_otimizado:.2f}")

# Executa o programa
calcular_tintas()

### Explicação do programa:

"""
1. **Entrada de dados**: O usuário informa a área a ser pintada em m².
2. **Cálculo com folga**: Adiciona 10% de folga e calcula a 
quantidade de tinta necessária (1L para cada 6m²).
3. **Opção 1 - Apenas latas de 18L**:
   - Calcula quantas latas são necessárias (arredondando para cima)
   - Calcula o preço total
4. **Opção 2 - Apenas galões de 3.6L**:
   - Calcula quantos galões são necessários (arredondando para cima)
   - Calcula o preço total
5. **Opção 3 - Mistura otimizada**:
   - Usa o máximo possível de latas de 18L
   - Completa com galões de 3.6L
   - Verifica se vale a pena comprar uma lata extra em vez de 
   muitos galões
6. **Saída**: Mostra as três opções com quantidades e preços.

O programa sempre arredonda para cima as quantidades de tinta 
necessárias, garantindo que a área seja completamente coberta.
"""