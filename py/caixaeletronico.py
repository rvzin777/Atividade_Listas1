print('Seja bem-vindo ao caixa eletrônico')

usuario = 'Ravi1020'
senha = 1234
senha_transacao = 2011

prgnt_usuario = input('NOME DE USUARIO\n')
prgtnt_senha = int(input('SENHA\n'))

if prgnt_usuario == usuario and prgtnt_senha == senha:

    saldo = 200
    opcao = 1

    while opcao != 0:

        print('\nEscolha qual ação você deseja executar')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Ver Saldo')
        print('0. Sair')

        opcao = int(input('Digite sua opção: '))

        if opcao == 1:

            deposito = float(input('Qual valor você deseja depositar: '))

            if deposito > 0:
                cont1 = 0

                while cont1 < 3:

                    prgnt_transacao = int(
                        input('DIGITE SUA SENHA DE TRANSFERÊNCIA\n')
                    )

                    cont1 += 1

                    if prgnt_transacao == senha_transacao:
                        print('SENHA CORRETA')

                        saldo += deposito

                        print(
                            'Seu saldo disponível agora é {:.2f} R$'.format(saldo)
                        )
                        break

                    else:
                        print('SENHA INCORRETA')

                if cont1 == 3 and prgnt_transacao != senha_transacao:
                    print('LIMITE DE TENTATIVAS EXCEDIDO')
                    opcao = 0

            else:
                print('O valor do depósito deve ser maior que zero.')

        elif opcao == 2:

            saque = float(input('Quanto você deseja sacar: '))

            if saque <= 0:
                print('O valor do saque deve ser maior que zero.')

            elif saque > saldo:
                print('Saldo insuficiente.')

            else:
                cont2 = 0

                while cont2 < 3:

                    prgnt_saque = int(
                        input('DIGITE SUA SENHA DE TRANSFERÊNCIA\n')
                    )

                    cont2 += 1

                    if prgnt_saque == senha_transacao:
                        print('SENHA CORRETA')

                        saldo -= saque

                        print(
                            'Seu saldo disponível agora é {:.2f} R$'.format(saldo)
                        )
                        break

                    else:
                        print('SENHA INCORRETA')

                if cont2 == 3 and prgnt_saque != senha_transacao:
                    print('LIMITE DE TENTATIVAS EXCEDIDO')
                    opcao = 0

        elif opcao == 3:

            print('Seu saldo é {:.2f} R$'.format(saldo))

        elif opcao == 0:

            print('Saindo...')

        else:

            print('Opção inválida!')

    print('Caixa eletrônico encerrado.')

elif prgnt_usuario != usuario:

    print('Nome de usuário inválido.')

elif prgtnt_senha != senha:

    print('Senha inválida.')