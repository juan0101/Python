######################################################################################################################################
#############################################                                            #############################################
#############################################                JUAN VINICIUS               #############################################
#############################################                                            #############################################
######################################################################################################################################
def combinacoes(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinacoes(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutacoes(items):
    return combinacoes(items, len(items))

pessoas = []
damas = []
pretendentes = {}

print ("Exercício A - Casamento")
print ("Lendo arquivo...")
casamento_txt = open('casamento.txt', 'r')
for linha in casamento_txt.readlines():
    linha = linha.split()
    damas.append(linha[0])
    pretendentes[linha[0]] = linha[1:]
    for i in linha:
        if i not in pessoas:
            pessoas.append(i)
casamento_txt.close()

def formatarPar(par):
    global damas
    if par[1] == None:
        return par
    elif par[0] in damas:  
        conjuge_1 = par[0]
        conjuge_2 = par[1]
    else:
        conjuge_1 = par[1]
        conjuge_2 = par[0]
    return([conjuge_1, conjuge_2])


def validarPossibilidade(p):
    global pretendentes
    for par in p:
        par_formatado = formatarPar(par)
        dama = par_formatado[0]
        if par_formatado[1]:
            if dama in pretendentes:
                pretendentes_dama = pretendentes[dama]
                if par_formatado[1] not in pretendentes_dama:
                    return False
            else:
                return False
        else:
            return False
    return True
        

print ("Gerando todas as possibilidades...")
possibilidades = []
total_possibilidades = 0
for p in permutacoes(pessoas):
    total_possibilidades += 1
    n_pares = 0
    solteiro = False
    if len(p) % 2 == 0:
        n_pares = int(len(p) / 2)
    else:
        n_pares = int((len(p)-1) / 2)
        solteiro = True
    pessoa_i = 0
    possibilidade = []
    for par_i in range(0,n_pares-1):
        par = [p[pessoa_i], p[pessoa_i+1]]
        pessoa_i += 2
        possibilidade.append(par)
    if solteiro:
        possibilidade.append([p[-1], None])
    possibilidades.append(possibilidade)

print ("Validando todas as possibilidades...")
casaram = False
for p in possibilidades:
    if validarPossibilidade(p):
        casaram = True
        print("Pronto! Segue abaixo os casais:")
        for par in p:
            print(formatarPar(par))
        break
if not casaram:
    print ("Em nenhuma das possibilidades as damas ficaram sempre com seus pretendentes.")


def combinacoes2(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinacoes2(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutacoes2(items):
    return combinacoes2(items, len(items))

tavola_opcao = []
tavola = open('cavaleiros.txt','r')
cavaleiros = {}

for linha in tavola:
    linha.replace("\r","")
    tavola_opcao.append(linha.split())
for lista in tavola_opcao:
    cavaleiros[lista[0]] = lista[1:]
print ('Permutações')

for p in permutacoes2(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
    indice = 0
    while indice < 6:
        amigo = p[indice + 1]
        if amigo in cavaleiros[p[indice]]:
            indice += 1
        else:
            break
    if indice == 6:
        amigo = p[0]
        if amigo in cavaleiros[p[indice]]:
            print(p)
            break
if indice < 6:
    print('Não é possível arrumar a mesa para os 7 cavaleiros')
else:
    print('Mesa Arrumada')
        
