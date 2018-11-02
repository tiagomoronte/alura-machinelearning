import csv

def carregar_acessos():

    X = []
    Y = []

    arquivo = open('acesso.csv', 'rt')
    leitor = csv.reader(arquivo)

    next(leitor)

    for acessou_home,acessou_como_funciona,acessou_contato,comprou in leitor:
        X.append([int(acessou_home),int(acessou_como_funciona),int(acessou_contato)])
        Y.append(int(comprou))
    return X, Y

def carregar_busca():

    X = []
    Y = []

    arquivo = open('busca.csv', 'rt')
    leitor = csv.reader(arquivo)

    next(leitor)

    for home,busca,logado,comprou in leitor:
        X.append([int(home),busca,int(logado)])
        Y.append(int(comprou))
    return X, Y
