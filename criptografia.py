from cryptography.fernet import Fernet



class Criptografia:
    cipher = None
    def __init__(self):
        self.cipher = Fernet(b"Y1p3Ym5uTE91Rk5zTk1vZWlwN3NYN3FjeVlZbXNTM3k=")

    def encriptar(self, string):
        stringEncriptado = self.cipher.encrypt(string)
        return stringEncriptado

    def desencriptar(self, stringEncriptado):
        hola = self.cipher.decrypt(stringEncriptado)
        return self.cipher.decrypt(stringEncriptado).decode("utf-8")
