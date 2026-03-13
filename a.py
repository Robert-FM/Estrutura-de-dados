lista = []

for i in range(0,5):
    number = int(input(f'Digite o valor: '))

    if len(lista) == 0 or number > lista[-1]:
        lista.append(number)
        print(f'Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if number <= lista[pos]:
                lista.insert(pos, number)
                print(f'Adicionado na posição {pos}º da lista.')
                break
            pos += 1
print('-=-'*30)
print(f'Os valores digitados em ordem foram {lista}.')
