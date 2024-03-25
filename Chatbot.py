import subprocess
#Run the installation script to get all packages
subprocess.run(['python', 'installs.py'])

#Look to see if text proccessing files and mof
def locateFilesFunction():
    try:
        from locateFiles import textProcessingModule, loadModelmModule

        # Call the functions
        textProcessingModule()
        loadModelmModule()

    except ImportError:
        print("Error: 'locateFiles.py' could not be found. Please place the file in the project directory.")

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import json
import torch.cuda

# Function to load textProcessing module with error handling

locateFilesFunction()


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("end")
