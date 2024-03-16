# Multilayer Perceptron (MLP)

## Introduction

The Multilayer Perceptron (MLP) is a type of feedforward artificial neural network (ANN) composed of multiple layers of nodes, each layer fully connected to the next one. It is a versatile and powerful architecture widely used in machine learning for classification, regression, and other tasks.

## Architecture

An MLP consists of three types of layers:

1. **Input Layer:** This layer contains input nodes that represent the features of the input data. Each node corresponds to a feature, and the number of nodes in this layer is equal to the number of input features.

2. **Hidden Layers:** These are one or more layers between the input and output layers. Each hidden layer consists of multiple nodes (neurons), and each node is connected to every node in the previous layer (fully connected). The hidden layers perform complex transformations on the input data, extracting hierarchical features.

3. **Output Layer:** The output layer produces the final output of the network. The number of nodes in this layer depends on the problem type. For binary classification, there is one node with a sigmoid activation function. For multi-class classification, there are multiple nodes, one for each class, typically with a softmax activation function. For regression tasks, there is usually a single node with a linear activation function.

## Activation Function

Each node in the MLP, except those in the input layer, applies an activation function to the weighted sum of its inputs. Common activation functions include:

- **Sigmoid:**
  
    $f(x) = \frac{1}{1 + e^{-x}}$
- **ReLU (Rectified Linear Unit):**
  
    $f(x) = \max(0, x)$
- **Tanh:**
  
    $f(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$
- **Softmax:**
  
    $f(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{n} e^{x_j}}$ (for output layer in multi-class classification)

## Training

Training an MLP involves adjusting the weights and biases of the connections between neurons to minimize a loss function. This is typically done using an optimization algorithm like gradient descent. Backpropagation, a method for efficiently computing gradients, is used to update the weights in the network by propagating the error backward from the output layer to the input layer.

## Advantages

- MLPs are capable of learning complex non-linear relationships in data.
- They can approximate any continuous function given enough hidden units.
- They are versatile and can be applied to a wide range of tasks, including classification, regression, and even reinforcement learning.

## Limitations

- Training an MLP can be computationally expensive, especially for large networks and datasets.
- MLPs are prone to overfitting, especially with insufficient training data or poorly chosen hyperparameters.
- They may require careful tuning of hyperparameters, such as the number of layers, number of nodes per layer, and learning rate.

## Conclusion

Multilayer Perceptrons are powerful and versatile neural network architectures that have been widely used in machine learning for various tasks. With appropriate architecture design, hyperparameter tuning, and training strategies, MLPs can achieve state-of-the-art performance on many challenging problems.

## Usage

It consists of a file called `DataForMLP.csv` which contains input for the program `MultiLayerPerceptron.csv`.

## Specifications about `DataForMLP.csv`

1. First Line: Input points
2. Second Line: Weights for path from input layer to hidden layer (Must be = hidden layer nodes * input nodes).
     1. Example: With 3 input nodes and 2 hidden layer nodes, this line must have 6 weights with first three for first node and other three for other node.
3. Third line: Weights for path from hidden layer to output layer (Must be = no of hidden layer nodes).
4. Fourth line: Contains other utility data
     1. First object: Target Output.
     2. Second object: Learning Rate.
     3. Third object: No of Epochs to run.
