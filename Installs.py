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
def pipLatestVersion():
    try:
        from pip._internal.operations import freeze
        installed_packages = freeze.freeze()
        for package in installed_packages:
            if package.startswith('pip=='):
                return package.split('==')[1]
    except Exception as e:
        print("Error:", e)
    return None
# Check if pip is up-to-date
def pipUpToDate():
    installedVersion = pipLatestVersion()
    if installedVersion:
        latestVersion = pip.__version__
        print(f"Installed version: {installedVersion}, Latest version: {latestVersion}")
        return installedVersion == latestVersion
    return False
def upgradePip():
    print("Upgrading pip...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

# Check if nltk.data packages are already installed and if not install them
def nltkData():
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

    # if not nltk.corpus.stopwords.words('english'):
    #     print("Installing nltk stopwords...")
    #     print(f"This may take a few minutes...")
    #     nltk.download('stopwords')
    # else:
    #     print(f"NLTK stopwords are already installed.")
    # if not nltk.tokenize.word_tokenize("test"):
    #     print("Installing nltk punkt...")
    #     print(f"This may take a few minutes...")
    #     nltk.download('punkt')
    # else:
    #     print(f"nltk punkt is already installed.")
    # print("nltk data check completed.")

if __name__ == "__main__":
    # Update pip if necessary
    if not pipUpToDate():
        upgradePip()
    else:
        print (f"pip is up-to-date")
    # All the packages are already installed.
    packagesToInstall = [
        "torch",
        "tensorflow",
        "flask",
        "flask-cors",
        "ipykernel",
        "nltk"
    ]
    installPackages(packagesToInstall)
    nltkData()
    print("***All packages installed***")
