import pandas as pd

df = pd.read_csv('busca.csv')
X_df = df[['home','busca','logado']]
Y_df = df['comprou']

X = pd.get_dummies(X_df).values
Y = Y_df.values

print(X,Y)

