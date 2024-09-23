'''
Cálculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO APÓS O TRAÇO
multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex: 746.824.890-70 (746824890)
11  10 9  8  7  6  5  4  3  2
7   4  6  8  2  4  8  9  0  7 <- PRIMEIRO DÍGITO *
70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301*10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
..... resultado é 0
contrário disso:
'''

cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo1
    contador_regressivo1 -= 1
digito_1 = (resultado_digito_1 *10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo2
    contador_regressivo2 -=1 
digito_2 = (resultado_digito_2 *10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')



    



    
    
