import subprocess
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import json
from textProcessing import wordBag, tokenize, stemming
from model import Network

# Run the installation script to get all packages
subprocess.run(['python', 'installs.py'])

# Open intents file validation
try:
    with open('intents.json', 'r') as f:
        intents = json.load(f)
except FileNotFoundError:
    print("Error: 'intents.json' could not be found. Please place the file in the project directory.")
    raise SystemExit(1)

# Process intents data
allWords = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        sentenceWords = tokenize(pattern)
        allWords.extend(sentenceWords)
        xy.append((sentenceWords, tag))

allWords = [stemming(word) for word in allWords if word not in ['?', '.', '!', '+', '-']]
allWords = sorted(set(allWords))
tags = sorted(set(tags))

# Convert data into training format
x_train = []
y_train = []

for (sentenceWords, tag) in xy:
    bag = wordBag(sentenceWords, allWords)
    x_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

# Define Dataset class
class ChatbotDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = torch.tensor(x_train, dtype=torch.float32)
        self.y_data = torch.tensor(y_train, dtype=torch.long)

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
trainLoader = DataLoader(dataset=dataset, batch_size=batchSize, shuffle=True)

# Check for GPU support
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize model
model = Network(inputSize, hiddenSize, outputSize).to(device)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

# Print status message
print("Training program is running")

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

    # Print losses every 100 epochs
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

try:
    FILE = "data.pth"
    torch.save(data, FILE)
    print(f"Training complete, model saved to '{FILE}'")
except IOError:
    print("Error: An I/O error occurred while saving the model.")
except Exception as e:
    print(f"Error: {e}")
