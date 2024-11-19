from cryptography.fernet import Fernet

class Criptografia:
    cipher = None #Esta variable tendrá el encriptador/desemcro´tadpr
    def __init__(self):
        self.cipher = Fernet(b"Y1p3Ym5uTE91Rk5zTk1vZWlwN3NYN3FjeVlZbXNTM3k=") #Se crea un objeto Fernet, con una clave ya determinada. Esta clave se generó aleatoriamente y se trabajará todos los archivos con la misma.

    def encriptar(self, string): 
        stringEncriptado = self.cipher.encrypt(string) #Se encripta la cadena, la variable stringEncriptado es un string en bytes.
        return stringEncriptado #Se devuelve la encriptación correspondiente.

    def desencriptar(self, stringEncriptado):
        return self.cipher.decrypt(stringEncriptado).decode("utf-8") #Se desencripta el string encriptado y se en formato UTF-8.
