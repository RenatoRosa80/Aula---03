# 18.	Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
# de download do arquivo usando este link (em minutos).

# Solicita o tamanho do arquivo em MB e a velocidade do link em Mbps
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Converte o tamanho do arquivo para megabits (1 MB = 8 Mb)
tamanho_arquivo_mb = tamanho_arquivo_mb * 8

# Calcula o tempo em segundos
tempo_segundos = tamanho_arquivo_mb / velocidade_link_mbps

# Converte o tempo para minutos
tempo_minutos = tempo_segundos / 60

# Exibe o resultado
print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")


"""
# Solicita o tamanho do arquivo em MB e a velocidade do link em Mbps
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Converte o tamanho do arquivo para megabits (1 MB = 8 Mb)
tamanho_arquivo_mb = tamanho_arquivo_mb * 8

# Calcula o tempo em segundos
tempo_segundos = tamanho_arquivo_mb / velocidade_link_mbps

# Converte o tempo para minutos
tempo_minutos = tempo_segundos / 60

# Exibe o resultado
print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")

"""