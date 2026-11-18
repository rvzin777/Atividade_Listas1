#Q1
# a=int(input('Me informe seu primeiro número: '))
# b=int(input('Me informe seu segundo número: '))
# cont=0

# if a<b:
#     for i in range(a, b):
#         cont= cont+i
#         print(cont)
# else:
#     print('ERRO')

#Q2
# t1=int(input('Me informe seu primeiro termo: '))
# t2=int(input('Me informe sua quantidade de termos: '))
# t3=int(input('Me informe sua razão: '))

# for i in range(t1, t2, t3):
#     print(i)

#Q3
qntd=int(input('Me diga a quantidade de medicamentos que você tem: '))
mnrprec=1000000000000000000000000000000
pdtbarat=''
cont=0
for a in range(qntd):
    nome=input('Me diga o nome do seu produto: ')
    preco=float(input('Me diga o preço do produto: '))
    cont= cont + preco

    if preco < mnrprec:
        mnrprec = preco
        pdtbarat = nome
m=cont/qntd
print('O {} custa {:.2f} e é o produto com menor valor'.format(pdtbarat, mnrprec))
print('A media aritimetrica de seus produtos é {:.1f}'.format(m))
        

