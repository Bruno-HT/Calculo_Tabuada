# Programa para estudar tabuada
import os

produto = []
resposta = []
correcao = []
errado = []

def apresentacao_inicial():
    '''Apresentação inicial e pequena explicação do que é a multiplicação.'''

    print('''
▒█▀▀█ ░█▀▀█ ▒█░░░ ▒█▀▀█ ▒█░▒█ ▒█░░░ ░█▀▀█ ▒█▄░▒█ ▒█▀▀▄ ▒█▀▀▀█ 　 ░█▀▀█ 　 ▀▀█▀▀ ░█▀▀█ ▒█▀▀█ ▒█░▒█ ░█▀▀█ ▒█▀▀▄ ░█▀▀█ 
▒█░░░ ▒█▄▄█ ▒█░░░ ▒█░░░ ▒█░▒█ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▒█ ▒█░░▒█ 　 ▒█▄▄█ 　 ░▒█░░ ▒█▄▄█ ▒█▀▀▄ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▒█▄▄█ 
▒█▄▄█ ▒█░▒█ ▒█▄▄█ ▒█▄▄█ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ▒█░░▀█ ▒█▄▄▀ ▒█▄▄▄█ 　 ▒█░▒█ 　 ░▒█░░ ▒█░▒█ ▒█▄▄█ ░▀▄▄▀ ▒█░▒█ ▒█▄▄▀ ▒█░▒█''')

    print('\nA multiplicação nada mais é do que a soma de um número por ele mesmo uma determinada quantidade de vezes.')
    print('Vejamos um exemplo: 2 x 3 = 2 + 2 + 2 = 6 ou como de outra forma 2 x 3 = 3 + 3 = 6\n')
    print('Vamos agora calcular a tabuada!')


def realizar_calculos():
    '''Recebe qual tabuada o usuário deseja exercitar e realiza o cálculo!
    INPUT: qual o fator da tabuada a ser calculada.
    OUTPUT: tabuada do número inserido pelo usuário.'''
    fator1 = int(input('\nQual número irei calcular a tabuada? '))

    for fator2 in range(0, 11):
        calculo = fator1 * fator2
        produto.append(calculo)
    return fator1

def preenchendo_tabuada(fator):
    '''Pergunta número a número a tabuada do número solicitado.
    INPUT: toda a tabuada do número
    OUTPUT: tabuada preenchida pelo usuário para verificação posterior.'''
    os.system('cls')
    for indice in range(0, 11):
        teste = int(input(f'Qual o valor de {indice} x {fator}: '))
        resposta.append(teste)

def correcao_da_tabuada():
    '''Realiza a verificação da tabuada preenchida pelo usuário com a calculada pelo sistema e acha os erros.
    OUTPUT: lista com os possíveis erros do usuário'''
    for index in range (len(produto)):
        check = produto[index] == resposta[index]
        if check:
            correcao.append(0)
        else:
            correcao.append(1)
            errado.append(resposta[index])

    erros = correcao.count(1)
    return erros

def apresentacao_final(qtd_erro):
    '''Apresentação dos resultados.'''
    print(f'\nVocê teve {qtd_erro} erros.')
    if (qtd_erro == 0):
        print('Parabéns!!!!')
    else:
        print(f'Veja seus erros: {errado}')
        print(f'Você colocou os seguintes números: {resposta}')
        print(f'Veja como é o resultado correto:   {produto}\n')

    nova_tabuada = input('Vamos praticar mais um pouco? ').upper()
    if nova_tabuada == 'S':
                produto.clear()
                resposta.clear()
                correcao.clear()
                errado.clear()
                main()
    else:
        print('\nObrigado por estudarmos juntos hoje!!!\n\n')

def main():
    os.system('cls')
    apresentacao_inicial()
    fator = realizar_calculos()
    preenchendo_tabuada(fator)
    qtd_erro = correcao_da_tabuada()
    apresentacao_final(qtd_erro)
    
if __name__ == '__main__':
    main()