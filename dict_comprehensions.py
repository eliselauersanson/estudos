from collections import Counter
with open('text.txt', 'r') as t:
    text = t.read()

def func1(text):
    chars = []
    quantity = []
    for c in text:
        if not c in chars:
            chars.append(c)
            quantity.append(1)
        else:
            index = chars.index(c)
            quantity[index] += 1
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]

    return d
def func2(text):
    chars = set()
    for c in text:
        chars.add(c)
    chars = list(chars)
    quantity = [text.count(c) for c in chars]
    d = {}
    for i in range(len(chars)):
        print(i)
        d[chars[i]] = quantity[i]
    print(d)

def func3(text):
    chars = list({ c for c in text })
    quantity = [text.count(c) for c in chars]
    d = {}
    for i in range(len(chars)):
        print(i)
        d[chars[i]] = quantity[i]
    print(d)

def func4(text):
    chars = list({ c for c in text })
    quantity = [(c, text.count(c)) for c in chars]
    return dict(quantity)

def func5(text):
    return dict([(c, text.count(c)) for c in set(text)])

def func6(text):
    return {c: text.count(c) for c in set(text)}

def func7(text):
    return Counter(text)
    # return Counter(text).most_common(4)

print(func7(text))