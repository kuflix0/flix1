import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from Vigenere import verschlüsseln, entschlüsseln

print(os.environ.get('PYTHONPATH'))

def main():
    cont = True
    choice = ""
    print("One-Time-Pad Programm.")
    print("\nAuswahl:\n1: Verschlüsselung\n2: Entschlüsselung\n3: Verlassen")
    while cont == True:
        choice = input(">>> ")
        if choice == "1":
            kText = input("Bitte geben sie ihren kText ein: ")
            schluessel = input("Bitte geben sie ihren schluessel: ")
            print("Ihr Geheimtext ist " + verschlüsseln(kText.lower(), schluessel.lower()))

        elif choice == "2":
            gText = input("Bitte geben sie ihren geheimtext ein: ")
            schluessel = input("Bitte geben sie ihren schluessel an: ")
            print("Ihr kText lautet " + entschlüsseln(gText.lower(), schluessel.lower()))


        elif choice == "3":
            cont = False

        else:
            print("Wählen sie zwischen 1, 2, oder 3")


main()
