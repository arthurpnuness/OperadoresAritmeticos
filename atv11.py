## Este código calcula a idade de uma pessoa com base no ano de nascimento e no ano atual fornecidos pelo usuário.

# Innteração com o usuario
dataNasc = int(input('Digite o ano do seu nascimento: '))
anoAtual = int(input('Em qual ano voce está? '))

## Calculo
idade = anoAtual - dataNasc

#Exibe o resultado
print('O tem {} anos'.format(idade))