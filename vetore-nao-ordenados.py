import numpy as np

class VetorNaoOrdenado():
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade,dtype=int)
    
    def insere(self,valor):
        if self.ultima_posicao == self.capacidade - 1:
            print(f'Capacidade máxima atingida.')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def Imprime(self):
        if self.ultima_posicao == - 1:
            print(f'O vetor está vazio.')
        else:
            for i in range(self.ultima_posicao+1):
                print(f'{i} - {self.valores[i]}')
    
    def pesquisar(self,valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def excluir(self,valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao,self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            
            self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.insere(7)


#vetor.Imprime()


#vetor.insere(7)

#print(vetor.ultima_posicao)

#print(vetor.pesquisar(8))
#print(vetor.pesquisar(9))
#print(vetor.pesquisar(3))

#vetor.Imprime()

vetor.excluir(5)

vetor.excluir(1)

vetor.Imprime()