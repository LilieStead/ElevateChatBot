import torch
import torch.nn as nn


# The naturel network model below
class network(nn.Module):
    def __init__(self, inputSize, hiddenSize, numberClasses):
        super(network, self).__init__()  # Call the parent class constructor
        # Define all three layers of the network
        self.l1 = nn.Linear(inputSize, hiddenSize)
        self.real = nn.ReLU()

        self.l2 = nn.Linear(hiddenSize, hiddenSize)
        self.l3 = nn.Linear(hiddenSize, numberClasses)

    # Forward pass of the network (send data through layers)
    def forward(self, x):
        out =self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        return out