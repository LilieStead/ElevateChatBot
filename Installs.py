import subprocess
import sys
import re

# Validation to ensure each package is installed to Python interpreter
def pipLookUp(package):
    try:
        subprocess.check_output([sys.executable, '-m', 'pip', 'show', package])
        return True
    except subprocess.CalledProcessError:
        return False

def installPackages(packageList):
    for package in packageList:
        if not pipLookUp(package):
            print(f"Installing {package}")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        else:
            print(f"{package} is already installed.")

def pipLatestVersion():
    try:
        pipInfo = subprocess.check_output([sys.executable, '-m', 'pip', 'search', 'pip']).decode('utf-8')
        latestVersion = re.search(r'\(([^)]+)\)', pipInfo).group(1)
        return latestVersion
    except subprocess.CalledProcessError:
        return None

def pipUpToDate():
    installedVersion = pipLatestVersion()
    latestVersion = subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'pip']).decode('utf-8')
    latestVersion = re.search(r'Version: (.+)', latestVersion).group(1)
    if installedVersion and latestVersion:
        return installedVersion == latestVersion
    return False

def upgradePip():
    print("Upgrading pip...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

if __name__ == "__main__":
    if not pipUpToDate():
        upgradePip()

    packagesToInstall = [
        "torch",
        "tensorflow",
        "flask",
        "flask-cors",
        "ipykernel"
    ]

    installPackages(packagesToInstall)
