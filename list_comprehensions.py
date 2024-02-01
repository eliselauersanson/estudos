lista = []
for v in [1, 2, 3]:
    for v2 in [4, 5, 6]:
        if v % 2 == 0:
            lista.append((v, v2))

lista2 = [(v, v2)
          for v in [1, 2, 3]
          for v2 in [4, 5, 6]
          if v % 2 == 0]

lista3 = [[i for i in range(4)]
          for v in range(3)
          if v % 2 == 0]

# usando geradores
a = (i for i in range(1_000_000))


def b():
    n = 0
    while True:
        n += 1
        yield n


def evens(limit=10):
    n = 0
    while True:
        n += 2
        if n > limit:
            return
        yield n


def odds(limit=10):
    n = 1
    while True:
        if n > limit:
            return
        yield n
        n += 2


def chain(g1, g2):
    for i in g1:
        yield i
    for i in g2:
        yield i

def chain2(g1, g2):
    yield from g1
    yield from g2


# for i in chain(evens(), odds()):
#     print(i)

# print(next(chain(evens(), odds())))
print(next(evens()))
