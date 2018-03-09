
import pandas as pd


class matchTest():
    dicti = {row[0] : row[1] for _, row in pd.read_csv("precaution.csv").iterrows()}

'''genrated_from_db={}
import itertools
for len in range(3,5):
    for comb in itertools.combinations(values_db, len):
        if(None==(genrated_from_db.get(frozenset(comb)))):
            genrated_from_db[frozenset(comb)]=1
        else:
            genrated_from_db[frozenset(comb)]=genrated_from_db.get(frozenset(comb))+1'''
