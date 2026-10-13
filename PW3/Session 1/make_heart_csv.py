import pandas as pd
cols=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","num"]
df=pd.read_csv("processed.cleveland.data",header=None,names=cols,na_values="?")
df["target"]=(df["num"]>0).astype(int)   # 0=no disease, 1..4 -> 1=disease
df=df.drop(columns="num")
df.to_csv("heart.csv",index=False)
print(df.shape)
