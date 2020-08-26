# Conversor de Base Númerica
# Autor: Rento Borelli da Silva
# Objetivo: educacional
# Data: 24/08/20

# Adiciona o módulo de funções
import conversor_funcoes
from conversor_funcoes import f_escolhe_opcao
from conversor_funcoes import f_usuario_input
from conversor_funcoes import f_decimal_binario

f_escolhe_opcao()
x = conversor_funcoes.f_usuario_input()

if x == 1:
    decimal = int(input("\nInforme o valor em decimal: "))
    f_decimal_binario(decimal)
    res_binario = conversor_funcoes.f_decimal_binario(decimal)
    print("Resultado em binario: " + res_binario)
    