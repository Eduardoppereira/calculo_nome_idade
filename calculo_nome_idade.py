nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Verificando se a idade é um número positivo
try:
    idade = int(idade)
    if idade <= 0:
        raise ValueError("A idade deve ser um número positivo.")
except ValueError:
    print("Por favor, insira uma idade válida.")
    exit()

if len(nome) > 1 and idade > 1:
    print("Seu nome é {}, e você tem {} anos.".format(nome, idade))
    print("Nome ao contrário:", nome[::-1])

    if ' ' in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")

    primeira_letra = nome[0]
    ultima_letra = nome[-1]

    print("Primeira letra do nome:", primeira_letra)
    print("Última letra do nome:", ultima_letra)

    # Adicionando verificação de faixa etária
    if idade < 18:
        print("Você é menor de idade.")
    elif 18 <= idade <= 65:
        print("Você é adulto.")
    else:
        print("Você é um idoso.")

    # Adicionando contagem de caracteres no nome
    num_caracteres = len(nome)
    print("O nome possui {} caracteres.".format(num_caracteres))

    # Verificando se o nome é composto apenas por letras
    if nome.isalpha():
        print("O nome contém apenas letras.")
    else:
        print("O nome não contém apenas letras.")

    # Verificando a diferença entre a idade e 100 anos
    diferenca_idade_100 = abs(idade - 100)
    print("A diferença entre sua idade e 100 anos é {}.".format(diferenca_idade_100))

    # Verificando se o nome está em maiúsculas, minúsculas ou ambas
    if nome.isupper():
        print("O nome está todo em maiúsculas.")
    elif nome.islower():
        print("O nome está todo em minúsculas.")
    else:
        print("O nome possui maiúsculas e minúsculas.")

    # Calculando o dobro da idade
    dobro_idade = idade * 2
    print("O dobro da sua idade é {}.".format(dobro_idade))

else:
    print("Por favor, insira um nome válido e uma idade válida.")
