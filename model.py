import torch
import torch.nn as nn

# The neural network model below
class Network(nn.Module):
    def __init__(self, inputSize, hiddenSize, numberClasses):
        super(Network, self).__init__()  # Call the parent class constructor
        # Define all three layers of the network
        self.l1 = nn.Linear(inputSize, hiddenSize)
        self.relu = nn.ReLU()  # Correct ReLU activation definition
        self.l2 = nn.Linear(hiddenSize, hiddenSize)
        self.l3 = nn.Linear(hiddenSize, numberClasses)

    # Forward pass of the network (send data through layers)
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)  # Correct way to apply ReLU activation
        out = self.l2(out)
        out = self.relu(out)  # Correct way to apply ReLU activation
        out = self.l3(out)

        return out
