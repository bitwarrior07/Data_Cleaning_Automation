import pandas as pd
import numpy as np

df=pd.read_csv('E:/varun/data science lab/data cleaning/Loan_data.csv')
col=list(df.columns)
ncol=list()
sizedf=np.size(df,axis=0)
print(df)

def null_val(ncol):
    c=0
    
    while c<len(ncol):
        l=list(df[ncol[c]])
        ulist=list(pd.unique(l))
        clist=list()
        #count of uval
        for i in ulist:
            count=0
            for j in l:
                if j==i:
                    count=count+1
            clist.append(count)
        
        ccl=0
        for x in clist:
            if x>1:
                ccl=ccl+1
            else:
                continue
        max_cl=max(clist)
        ind_max=clist.index(max_cl)
        val_max=ulist[ind_max]
        
        #int
        if df[ncol[c]].dtype==int or df[ncol[c]].dtype==np.short:
            #categorical
            if ccl>1:
                df[ncol[c]].fillna(val_max,inplace=True)

            #non-categorical
            if ccl==0:
                if sizedf>10000:
                    df[ncol[c]].dropna(inplace=True)
                else:
                    mn=df[ncol[c]].mean()
                    df[ncol[c]].fillna(round(mn),inplace=True)                
        
        #object
        elif df[ncol[c]].dtype==object or df[ncol[c]].dtype==str or df[ncol[c]].dtype==np.character:
            #normalize
            idx=0
            while idx<len(ulist):
                ulist[idx]=str(ulist[idx]).capitalize()
                ulist[idx]=str(ulist[idx]).strip()
                idx=idx+1

            #non categorical
            if ccl==0:
                if sizedf>10000:
                    df[ncol[c]].dropna(inplace=True)
                else:            
                    if max(clist)==1:
                        df[ncol[c]].fillna("-",inplace=True)
                        
                    else:
                        df[ncol[c]].fillna(method='bfill',inplace=True)
            
            #categorical
            if ccl>1:
                df[ncol[c]].fillna(val_max,inplace=True)
            
            dfi=0
            for n in df[ncol[c]].isnull():
                if n==True:
                    pass
                else:
                    df[ncol[c]][dfi]=str(df[ncol[c]][dfi]).capitalize()
                    df[ncol[c]][dfi]=str(df[ncol[c]][dfi]).strip()
                dfi=dfi+1

        #float
        elif df[ncol[c]].dtype==float or df[ncol[c]].dtype==np.double or df[ncol[c]].dtype==np.longfloat or df[ncol[c]].dtype==np.longdouble or df[ncol[c]].dtype==np.float64:
            #categorical
            if ccl>1:
                df[ncol[c]].fillna(val_max,inplace=True)

            #non-categorical
            if ccl==0:
                if sizedf>10000:
                    df[ncol[c]].dropna(inplace=True)
                else:
                    mn=df[ncol[c]].mean()
                    df[ncol[c]].fillna(round(mn,3),inplace=True)
        
        else:
            pass
        c=c+1
    

#nullval
for i in range(len(col)):
    for j in df[col[i]].isnull():
        if j==True:
            ncol.append(col[i])
            break
    else:
        pass

#nullval
if len(ncol)>0:
    null_val(ncol)
ndf=df
print(ndf)
path1='E:/varun/code/datacleaning/data.csv'
ndf.to_csv(path1)