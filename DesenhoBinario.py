# Juan #



entrada1 = '''
010
111
000
101'''

entrada2 = '''
10101
10101
11111'''

entrada3 ='''
0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''




def binario(matriz_entrada):
    regiao = []
    principalMatriz = []
    bin1, bin0 = '10'
    
    def ligacao(aux1, aux2):        
        if aux1 == aux2:
            return
        regiao[aux1].extend(regiao[aux2])
        regiao.remove(regiao[aux2])
    def verificaRegiao(linha, coluna):        
        for i in regiao:
            if (linha, coluna) in i:
                return regiao.index(i)    
    
    for linha_entrada in matriz_entrada.splitlines():
        if len(linha_entrada) > 0:
            principalMatriz.append(list(linha_entrada))		
    tamanhoMatriz = len(principalMatriz)
    tamanhoLinha = len(linha_entrada)
    

    def verificaSuperior(linha,coluna):
        teste = bin1
        if linha == 0:
            return False
        teste = (principalMatriz[linha-1][coluna] == teste)
        return teste

    def verificaEsquerda(linha,coluna):
        teste = bin1
        if coluna == 0:
            return False
        teste = (principalMatriz[linha][coluna-1] == teste)
        return teste

    for i in range(tamanhoMatriz):
        for j in range(tamanhoLinha):
            if principalMatriz[i][j] == bin1:
                aux1 = -1
                aux2 = -1   
                if verificaSuperior(i , j):
                    aux1 = verificaRegiao(i-1 , j)
                    regiao[aux1].append((i,j))
                if verificaEsquerda(i , j ):
                    aux2 = verificaRegiao(i , j-1)
                    if aux1 != -1:
                        ligacao(aux1 , aux2)
                    else:                               
                        regiao[aux2].append((i , j))
                if aux1 == -1 and aux2 == -1:
                    regiao.append([(i,j)])            

    cont = 1
    for r in regiao:
        for l, c in r:
            principalMatriz[l][c] = str(cont)
        cont +=1

    print ('\nSaída:')
    for linha in principalMatriz:
        print (''.join(linha))
		
binario(entrada1)
binario(entrada2)
binario(entrada3)
