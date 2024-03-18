import subprocess
#Run the installation script to get all packages
subprocess.run(['python', 'installs.py'])

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import json


# Function to load textProcessing module with error handling
def textProcessingModule():
    try:
        from textProcessing import wordBag, tokenize, stemming
        return wordBag, tokenize, stemming
    except ImportError:
        print("Error: 'textProcessing.py' could not be found. Please place the file in the project directory.")
    raise SystemExit(1)

# Function to load model module with error handling
def loadModelmModule():
    try:
        from model import Network
        return Network
    except ImportError:
        print("Error: 'model.py' could not be found. Please place the file in the project directory.")
        raise SystemExit(1)

# Open intents file validation
try:
    with open('Intents.json', 'r') as f:
        intents = json.load(f)
except FileNotFoundError:
    print("Error: 'intents.json' could not be found. Please place the file in the project directory.")
    print("    -Training program has stopped running due to error")
    raise SystemExit(1)

# Load text processing module
wordBag, tokenize, stemming = textProcessingModule()

# Load model module
network = loadModelmModule()

# Print status message
print("Training program is running")

# Define ignored characters
ignoredLetters = ['?', '.', '!', '+', '-']

# Process intents data
allWords = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        sentenceWord = tokenize(pattern)
        allWords.extend(sentenceWord)
        xy.append((sentenceWord, tag))

allWords = [stemming(sentenceWord) for sentenceWord in allWords if sentenceWord not in ignoredLetters]
allWords = sorted(set(allWords))
tags = sorted(set(tags))

# Convert data into training format
x_train = []
y_train = []

for (sentencePattern, tag) in xy:
    bag = wordBag(sentencePattern, allWords)
    x_train.append(bag)
    label = tag.index(tag)
    y_train.append(label)

x_train = torch.tensor(x_train)
y_train = torch.LongTensor(y_train)

# Define Dataset class
class ChatbotDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

# Define model parameters
hiddenSize = 8
outputSize = len(tags)
inputSize = len(x_train[0])
batchSize = 8
learningRate = 0.001
numberEpochs = 1000

# Create DataLoader
dataset = ChatbotDataset()
trainLoader = DataLoader(dataset=dataset, batch_size=batchSize, shuffle=True, num_workers=0)

# Check for GPU support
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Initialize model
model = network(inputSize, hiddenSize, outputSize).to(device)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

# Training loop
for epoch in range(numberEpochs):
    for words, labels in trainLoader:
        words = words.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # print losses at each 100 epochs
        if (epoch + 1) % 100 == 0:
            print(f"Epoch [{epoch + 1}/{numberEpochs}], Loss: {loss.item():.4f}")

print(f'Final loss: {loss.item():.4f}')

# Save model data
data = {
    "model_state": model.state_dict(),
    "input_size": inputSize,
    "output_size": outputSize,
    "hidden_size": hiddenSize,
    "all_words": allWords,
    "tags": tags,
}
# data file validation
try:
    # try save data
    FILE = "data.pth"
    torch.save(data, FILE)
    print(f"Training complete, model saved to '{FILE}'")
except IOError:
    print("Error: An I/O error occurred while saving the model.")
except Exception as e:
    print(f"Error: {e}")
