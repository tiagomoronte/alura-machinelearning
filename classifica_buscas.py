import pandas as pd
from collections import Counter

df = pd.read_csv('busca.csv')
X_df = df[['home','busca','logado']]
Y_df = df['comprou']

X = pd.get_dummies(X_df).values
Y = Y_df.values

porcentagem_de_treino = 0.9
tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_teste = int(len(Y) - tamanho_de_treino)

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]
teste_dados = X[-tamanho_teste:]
teste_marcacoes = Y[-tamanho_teste:]

def fit_and_predict(modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):

    modelo.fit(treino_dados, treino_marcacoes)
    resultado = modelo.predict(teste_dados)

    acertos = resultado == teste_marcacoes
    total_de_acertos = sum(acertos)
    total_de_elementos = len(teste_dados)
    taxa_acertos = total_de_acertos / total_de_elementos

    taxa_acerto_base = max(Counter(teste_marcacoes).values()) / len(Y)

    print(taxa_acerto_base)
    print(taxa_acertos)



from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

fit_and_predict(modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from sklearn.ensemble import AdaBoostClassifier
modelo = AdaBoostClassifier()

fit_and_predict(modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

