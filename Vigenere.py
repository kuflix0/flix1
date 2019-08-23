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
    gText = ""
    for i in range(0, len(kText)):
        gText += encodeChar(kText[i], schluessel[i % len(schluessel)])

    return gText


def entschlüsseln(gText, schluessel):
    kText = ""
    for i in range(0, len(gText)):
        kText += decodeChar(gText[i], schluessel[i % len(schluessel)])
    return kText
