import subprocess
#Run the installation script to get all packages
subprocess.run(['python', 'installs.py'])

#Look to see if text proccessing files and mof
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

import random
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import json
import torch.cuda

# Function to load textProcessing module with error handling

loadModelmModule()
textProcessingModule()


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

try:
    with open('intents.json', 'r') as f:
        intents = json.load(f)
except FileNotFoundError:
    print("Error: 'intents.json' could not be found. Please place the file in the project directory.")
    raise SystemExit(1)

fallbackResponses = [
    "I'm sorry, I couldn't find an answer to your query. Can I assist you with anything else?",
    "Apologies, I'm not able to provide a response to that question. Is there something else you'd like to know?",
    "It seems I'm unable to assist with that request. Would you like help with another topic?",
    "I'm afraid I don't have the information you're looking for at the moment. Can I help you with anything else?",
    "I'm currently unable to process that request. Please feel free to ask me anything else.",
    "I'm still learning and may not have the answer to your question. Is there another way I can assist you?",
    "I apologize, but I'm not equipped to handle that request. Is there a different topic you'd like to discuss?",
    "Unfortunately, I'm unable to understand your request. Could you please provide more details or ask a different question?",
    "I'm sorry, I don't have the necessary information to address that. Can I help you with something else?",
    "I'm unable to provide an answer to your question. Is there anything else I can assist you with?",
]


wordBagFunction, tokenizeFunction, stemmingFunction = textProcessingModule()
Network = loadModelmModule()
file = "data.pth"
data = torch.load(file)
inputSize = data["input_size"]
hiddenSize = data["hidden_size"]  # Correct the case of the key
outputSize = data["output_size"]
allWords = data["all_words"]
tags = data["tags"]
modelState = data["model_state"]
module = Network(inputSize, hiddenSize, outputSize).to(device)
module.load_state_dict(modelState)
module.eval()

name = "Elevate"
print(f"*********{name} Chatbot has successfully deployed*********")


def getResponse(msg):
    sentence = tokenizeFunction(msg)
    x = wordBagFunction(sentence, allWords)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = module(x)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    print(tag)

    prob = torch.softmax(output, dim=1)
    prob = prob[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
                print(f"{tag} & {intent}")
    else:
        return random.choice(fallbackResponses)

if __name__ == "__main__":
    print(f"Ready to chat!")
    while True:
        sentence = input("You: ")
        if sentence.lower() == "quit":
            print("Exiting...")
            break
        bot_response = getResponse(sentence)
        print("Bot:", bot_response)



