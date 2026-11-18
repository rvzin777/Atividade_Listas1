# # frutas = []
# # for i in range(5):
# #     prg=input('Diga a fruta que você que adicionar: ')
# #     frutas.append(prg)

# # print('Suas frutas são {}'.format(frutas))

# Q2

# numeros=[10, 20, 30, 40, 50]
# print('Seus números são: {}'.format(numeros))
# numeros.sort(reverse=True)
# print('Seus números em ordem decresente é {}'.format(numeros))

#Q3

# alunos=['Ravi', 'Arthur', 'Enzo']
# print('Sua lista de alunos é {}'.format(alunos))

# for i in range(2):
#     aluno_novo=input('Me diga o nome do seu novo aluno: ')
#     alunos.append(aluno_novo)

# print('Sua lista atualizada é {}'.format(alunos))

#Q4

# linguagem= ['Python', 'Java', 'C++', 'Php']
# print('Sua lista é {}'.format(linguagem))
# linguagem.insert(2, "Java Scrit")

# print('sua lista depois é :{}'.format(linguagem))

#Q5

# numeros=[1, 2, 3, 4, 5, 6]
# print('Sua lista antes da remoção é {}'.format(numeros))
# numeros.pop()
# print('Sua lista depois da remoção é: {}'.format(numeros))

#Q6

# cores=['azul', 'verde', 'vermelho', 'verde', 'amarelo']
# cores.remove('verde')
# print(cores)

#Q7

# animais=['vaca', 'cavalo', 'rã', 'passaro', 'soin']
# del animais[3]
# print(animais)

#Q8
import random

lista=[]
while range !=0:
    prgnt=input('Você que adiconar um nome ? S/N ')
    prgnt.upper()

    if prgnt == 'S':
        add_l= input('Qual nome você que adicionar a lista? ')
        lista.append(add_l) 

    if prgnt == 'N':
        break

    else:
        print('Diga uma opção valida')

random.shuffle(lista)
vencedor=random.choice(lista)
print('O vencedor é: {}'.format(vencedor))