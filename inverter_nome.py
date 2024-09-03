"""Escreva um programa que inverta os caracteres de um string"""
def inverter_nome():
    nome = input('Olá, irei inverter as letras do seu nome. Para começar, digite seu nome: ')
    if nome:
        print(f'Seu nome invertido é {nome[::-1]}')
    else:
        print('Por favor, tente novamente.')

inverter_nome()

"""Sem utilizar o [::-1]:"""

