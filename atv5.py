# Interação com o usuário
nome = input("Digite teu nome: ")
nota1 = float(input("Digite a nota da tua primeira prova: "))
nota2 = float(input("Digite a nota da tua segunda prova: "))
nota3 = float(input("Digite a nota da tua terceira prova: "))

# Calculo
mediaFinal = (nota1 + nota2 + nota3) / 3

# Exibe  resultado
print('A média final do aluno {} é: {} '.format(nome, mediaFinal))