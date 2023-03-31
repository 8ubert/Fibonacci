'''
Feito por iamAware:
João Eduardo
Larissa
Luiza
Rafael
Vitor
'''

try:
    n = int(input("Digite um número maior ou igual a 2: "))
    if n < 2:
        raise ValueError("O número deve ser maior ou igual a 2.")
except ValueError as erro:
    print("Erro: ", erro)
else:
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=" ")
        a, b = b, a + b
        i += 1
