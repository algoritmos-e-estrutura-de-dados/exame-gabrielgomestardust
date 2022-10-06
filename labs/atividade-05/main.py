def maximizar_troca_de_figurinhas(figurinhaMaria, figurinhaJoao):
    max_trocas = 0
    contador = 0
    
    if (figurinhaMaria) < (figurinhaJoao):
        menor_qtd = figurinhaMaria  
    else: 
        menor_qtd = figurinhaJoao

    max_trocas = int(menor_qtd)

    while contador <= max_trocas:
        if figmaria == figjoao:
            if max_trocas == 0: 
                max_trocas = 0   
            else: 
                max_trocas = max_trocas -1
        contador = contador + 1
    return max_trocas

if __name__ == '__main__':
    A, B = input().split(' ')
    figmaria = [input().split(' ')]
    figjoao = [input().split(' ')]
    print(maximizar_troca_de_figurinhas(A, B))