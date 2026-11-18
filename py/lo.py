salario=float(input('Me diga seu salário: '))
print('1.Progamador de Sistemas')
print('2.Analisador de Sistemas')
print('3.Analisador de Banco de dados')
cargo=int(input('Me diga o seu cargo: '))

if cargo==1:
    Ps= salario * 30 / 100
    print('Você como Progamador de Sistemas irá receber {:.2f}.'.format(Ps+salario))

elif cargo==2:
    As= salario * 20 / 100
    print('Você como Analisador de Sistemas irá receber {:.2f}.'.format(As+salario))

elif cargo==3:
    Abd= salario * 15 / 100
    print('Você como Analisador de Banco de Dados irá receber {:.2f}'.format(Abd+salario))

else:
    print('Digite um cargo válido!')
    

