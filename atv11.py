# Innteração com o usuario
dataNasc = int(input('Digite o ano do seu nascimento: '))
anoAtual = int(input('Em qual ano voce está? '))

## Calculo
idade = anoAtual - dataNasc

#Exibe o resultado
print('O tem {} anos'.format(idade))