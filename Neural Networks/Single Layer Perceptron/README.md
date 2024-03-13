# Single-Layer Perceptron (SLP)

A single-layer perceptron (SLP) is the simplest form of artificial neural networks, a fundamental building block in the field of machine learning. It consists of a single layer of interconnected nodes, also known as perceptrons, without any hidden layers.

## Architecture

The SLP architecture is characterized by the following components:

### Input Layer

- **Nodes (Neurons):** The input layer consists of nodes, each representing a feature or input variable. These nodes pass the input values to the next layer.

### Output Layer

- **Nodes (Perceptrons):** The output layer generates the final output based on the weighted sum of inputs and an activation function.

## Operation

1. **Input:** Input values are fed into the input layer nodes.
  
2. **Weighted Sum:** Each input is multiplied by its corresponding weight, and the results are summed up.

   \[ \text{Weighted Sum} = \sum_{i=1}^{n} ( \text{Input}_i \times \text{Weight}_i ) + \text{Bias} \]

3. **Activation Function:** The weighted sum is then passed through an activation function. Common activation functions include the step function, sigmoid, or hyperbolic tangent (tanh).

   \[ \text{Output} = \text{Activation}(\text{Weighted Sum}) \]

4. **Output:** The output is produced by the perceptron, representing the result of the computation.

## Training

- **Learning Algorithm:** The perceptron is trained using a learning algorithm, such as the perceptron learning algorithm. The weights and bias are adjusted during training to minimize the error between the predicted output and the actual target.

## Limitations

- **Linear Separability:** SLPs can only learn and represent linearly separable functions. They are limited in solving problems that require non-linear decision boundaries.

- **Binary Classification:** SLPs are mainly used for binary classification tasks where the output is either 0 or 1.

Despite its limitations, the single-layer perceptron serves as a foundation for more complex neural network architectures and paved the way for the development of multilayer perceptrons (MLPs) and deep learning models.

## Execution

The program for execution is `SingleLayerPerceptron.py`. Execute the code according to the requirements of the program (List of Gates csv available: AND, OR, NOR, XOR).
