import random
quantida_de_rifas=int(input('Quantas rifas você vendeu?: '))
compradores=[]
for i in range (quantida_de_rifas):
    nome_pessoas=input('Me diga o nome do seu compadro: ')
    compradores.append(nome_pessoas)

print('O vencedor de sua rifa foi: ',random.choice(compradores))