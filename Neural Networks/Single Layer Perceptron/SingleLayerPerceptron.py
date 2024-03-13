import pandas as pd

gate = input("Enter the gate in caps: ")
inp = pd.read_csv(f"{gate}.csv")

iterationTables = []
row = len(inp)
learnRate = 1
a = 0
b = 0
c = 1
j = 0

while j != 100:
    print(f"Iteration {j+1}:")
    instance = inp
    instance.loc[0, 'w1'] = a
    instance.loc[0, 'w2'] = b
    instance.loc[0, 'wbj'] = c
    for i in range (row):
        instance.loc[i, 'yin'] = (
                instance.loc[i, 'w1'] * instance.loc[i, 'x1'] +
                instance.loc[i, 'w2'] * instance.loc[i, 'x2'] +
                instance.loc[i, 'wbj'] * instance.loc[i, 'bj']
            )
        instance.loc[i, 'out'] = 0 if instance.loc[i, 'yin'] < 0 else 1
        instance.loc[i, 'nw1'] = instance.loc[i, 'w1'] + (learnRate * (instance.loc[i, 'yt'] - instance.loc[i, 'out']) * instance.loc[i, 'x1'])
        instance.loc[i, 'nw2'] = instance.loc[i, 'w2'] + (learnRate * (instance.loc[i, 'yt'] - instance.loc[i, 'out']) * instance.loc[i, 'x2'])
        instance.loc[i, 'nwbj'] = instance.loc[i, 'wbj'] + (learnRate * (instance.loc[i, 'yt'] - instance.loc[i, 'out']) * instance.loc[i, 'bj'])
 
        if i < row - 1:
            instance.loc[i+1, 'w1'] = instance.loc[i, 'nw1']
            instance.loc[i+1, 'w2'] = instance.loc[i, 'nw2']
            instance.loc[i+1, 'wbj'] = instance.loc[i, 'nwbj']
 
    if len(iterationTables) > 2:
        del iterationTables[0]
 
    a = instance.loc[i, 'nw1']
    b = instance.loc[i, 'nw2']
    c = instance.loc[i, 'nwbj']
    
    for i in range(row):
        instance.loc[i, 'pout'] = 0 if instance.loc[3, 'nw1']*instance.loc[i, 'x1'] + instance.loc[3, 'nw2']*instance.loc[i, 'x2'] + instance.loc[3, 'nwbj']*instance.loc[i, 'bj'] < 0 else 1
 
    sd = (instance['yt'] == instance['pout'])
    instance = instance.astype("int")
    iterationTables.append(instance)
    print(f"{instance}\n")
 
    if sd.all() == True:
        print("Converged.")
        exit(0)
 
    elif j > 0 and iterationTables[0].equals(iterationTables[1]):
        print("Will not be converged due to same previous and current epochs.")
        exit(0)
    j += 1
 