import subprocess
import sys
import pip

# Validation to ensure each package is installed to Python interpreter
def pipLookUp(package):
    try:
        subprocess.check_output([sys.executable, '-m', 'pip', 'show', package])
        return True
    except subprocess.CalledProcessError:
        return False

# Used to install all the packages
def installPackages(packageList):
    for package in packageList:
        if not pipLookUp(package):
            print(f"Installing {package}")
            print(f"This may take a few minutes...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        else:
            # Package is already installed
            print(f"{package} is already installed.")

# Gets the latest version of pip

def upgradePip():
    print("Upgrading pip...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

# Check if nltk.data packages are already installed and if not install them
def nltkData():
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

if __name__ == "__main__":
    # Update pip if necessary
    upgradePip()
    # All the packages are already installed.
    packagesToInstall = [
        "torch",
        "tensorflow",
        "flask",
        "flask-cors",
        "ipykernel",
        "nltk",
        "autocorrect",
        "tk"
    ]
    installPackages(packagesToInstall)
    nltkData()
    print("***All packages installed***")
