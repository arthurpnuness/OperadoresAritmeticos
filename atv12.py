## Este código calcula o custo total para trocar os pneus de todos os carros de uma frota, considerando que cada carro possui quatro pneus e cada pneu custa R$395,40.

## Interação com o usuario
frota = int(input('Quantos carros tem na tua frota? '))

## Calculo
totalPneus = frota * 4
valorTotal = (totalPneus * 4) * 395.40

## Exibe o resultado
print('O valor necessário para trocar os pneus de todos teus carros da frota é de R${}'.format(valorTotal))