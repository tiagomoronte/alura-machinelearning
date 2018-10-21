from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB


X, Y = carregar_acessos()

print(X,Y)

modelo = MultinomialNB()
modelo.fit(X, Y)

print(modelo.predict([[1,0,1]]))

