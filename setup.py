import os
import sys
import subprocess

def install_packages():
    print("The install is started")
    packages = ["requests", "dnspython", "python-whois"]
    for package in packages:
        subprocess.call([sys.executable, "-m", "pip", "install", package, "--quiet"])
    print("The install is ended!")

def run_multitool():
    filename = "main.py"
    if not os.path.exists(filename):
        print(f"[-] Nem található a fájl: {filename}")
        return
    subprocess.call([sys.executable, filename])

if __name__ == "__main__":
    install_packages()
    run_multitool()
