#psycopg2
import main as m
import psycopg2
import pandas as pd
import numpy as np

df1=pd.DataFrame(m.ndf)
conn=psycopg2.connect(dbname="cleanerdb",user="postgres",password="postgres",host="localhost")
cursor=conn.cursor()
val=tuple(df1.values)
a=list(df1.columns)
c=0
dfdtype=list()

for i in range(len(a)):
    dfdtype.append(df1[a[i]].dtype)

def insert_val(x):
    ind=0
    s="""INSERT INTO data VALUES("""
    while ind<len(val[x]):
        if ind==len(val[x])-1:
            if type(val[x][ind])==str or type(val[x][ind])==object:
                s=s+"'"+val[x][ind]+"'"+")"
            else:
                s=s+str(val[x][ind])+')'
        else:
            if type(val[x][ind])==str or type(val[x][ind])==object:
                s=s+"'"+val[x][ind]+"'"+','
            else:
                s=s+str(val[x][ind])+','
        ind=ind+1
    cursor.execute(s)

#create the table name under the file name--now just temporary
cursor.execute("""DROP TABLE data;""")
cursor.execute("""CREATE TABLE data();""")
while c<len(a):
    if dfdtype[c]==int:
        cursor.execute("""ALTER TABLE data ADD COLUMN """+a[c]+""" INT;""")
    elif dfdtype[c]==float:
        cursor.execute("""ALTER TABLE data ADD COLUMN """+a[c]+""" FLOAT;""")
    elif dfdtype[c]==object or dfdtype[c]==str:
        cursor.execute("""ALTER TABLE data ADD COLUMN """+a[c]+""" VARCHAR(100);""")
    else:
        cursor.execute("""ALTER TABLE data ADD COLUMN """+a[c]+""" VARCHAR(100);""")
    c=c+1

for x in range(len(val)):
    insert_val(x)
conn.commit()
conn.close()