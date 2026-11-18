print (30*'*')
print('      CÁLCULO DE GRANDEZAS ELÉTRICAS')
print (30*'*')
print('1.Tensão em volt')
print('2.Resistência em Ohm')
print('3.Corrente em anpere')

calculo=int(input('Qual cálculo você deseja realizar? '))

if calculo==1:
    r=int(input('informe o valor da sua resistência: '))
    core=int(input('informe o valor da sua corrente: '))
    t= r *core
    print('O valor da tensão é {}'.format(t))

elif calculo==2:
    ten=int(input('informe o valor da sua tensão: '))
    cor=int(input('informe o valor da sua corrente: '))
    re= ten * cor
    print('o valor da resistência é {}'.format(re))

elif calculo==3:
    te=int(input('Informe o valor da sua tensão: '))
    res=int(input('informe o valor da sua resistência: '))
    co= te*res
    print('O valor da sua corrente é {}'.format(co))

else:
    print('digite um número de 1 a 3 ')
