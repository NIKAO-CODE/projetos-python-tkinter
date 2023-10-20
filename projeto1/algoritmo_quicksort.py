def geral():
    def quicksort(lista, esquerda, direita):
        '''Verifica se a lista tem pelo menos 2 elementos.
        Depois define a variável que recebe a posição exata do pivô.
        Chama a função quick sort nas sub listas que nesse momento são:
        esquerda: elementos menores que o pivô.
        direita: elementos maiores que o pivô.'''
        
        if (esquerda < direita):
            p = particao(lista, esquerda, direita)
            quicksort(lista, esquerda, p - 1)
            quicksort(lista, p + 1, direita)


    def particao(lista, esquerda, direita):
        pivot = lista[direita]
        i = esquerda

        for j in range(esquerda, direita):
            if (lista[j] <= pivot):
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
        lista[i], lista[direita] = lista[direita], lista[i]

        return i


    lista = [22, 11, 88, 77, 45, 4, 23, 7]
    quicksort(lista, 0, len(lista)-1)

if __name__ == '__main__':
    geral()