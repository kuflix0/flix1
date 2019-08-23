import os
from unittest import TestCase
from Vigenere import verschlüsseln, entschlüsseln, buchstabeZUZahl

class TestOtp(TestCase):
    def test_verschlüsseln(self):
        kText = "hallz"
        schluessel = "hamlet"
        gText = "oaxwd"

        self.assertEqual(gText, verschlüsseln(kText, schluessel))


    def test_entschlüsseln(self):
        gText = "oaxws"
        schluessel = "hamlet"
        kText = "hallo"

        self.assertEqual(kText, entschlüsseln(gText, schluessel))

    def test_exception_entschlüssln_kText_uz(self):
        with self.assertRaises(Exception) as context:
           entschlüsseln("-", "wasd")

        self.assertTrue('ungültiges Zeichen' in str (context.exception))

    def test_exception_entschlüssln_schluessel_uz(self):
        with self.assertRaises(Exception) as context:
            entschlüsseln("was", "+w+#")

        self.assertTrue('ungültiges Zeichen' in str(context.exception))

    def test_exception_verschlüssln_kText_uz(self):
        with self.assertRaises(Exception) as context:
            verschlüsseln("-", "wasd")

        self.assertTrue('ungültiges Zeichen' in str(context.exception))

    def test_exception_verschlüssln_schluessel_uz(self):
        with self.assertRaises(Exception) as context:
            verschlüsseln("was", "+w+#")

        self.assertTrue('ungültiges Zeichen' in str(context.exception))
