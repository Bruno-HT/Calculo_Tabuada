import os
# Programa para estudar divisores

divisores = []
numero = ''

def apresentacao_inicial():
    os.system('cls')
    print('''
░█▀▀█ ─█▀▀█ ░█─── ░█▀▀█ ░█─░█ ░█─── ─█▀▀█ ░█▄─░█ ░█▀▀▄ ░█▀▀▀█ 　 ░█▀▀▀█ ░█▀▀▀█ 　 ░█▀▀▄ ▀█▀ ░█──░█ ▀█▀ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ 
░█─── ░█▄▄█ ░█─── ░█─── ░█─░█ ░█─── ░█▄▄█ ░█░█░█ ░█─░█ ░█──░█ 　 ░█──░█ ─▀▀▀▄▄ 　 ░█─░█ ░█─ ─░█░█─ ░█─ ─▀▀▀▄▄ ░█──░█ ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ 
░█▄▄█ ░█─░█ ░█▄▄█ ░█▄▄█ ─▀▄▄▀ ░█▄▄█ ░█─░█ ░█──▀█ ░█▄▄▀ ░█▄▄▄█ 　 ░█▄▄▄█ ░█▄▄▄█ 　 ░█▄▄▀ ▄█▄ ──▀▄▀─ ▄█▄ ░█▄▄▄█ ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█▄▄▄█''')
    print('\nAo calcular os divisores veremos todos os números que podem dividir um ')
    print('determinado número de forma inteira, ou seja, o resto da operação será zero!\n')

def entrada_do_numero_e_calculo_divisores():
    numero = int(input('Qual número você gostaria de calcular os divisores? '))
    for contador in range(1, numero + 1):
        calculo = numero % contador 
        if (calculo == 0):
            divisores.append(contador)

def apresentacao_final():
    print(F'Esses são os divisores do número {numero}: {divisores}')
    if (len(divisores) == 2):
        print(f'O número {numero} é um número primo, ou seja, só tem dois divisores!')
    reiniciar = input('Deseja calcular os divisores de algum outro número? (S/N) ').upper()
    if reiniciar == 'S':
        divisores.clear()
        main()
    else:
        print('\nObrigado por ter estudado um pouco comigo!!!')

def main():
    apresentacao_inicial()
    entrada_do_numero_e_calculo_divisores()
    apresentacao_final()

if __name__ == '__main__':
    main()