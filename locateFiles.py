


def textProcessingModule():
    print("Please")
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