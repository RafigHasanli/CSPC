import pandas as pd,numpy as np
from scipy import stats
import matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
out=[]
def P(*a):
    s=" ".join(str(x) for x in a);print(s);out.append(s)

df=pd.read_csv("heart.csv")
d=df[df.target==1].thalach;h=df[df.target==0].thalach
t,p=stats.ttest_ind(d,h,equal_var=False);P("Welch t=",t,"p=",p)
u,pu=stats.mannwhitneyu(d,h);P("Mann-Whitney U=",u,"p=",pu)
for n,g in (("disease",d),("healthy",h)):
    P(n,"n=",len(g),"mean=",g.mean(),"SEM=",g.sem(),"CI95=+-",1.96*g.sem())
plt.figure()
plt.errorbar(["Disease","Healthy"],[d.mean(),h.mean()],yerr=[1.96*d.sem(),1.96*h.sem()],fmt="o",capsize=6)
plt.ylabel("thalach (bpm)");plt.title("Mean +- 95% CI");plt.savefig("thalach_means.png",dpi=150)

r,pr=stats.pearsonr(df.age,df.thalach);rho,ps=stats.spearmanr(df.age,df.thalach)
P("age-thalach Pearson r=",r,"p=",pr,"| Spearman rho=",rho,"p=",ps)
plt.figure();plt.scatter(df.age,df.thalach,s=10)
plt.xlabel("age");plt.ylabel("thalach");plt.savefig("age_thalach.png",dpi=150)

c=pd.read_csv("chemicals_cancer.csv")
mal,pol,ben,cad="malignancy","pollution_index","benzene","cadmium"
P("NAIVE corr with malignancy:",{k:round(c[k].corr(c[mal]),3) for k in (ben,cad)})
P("pollution corr with:",{k:round(c[pol].corr(c[k]),3) for k in (ben,cad,mal)})

q=c[pol].quantile
s=c[(c[pol]>q(.4))&(c[pol]<q(.6))]
P("RESTRICTED (pollution 40-60th percentile) n=",len(s),{k:round(s[k].corr(s[mal]),3) for k in (ben,cad)})
c["bin"]=pd.qcut(c[pol],5,labels=False)
for k in (ben,cad):
    P("per-bin corr",k,[round(g[k].corr(g[mal]),3) for _,g in c.groupby("bin")])
res=lambda y:y-np.polyval(np.polyfit(c[pol],y,1),c[pol])
P("PARTIAL corr (controlling pollution):",{k:round(np.corrcoef(res(c[k]),res(c[mal]))[0,1],3) for k in (ben,cad)})
fig,ax=plt.subplots(1,2,figsize=(10,4))
for a,k in zip(ax,(ben,cad)):
    a.scatter(c[k],c[mal],s=5,c=c[pol],cmap="viridis");a.set_xlabel(k);a.set_ylabel(mal)
plt.savefig("chemicals.png",dpi=150)

pp=df.target.value_counts(normalize=True);H=-(pp*np.log2(pp)).sum()
P("target proportions:",pp.round(3).to_dict(),"entropy H(bits)=",H)
open("results.txt","w").write("\n".join(out))
