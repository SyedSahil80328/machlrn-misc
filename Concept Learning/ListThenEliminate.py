import pandas as pd
import numpy as np
from itertools import product

df = pd.read_csv("EnjoySport.csv")
array = np.array(df.iloc[:,:-1])
headers = df.columns
uniq = pd.Series({c:df[c].unique() for c in df})
for i in range(0,len(uniq) - 1):
    uniq[i] = uniq[i].tolist()
    uniq[i].append('?')

versionSpace = [list(x) for x in product(uniq[0], uniq[1], uniq[2], uniq[3], uniq[4], uniq[5])]
versionSpace.append(['0'] * (df.shape[1]-1))
attr = np.array(df.iloc[:,0:-1])
target = np.array(df.iloc[:,-1])

for i, x in enumerate(attr):
    if target[i] == 'Yes':
        to_remove = []
        for j, y in enumerate(versionSpace):
            for k in range(len(x)):
                if x[k] != y[k] and y[k] != '?':
                    to_remove.append(j)
                    break
        for j in sorted(to_remove, reverse=True):
            del versionSpace[j]

hypothesesList = pd.DataFrame(versionSpace)
hypothesesList.columns = headers[:-1]

print("Hypotheses: ")
print(hypothesesList)

def isConsistent(example, hypothesis):
    for attribute, value in example.items():
        if hypothesis[attribute] != '?' and hypothesis[attribute] != value:
            return False
    return True

def filterConsistentHypotheses(hypothesesList, sampleData):
    consistentHypothesesDataframe = hypothesesList[hypothesesList.apply(lambda row: isConsistent(sampleData, row), axis=1)]
    return consistentHypothesesDataframe

consistent = hypothesesList
for i in array:
    dictionaryData = dict()
    for j, h in enumerate(headers[:-1]):
        dictionaryData[h] = i[j]
    consistent = filterConsistentHypotheses(consistent, dictionaryData)

print("Consistent Hypotheses:")
print(consistent)