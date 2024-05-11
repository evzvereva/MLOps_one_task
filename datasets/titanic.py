from catboost.datasets import titanic

df = titanic()[0]
df_new = df[['Pclass', 'Sex', 'Age']]
df_new.to_csv("titanic.csv", index=False)
