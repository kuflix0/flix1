kText = ""
gText = ""


def buchstabeZUZahl(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    zahl = 0
    for buchtstabe in alphabet:
        if buchtstabe == (char):
            return zahl
        zahl += 1
    raise Exception("ungültiges Zeichen")


def zahlZUBuchstabe(zahl):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    try:
        return alphabet[zahl]
    except IndexError:
        raise Exception("ungültiges Zeichen")


def encodeChar(kText, schluessel):
    gZahl = (buchstabeZUZahl(kText) + buchstabeZUZahl(schluessel)) % 26
    gText = zahlZUBuchstabe(gZahl)
    return gText


def decodeChar(gText, schluessel):
    kZahl = (buchstabeZUZahl(gText) - buchstabeZUZahl(schluessel) +26) % 26
    kText = zahlZUBuchstabe(kZahl)
    return kText


def verschlüsseln(kText, schluessel):
    if len(schluessel) < len(kText):
        raise Exception("schlüssel zu kurz")
    gText = ""
    for i in range(0, len(kText)):
        gText += encodeChar(kText[i], schluessel[i])

    return gText


def entschlüsseln(gText, schluessel):
    if len(schluessel) < len(gText):
        raise Exception("schlüssel zu kurz")

    kText = ""
    for i in range(0, len(gText)):
        kText += decodeChar(gText[i], schluessel[i])
    return kText


def main():
    cont = True
    choice = ""
    print("One-Time-Pad Programm.")
    print("\nAuswahl:\n1: Verschlüsselung\n2: Entschlüsselung\n3: Verlassen")
    while cont == True:
        choice = input(">>> ")
        if choice == "1":
            kText = input("Bitte geben sie ihren kText ein: ")
            schluessel =input("Bitte geben sie ihren schluessel: ")
            print("Ihr Geheimtext ist " + verschlüsseln(kText.lower(),schluessel.lower()))

        elif choice == "2":
            gText = input("Bitte geben sie ihren geheimtext ein: ")
            schluessel = input("Bitte geben sie ihren schluessel an: ")
            print("Ihr kText lautet " + entschlüsseln(gText.lower(),schluessel.lower()))


        elif choice == "3":
            cont = False

        else:
            print("Wählen sie zwischen 1, 2, oder 3")


main()
