import numpy as np
from kmodes.kmodes import KModes
import pandas as pd
from apyori import apriori
# random categorical data
class Algo():
    def myalgo(self,state,district,city):
        #return "this is my algo"
        dataset=pd.read_csv('media/'+state+'/'+district+'/'+city+'.csv')
        dicti = {row[0] : row[2] for _, row in pd.read_csv("media/matchWithThis.csv").iterrows()}
        gen=dataset.iloc[:,[1,2,3,4,6,7,11,12,15]]
        df1=dataset.iloc[:,[0,1,2,3,4,6,7,11,12,15]]
        #dataset['precaution']=0
        Count_Row=dataset.shape[0] #gives number of row count
        Count_col=dataset.shape[1] #gives number of column count

        location_count=dataset.area.value_counts()
        #cause_count=dataset.cause_of_accidents.value_counts()

        x1=list(set(dataset.iloc[:,0].values))
        y=set(dataset.iloc[:,7].values)
        k=0
        for i in x1:
            k=k+1

        z=pd.Series(location_count,index=x1)

        location_with_precaution={}

        High_location=list(z[z>=(Count_Row/k)].index)
        df1=df1.set_index('area')
        df2=df1.loc[High_location]
        for i in High_location:
            df2=df1.loc[i]
            row=df2.shape[0]
            col=df2.shape[1]
            print(i,":\n")
            #print(col)
            transaction=[]
            rule_in_ap=[]
            rl=[]

            #match=[]
            for ap in range(0,row):
                transaction.append([str(df2.values[ap,rw]) for rw in range(0,col)])
            rules=apriori(transaction,min_support=0.056,min_confidence=0.66,min_lift=2,min_length=3)
            #result=list(rules)
            for s in rules:
                rule_in_ap.append(str(s[0]))
                #print(s[0])
            items={}
            for ap_rul in rule_in_ap:
                if ap_rul in dicti:
                    print(ap_rul)
                    if(None==(items.get(ap_rul))):
                        items[ap_rul]=1
                    else:
                        items[ap_rul]=items.get(ap_rul)+1
            final_rule=[]
            for take in items:
                final_rule.append(dicti.get(take))
            location_with_precaution[i]=final_rule


        Mid_location=list(z[z.between(Count_Row/k-12,Count_Row/k,inclusive=True)].index)
        low_location=list(z[z<Count_Row/k-12].index)
        df3=df1.loc[low_location]

        print(location_with_precaution)

        return(location_with_precaution)
