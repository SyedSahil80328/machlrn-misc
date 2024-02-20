import pandas as pd
import numpy as np


dataset = np.array(pd.read_csv('EnjoySport.csv'))
print(f"The total number of training instances are {len(dataset)}.")

numAttribute = len(dataset[0]) - 1

hypothesis = ['\u03C6'] * numAttribute
print(f"Initial Hypothesis h0: {hypothesis}.\n")

for i, ele in enumerate(dataset):
    print(f"Row to use now: {ele[:-1]} (row {i+1}).")
    print(f"Current Hypothesis: h{i} = {hypothesis}.")
    if ele[numAttribute] == 'yes':
        for j in range(numAttribute):
            if hypothesis[j] == '\u03C6' or hypothesis[j] == ele[j]:
                hypothesis[j] = ele[j]
            else:
                hypothesis[j] = '?'
    print(f"Hypothesis after comparison: h{i+1} = {hypothesis}.\n")

print(f"Maximally Specific Hypothesis is h{i+1} = {hypothesis}.")