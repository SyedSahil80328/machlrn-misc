import math
with open ("DataForMLP.csv", "r") as file:
    lines = file.readlines()
    inputs = list(map(float, lines[0].strip().split(',')))
    weightsFirstLayer = list(map(float, lines[1].strip().split(',')))
    weightsSecondLayer = list(map(float, lines[2].strip().split(',')))
    otherData = list(map(float, lines[3].strip().split(',')))

    weightsFirstLayer = [weightsFirstLayer[i:i+len(inputs)] for i in range (0, len(weightsFirstLayer), len(inputs))]
    print(weightsFirstLayer)

def calculateHiddenLayer(node):
    h = 0
    for i, val in enumerate(inputs):
        h = h + val*weightsFirstLayer[node][i]
    
    outH = 1 / (1 + math.pow(math.e, 0 - h))
    return round(h, 4), round(outH, 4)

def calculateOutput():
    o = 0
    for i, val in enumerate(hiddenLayers):
        o = o + val[1] * weightsSecondLayer[i]
    
    outO = 1 / (1 + math.pow(math.e, 0 - o))
    return round(o, 4), round(outO, 4)

def calculateError(output):
    return round(math.pow(otherData[0] - output, 2) / 2, 4)

def printWeights():
    print("\nWeights from Input layer to Hidden layer: ")
    for i, row in enumerate(weightsFirstLayer):
        for j, element in enumerate(row):
            print(f"w{i+1}{j+1}: {element}.")

    print("\nWeights from Hidden layer to Output layer: ")
    for i, element in enumerate(weightsSecondLayer):
        print(f"w{i+1}1: {element}.")

def printObservations():
    print("Given Inputs: ")
    for i, element in enumerate(inputs):
        print(f"x{i+1}: {element}.")
    print(f"Target: {otherData[0]}.")
    print(f"Learning Rate: {otherData[1]}.")
    print(f"Iterations: {otherData[2]}.")

    printWeights()

    print(f"\nNumber of nodes in Input layer: {len(weightsFirstLayer)}.")
    print(f"Number of nodes Hidden layer: {len(weightsFirstLayer[0])}.")
    
print("Getting required inputs from the user: ")
printObservations()

iterations = otherData[2]
for epoch in range(int(iterations)):
    hiddenLayers = []
    for i in range(int(len(weightsFirstLayer))):
        hiddenLayers.append(calculateHiddenLayer(i))
    
    outputLayer = calculateOutput()
    error = calculateError(outputLayer[1])
    dHidden = []
    dOutput = round(outputLayer[1] * (1 - outputLayer[1]) * (otherData[0] - outputLayer[1]), 4)

    for i in range(len(hiddenLayers)):
        dHidden.append(round(hiddenLayers[i][1] * (1 - hiddenLayers[i][1]) * (weightsSecondLayer[i] * dOutput), 4))

    for i, row in enumerate(weightsFirstLayer):
        for j, element in enumerate(row):
            weightsFirstLayer[i][j] = round(otherData[1] * dHidden[i] * inputs[j] + weightsFirstLayer[i][j], 4)

    for i, element in enumerate(weightsSecondLayer):
        weightsSecondLayer[i] = round(otherData[1] * dOutput * hiddenLayers[i][1] + element, 4)

    if not (epoch + 1) % 10:
        print(f"\nPrinting Epoch {epoch+1}:", end="")
        printWeights()

        print("\nInputs and outputs to Hidden layers: ")
        for i, row in enumerate(hiddenLayers):
            print(f"h_in{i+1}: {row[0]}.")
            print(f"h_out{i+1}: {row[1]}.")

        print(f"\no_in: {outputLayer[0]}.")
        print(f"o_out: {outputLayer[1]}.")
        print(f"Error Observed: {error}.")

        print(f"\nd_Out: {dOutput}.")

        for i in range(len(hiddenLayers)):
            print(f"d_h{i+1}: {dHidden[i]}.")

print("\nParameters after final update:")
printWeights()
print(f"\nOutput: {outputLayer[1]}.")
print(f"Error Observed: {error}.")