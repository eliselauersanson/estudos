# i = 1
# while i <= 10:
#     print(i)
#     i += 1

for i in range(1, 11):
    print(i)

a = [1, 2, 3, 4]

# for i in range(len(a)):
#     print(a[i])

for i in a:
    print(i)

a = ' AIUHSDIUNSAD OASI JDOASI OASJD OIAWJe '
for letra in a:
    print(letra)

nomes = ['Elise', "caio", "ilse"]
idades = [27, 28, 59]

for i in range(len(nomes)):
    print(f'{nomes[i]} tem idade {idades[i]} anos')

for nome, idade in zip(nomes, idades):
    print(f'{nome} tem idade {idade} anos')

# with open('text.txt') as arquivo:
#     numero = 1
#     for linha in arquivo:
#         print(numero, ' ',linha)
#         numero += 1

with open('text.txt') as arquivo:
    for n, linha in enumerate(arquivo, start=1):
        print(n, ' ',linha)


a = {"will": 10, "maria": 30, "aline": 22}
# mais_velha = 0
# for k, v in a.items():
#     if v > mais_velha:
#         mais_velha = v
#     print(k,'->', v)
#     print(mais_velha)

for k, v in a.items():
    print(k,'->', v)
print(f'o  mais velho tem {max(a.values())}')

cols = 5
linhas = 5
achou = False
for linha in range(linhas):
    for col in range(cols):
        if linha == 3 and col ==3:
            achou = True
    if achou:
        break

for linha, col in ((l, c) for l in range(linhas) for c in range(cols)):
    if linha ==4 and col ==3:
        print('aqui', col, linha)
        break
