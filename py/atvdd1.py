respostas = 0

resposta = input("Telefonou para a vítima? (s/n): ")
if resposta.lower() == "s":
    respostas += 1

resposta = input("Esteve no local do crime? (s/n): ")
if resposta.lower() == "s":
    respostas += 1

resposta = input("Mora perto da vítima? (s/n): ")
if resposta.lower() == "s":
    respostas += 1

resposta = input("Devia para a vítima? (s/n): ")
if resposta.lower() == "s":
    respostas += 1

resposta = input("Já trabalhou com a vítima? (s/n): ")
if resposta.lower() == "s":
    respostas += 1

if respostas == 2:
    print("Suspeita")
elif respostas == 3 or respostas == 4:
    print("Cúmplice")
elif respostas == 5:
    print("Assassino")
else:
    print("Inocente")
