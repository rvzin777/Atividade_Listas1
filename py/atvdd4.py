v=float(input('Quantas maças você comprou ?: '))
qnt1= v*0.30
qtn2= v*0.25
if v<=12:
    print('Você vai pagar :{}'.format(qnt1))
elif v>12:
    print('Você vai pagar: {}'.format(qtn2))