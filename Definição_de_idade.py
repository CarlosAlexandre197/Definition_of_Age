'''1...12 é Criança, 13...17 é Adolescente, 18...65 é Adulto, acima de 65... é Idoso.
Sabendo das informções acima. Faça um programa que leia o nome e a idade de uma pessoa e imprima na tela:
seu nome e se é uma criança, adolescente, adulto ou idoso.'''

nome = str(input('Qual é o seu nome? '))
idade = int(input('Qual é a sua idade? '))


if (idade >= 1) and (idade < 13):
    print(f'{nome}, criança!')

elif (idade >= 13) and (idade < 18):
    print(f'{nome}, adolescente!')

elif (idade >= 18) and (idade < 65):
    print(f'{nome}, adulto!')

elif (idade >= 65):
    print(f'{nome}, idoso!')
