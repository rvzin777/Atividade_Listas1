from statistics import geometric_mean

l=[3, 4, 1, 6, 2, 9]
l.sort(reverse=True)
maiorvalor=l[0]
print('O maior valor da lista é: {}'.format(maiorvalor))
l.sort()
menorvalor=l[0]
print('O menor valor da lista é: {}'.format(menorvalor))
listacompleta=[maiorvalor, menorvalor]
media=geometric_mean(listacompleta)
print('O resultado da media geometrica do menor valor e do maior é: {:.2f}'.format(media))