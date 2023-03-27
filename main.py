anoatual = int(input('Em que ano estamos: '))
idade = int(input('Quantos anos você tem: '))
outroano = int(input('Ano que deseja saber sua idade: '))
nome = str(input('Escreva seu nome: '))

idadefutura = idade + (outroano - anoatual)
print(f'{nome}, no ano de {outroano} você terá {idadefutura} anos')

