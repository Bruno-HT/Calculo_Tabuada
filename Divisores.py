# Programa para estudar divisores

print('\n**********************************')
print('*** VAMOS ESTUDAR OS DIVISORES ***')
print('**********************************\n')

numero = int(input('Qual número você gostaria de calcular os divisores? '))

divisores = []

for contador in range(1, numero + 1):
    calculo = numero % contador 
    if (calculo == 0):
        divisores.append(contador)

print(F'Esses são os divisores do número {numero}: {divisores}')

if (len(divisores) == 2):
    print(f'O número {numero} é um número primo, ou seja, só tem dois divisores!')
