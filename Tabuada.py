# Programa para estudar tabuada

print('\n*******************************')
print('*** VAMOS ESTUDAR A TABUADA ***')
print('*******************************')

fator1 = int(input('\nQual número irei calcular a tabuada?'))
produto = []
resposta = []
correcao = []
errado = []

for fator2 in range(0, 11):
    calculo = fator1 * fator2
    produto.append(calculo)

for indice in range(0, 11):
    teste = int(input(f'Qual o valor de {indice} x {fator1}: '))
    resposta.append(teste)

for index in range (len(produto)):
    check = produto[index] == resposta[index]
    if check:
        correcao.append(0)
    else:
        correcao.append(1)
        errado.append(resposta[index])

erros = correcao.count(1)

print(f'\nVocê teve {erros} erros.')
if (erros == 0):
    print('Parabéns!!!!')
else:
    print(f'Veja seus erros: {errado}')
    print(f'Você colocou os seguintes números: {resposta}')
    print(f'Veja como é o resultado correto:   {produto}\n')