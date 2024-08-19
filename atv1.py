## Esse código realiza a soma de dois números inteiros inseridos pelo usuário e exibe o resultado. 

# Interação com o usuario
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

#Calculo
soma = num1 + num2

# Exibe o resultado
print('A soma entre {} e {} é igual a --> {}'.format(num1, num2, soma))