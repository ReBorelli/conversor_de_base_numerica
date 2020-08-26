# Módulo com funções para conversor_main.py

# função para escolher uma opção
def f_escolhe_opcao():
    print("\nEscolha uma opcao:\n")
    print("1 - decimal para binário\n")
    print("2 - binário para decimal\n")
    print("3 - hexadecimal para binário\n")
    print("4 - binário para hexadecimal\n")
    print("5 - hexadecimal para decimal\n")
    print("6 - decimal para hexadecimal\n")

# Função para tratar user inputs
def f_usuario_input():
    escolha = "erro"
    alcance = False
    alcance_aceito = range(1,6)
    while escolha.isdigit() == False or alcance == False:
        escolha = input('Opcao: ')
        if escolha.isdigit() == False:
            print('Digite apenas numeros.')
        if escolha.isdigit() == True:
            if int(escolha) in alcance_aceito:
                alcance = True
            else:
                alcance = False
                print('Opcao invalida')
    return int(escolha)

def f_decimal_binario(decimal):
    binario = []
    resto = 0
    while decimal > 1:
        resto = decimal % 2
        decimal //= 2
        binario.append(resto)
        if decimal == 1:
            binario.append(1)
            break
        else:
            continue
    binario.reverse()
    res_binario = "".join(map(str, binario))
    return res_binario 