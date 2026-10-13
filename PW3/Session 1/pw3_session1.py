import pandas as pd,numpy as np,matplotlib.pyplot as plt
from scipy import stats

# 1. Load
df=pd.read_csv("heart.csv")
print(df.shape); print(df.head())
cols=["age","chol","trestbps","thalach"]
X=df[cols]; print(X.describe().round(2))

# 2. Shape: histogram + KDE + normal fit
fig,ax=plt.subplots(2,2,figsize=(10,7))
for a,c in zip(ax.ravel(),cols):
    x=X[c].dropna()
    a.hist(x,bins=20,density=True,alpha=.6,edgecolor="k")
    g=np.linspace(x.min(),x.max(),300)
    a.plot(g,stats.gaussian_kde(x)(g),label="KDE")
    a.plot(g,stats.norm.pdf(g,x.mean(),x.std()),"--",label="normal fit")
    a.set_title(c); a.legend()
plt.tight_layout(); plt.savefig("fig_distributions.png",dpi=150); plt.close()

# 3. Normality: Q-Q plots + tests
fig,ax=plt.subplots(2,2,figsize=(8,7))
for a,c in zip(ax.ravel(),cols):
    stats.probplot(X[c].dropna(),dist="norm",plot=a); a.set_title(f"Q-Q: {c}")
plt.tight_layout(); plt.savefig("fig_qq.png",dpi=150); plt.close()

rows=[]
for c in cols:
    x=X[c].dropna().values
    W,p=stats.shapiro(x)
    rows.append(dict(var=c,n=len(x),skew=stats.skew(x),exkurt=stats.kurtosis(x),shapiro_W=W,shapiro_p=p,dagostino_p=stats.normaltest(x).pvalue))
res=pd.DataFrame(rows).round(4); print(res.to_string(index=False))
