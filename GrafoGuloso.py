#JUAN#

from random import choice

def montarDic():
    grafo = {}
    grafo[1] = [6, 7]
    grafo[2] = [3, 7]
    grafo[3] = [2, 4, 6, 7]
    grafo[4] = [3, 7]
    grafo[5] = [7]
    grafo[6] = [1, 3]
    grafo[7] = [1, 2, 3, 4, 5]
    return grafo
    
def menor(grafo):
    menor = choice(list(grafo.keys())) #sortea um key qualquer para comparar
    grafo_menor = grafo[menor] #grafo a ser comparado
    for i in grafo: #percorrer lista de vertice
        if len(grafo[i]) < len(grafo_menor): #comparar menor numero de vizinhos
            grafo_menor = grafo[i] #grafo_menor recebe o menor grafo
            menor = i   #indice do menor grafo
        if len(grafo[i]) == len(grafo_menor): #se os vertices tiverem o mesmo numero de vizinhos, pega o menor indice
            if i < menor:
                grafo_menor = grafo[i]
                menor = i
    return menor #retorn o indice do menor grafo

def resultadoAdd(menor_indice):
    resultado.append(menor_indice) #adiciona o indice na resposta
    print(resultado)

def remover_indice(menor_indice):
    for i in grafo: #varredura dos vertices do grafo
        if menor_indice in grafo[i]: #verifica se o indice é vizinho de alguem
            grafo[i].remove(menor_indice) #se for vizinho, remove da lista de vizinho

def remover_conteudo(conteudo_grafo):
    aux = 0
    while aux != len(conteudo_grafo):
        remover_indice(conteudo_grafo[aux])
        grafo.pop(conteudo_grafo[aux])
        conteudo_grafo.pop(aux)
        
resultado = []
grafo = montarDic()
while grafo != {}:
    indice_menor_grafo = menor(grafo) #indice do grafo com menos vizinhos
    resultadoAdd(indice_menor_grafo) #adiciona o indice no vetor de resultado
    lista_conteudo = grafo[indice_menor_grafo] #lista de vizinho do menor indice
    remover_indice(indice_menor_grafo) #remove o indice das vertices que eram seus vizinhos
    grafo.pop(indice_menor_grafo) #remove o indice do grafo
    remover_conteudo(lista_conteudo) #remove o conteudo do indice





