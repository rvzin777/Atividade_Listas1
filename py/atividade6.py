quantidade = int(input('Quantas turmas tem na escola? '))
soma = 0

for i in range(quantidade):
    alunos = int(input('Quantos alunos tem nessa turma? '))
    soma = soma + alunos

    if alunos >= 40:
        print('Tem uma turma com 40 ou mais alunos.')
        print('Programa encerrado.')
        break

media = soma / quantidade
print(f'A média de alunos por turma é {media}')