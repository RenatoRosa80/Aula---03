# imc = indice de massa corporal
# imc = peso / altura ** 2
# imc = peso / (altura * altura)

nome = 'lucas'
altura = 1.71
peso = 80
imc = peso / altura ** 2 
print(nome, 'tem' ,altura, 'de altura' ,peso, 'kg' , 'e' ,imc, 'de massa corporal')
# f - strigs . O que esta dentro das chaves é uma variável e do lado de fora é o rótulo.
print(f'{nome} tem {altura} de altura e, \npesa {peso} e seu IMC é = {imc : .2f}')
# opção sem espaçamento
print(f'{nome} tem {altura} de altura e pesa {peso} Kg e, seu IMC é = {imc : .2f}')