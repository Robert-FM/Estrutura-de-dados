expr = input('Digite a expressão: ')
pilha = []

pares = {')':'(',']':'[','}':'{'}

for i in expr:

    if i in pares.values():
        pilha.append(i)

    elif i in pares.keys():
        if not pilha or pilha.pop() != pares[i]:
            pilha.append(i)
            break

if not pilha:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
