## Este código calcula o consumo médio de combustível de um carro com base na distância total percorrida e na quantidade de combustível consumido. 

# Interação com o usuário
disTotal = float(input("Digite a distancia total percorrida em km: "))
consumo = float(input("Digite a quantidade de combustivel que foi consumida em litros: "))

# Calculo
consumoM = disTotal / consumo

# Exibe o resultado
print('O consumo médio do teu carro é: {}'.format(consumoM))
