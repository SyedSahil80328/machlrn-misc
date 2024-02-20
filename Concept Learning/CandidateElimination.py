import numpy as np 
import pandas as pd

data = pd.read_csv('EnjoySport.csv')
concepts = np.array(data.iloc[:,0:-1])
target = np.array(data.iloc[:,-1])

def learn(concepts, target): 
    specificHypothesis = concepts[0].copy()  
    print(f"Initial Specific Hypothesis {specificHypothesis}.") 
    generalHypothesis = [["?" for _ in range(len(specificHypothesis))] for _ in range (len(specificHypothesis))]     
    print(f"Initial General Hypothesis \n{generalHypothesis}")

    for i, h in enumerate(concepts):
        if target[i] == "yes":
            print("If instance is Positive")
            for x in range(len(specificHypothesis)): 
                if h[x]!= specificHypothesis[x]:                    
                    specificHypothesis[x] ='?'                     
                    generalHypothesis[x][x] ='?'
                   
        if target[i] == "no":            
            print("If instance is Negative")
            for x in range(len(specificHypothesis)): 
                if h[x]!= specificHypothesis[x]:                    
                    generalHypothesis[x][x] = specificHypothesis[x]                
                else:                    
                    generalHypothesis[x][x] = '?'        

        print(f"Step {i+1}:-")
        print(specificHypothesis)         
        print(f"{generalHypothesis}\n")

    indices = [i for i, val in enumerate(generalHypothesis) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        generalHypothesis.remove(['?', '?', '?', '?', '?', '?']) 
    return specificHypothesis, generalHypothesis 

finalSpecific, finalGeneral = learn(concepts, target)

print(f"Final Specific Hypothesis: {finalSpecific}.")
print(f"Final General Hypothesis: {finalGeneral}.")
