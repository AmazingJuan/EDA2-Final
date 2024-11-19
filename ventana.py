import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from cryptography.fernet import InvalidToken
from criptografia import Criptografia
from pathlib import Path
from ui_form import Ui_ventana

FILTRO_ARCHIVOS = "Archivos de texto editables (*.eda2)" #Este es el filtro que se va a aplicar a la hora de abrir o crear nuevos archivos.

class ventana(QMainWindow):
    obj = Criptografia() #Se inicializa un objeto de criptografia, que es capaz de encriptar y desencriptar strings.
    archivo = None #Aca se guardarán los distintos archivos que se abran o creen en la implementación.
    contenidoGuardado = "" #La ultima cadena que se ha guardado.

    def salir(self):
        #Este if verifica que el contenido que hay en el editor de texto corresponda con lo que está guardado, esto para avisarle al usuario que va a perder sus datos si procede con la accion.
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            if not self.archivo is None: #Si un archivo se inicializó, entonces se cierra.
                self.archivo.close()
                self.archivo = None
            self.close() #Aca se cierra la ventana.
        else: #Acá el usuario no ha guardado los cambios, entonces se le muestra un aviso.
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048: #Esto significa que el usuario decidió guardar cambios.
                self.guardar() #Entonces guarda los cambios.
                self.salir() #Y sale finalmente del programa.
            else:
                self.ui.textEdit.setEnabled(False) #En caso contrario, desabilita la entrada de texto y sale de programa.
                self.salir()

    def escribirArchivo(self, string): #Esta funcion permite escribir en el archivo actual.
        self.archivo.seek(0) #Va al principio del archivo
        self.archivo.truncate() #Deja en blanco el archivo.
        if len(string) > 0: #Si se va a ingresar un string no vacío entonces se encripta.
            self.archivo.write(self.obj.encriptar(string))
        else:
            self.archivo.write(b"") #Si el string es vacío, entonces solamente ingresa el espacio vacio
        self.archivo.flush() #Se actualiza el contenido del archivo.

    def abrir(self):
    #Este if verifica que el contenido que hay en el editor de texto corresponda con lo que está guardado, esto para avisarle al usuario que va a perder sus datos si procede con la accion.
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            rutaSeleccionada = QFileDialog.getOpenFileName(self, "Seleccione un archivo compatible con el editor", "", FILTRO_ARCHIVOS) #Le pide al usuario que seleccione la ruta donde va a abrir el archivo.
            if rutaSeleccionada[0] != "": #Si el usuario seleccionó una ruta valida, hace lo siguiente:
                if not self.archivo is None: #Si hubo un archivo antes del que viene, entonces cierrelo.
                    self.archivo.close()
                    self.archivo = None
                self.archivo = open(rutaSeleccionada[0], "r+b") #Abre el archivo en modo de lectura binaria ampliada (tambien puede escribir).
                texto = self.archivo.read() #Se obtiene el texto que está contenido en el archivo.
                if len(texto) != 0: #Si el archivo contiene texto entonces intente desencriptarlo.
                    try: #Intenta desencriptar el archivo.
                        aux = self.obj.desencriptar(texto) #Obtiene el texto desencriptado.
                        self.ui.textEdit.setPlainText(aux) #Se pone en el editor de texto el texto del archivo.
                        self.contenidoGuardado = aux #El contenido guardado es el que se acabó de leer.
                    except InvalidToken: #Si esta excepcion aparece, entonces el archivo está corrupto (fue encriptado con otra clave, o la estructura no es válida).
                        self.mostrar_mensaje("corrupto")
                else: #Si no hay texto simplemente muestre el editor de texto vacío.
                    self.contenidoGuardado = ""
                    self.ui.textEdit.setPlainText("")
                self.ui.textEdit.setEnabled(True) #Acá se habilita el editor de texto
                nombre_archivo = Path(rutaSeleccionada[0]).name #Se obtiene el nombre del archivo.
                self.setWindowTitle(f"Editor de texto - {nombre_archivo}") #Se cambia el nombre de la ventana, para que se muestre el nombre del archivo.
        else: #Acá el usuario no ha guardado los cambios, entonces se le muestra un aviso.
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048: #Esto significa que el usuario decidió guardar cambios.
                self.guardar() #Entonces guarda los cambios.
                self.abrir() #Hace saltar el dialogo para abrir un archivo.
            else:
                self.ui.textEdit.setEnabled(False) #En caso contrario, desabilita la entrada de texto y hace saltar el dialogo para abrir un archivo.
                self.abrir()

    def nuevo(self):
        #Este if verifica que el contenido que hay en el editor de texto corresponda con lo que está guardado, esto para avisarle al usuario que va a perder sus datos si procede con la accion.
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            rutaSeleccionada = QFileDialog.getSaveFileName(self, "Seleccione un archivo compatible con el editor", "", FILTRO_ARCHIVOS) #Le pide al usuario que seleccione la ruta donde va a crear el archivo.
            if(rutaSeleccionada[0] != ""): #Si el usuario seleccionó una ruta valida, hace lo siguiente:
                if not self.archivo is None: #Si hubo un archivo antes del que viene, entonces cierrelo.
                    self.archivo.close()
                self.ui.textEdit.setPlainText("") #Ponga el editor en blanco por si hubo antes un archivo abierto.
                self.archivo = open(rutaSeleccionada[0], "w+b") #Abra el archivo en modo escritura binaria ampliada (tambien permite leer).
                self.ui.textEdit.setEnabled(True) #Permitale al usuario escribir en el editor de texto.
                self.contenidoGuardado = "" #Como el archivo es nuevo, lo que está guardado en el es la cadena vacia.
                nombre_archivo = Path(rutaSeleccionada[0]).name #Se obtiene el nombre del archivo.
                self.setWindowTitle(f"Editor de texto - {nombre_archivo}") #En la ventana se pone el nombre del archivo.
        else: #Acá el usuario no ha guardado los cambios, entonces se le muestra un aviso.
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048: #Esto significa que el usuario decidió guardar cambios.
                self.guardar() #Entonces guarda los cambios.
                self.nuevo() #Hace saltar el dialogo para crear un archivo.
            else:
                self.ui.textEdit.setEnabled(False) #En caso contrario, desabilita la entrada de texto y hace saltar el dialogo para crear un archivo.
                self.nuevo()

    def guardar(self): #Esta funcion sirve para guardar en el archivo actual lo que el usuario tenga en el editor de texto.
        if self.ui.textEdit.isEnabled(): #Verifica si el usuario puede escribir en el editor de texto (esto quiere decir que tiene un archivo abierto).
            texto = self.ui.textEdit.toPlainText() #Se obtiene todo el texto en el editor.
            if(texto != self.contenidoGuardado): #Si el texto es igual al que está guardado no hay necesidad de guardarlo.
                self.escribirArchivo(texto.encode()) #Escribe los caracteres del texto en formato UTF-8
                self.contenidoGuardado = texto #El contenido guardado se actualiza

    def cerrar(self):
        #Este if verifica que el contenido que hay en el editor de texto corresponda con lo que está guardado, esto para avisarle al usuario que va a perder sus datos si procede con la accion.
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            self.ui.textEdit.setPlainText("") #Limpie el editor de texto.
            self.ui.textEdit.setEnabled(False) #Deshabilite la escritura en el editor.
            self.setWindowTitle(f"Editor de texto") #Y cambiele el nombre a la ventana, dado que no va a haber ningun archivo abierto.
            self.contenidoGuardado = ""
            if not self.archivo is None: #Si habia un archivo antes de cerrar, entonces cierre el archivo.
                self.archivo.close() 
                self.archivo = None
        else: #Acá el usuario no ha guardado los cambios, entonces se le muestra un aviso.
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048: #Esto significa que el usuario decidió guardar cambios.
                self.guardar() #Entonces guarda los cambios.
                self.cerrar() #Cierra el archivo actial.
            else:
                self.ui.textEdit.setEnabled(False) #En caso contrario, desabilita la entrada de texto y hace saltar el dialogo para cerrar un archivo.
                self.cerrar()


    def mostrar_mensaje(self, razon): #Esta funcion muestra las ventanas emergentes que salen cuanto hay un error o una advertencia.
        msj = QMessageBox() #Crea un objeto de caja de mensaje.
        if razon == "corrupto": #Si el archivo está corrupto hace lo siguiente:
            msj.setWindowTitle("Archivo corrupto") #Pone un titulo de archivo corrupto a la caja de mensaje.
            msj.setIcon(QMessageBox.Critical) #Esta linea asigna un icono critico a la caja.
            msj.setText("El archivo que ha proporcionado está corrupto o dañado, no podemos abrirlo...") #Coloca un texto que le dice al usuario que pasó
        elif razon == "no guardar": #Si el archivo no ha guardado cambios hace lo siguiente:
            msj.setWindowTitle("Archivo sin guardar") #Pone un titulo de cambios sin guardar a la caja de mensaje.
            msj.setIcon(QMessageBox.Warning)  #Esta linea asigna un icono de advertencia a la caja.
            msj.setStandardButtons(QMessageBox.Save | QMessageBox.No) #Coloca botones que le dan a escoger al usuario entre guardar o no.
            msj.setText("Usted no ha guardado su progreso, ¿desea guardarlo en el archivo actual?") #Se le da a saber al usuario q tiene cambios sin guardar.
        return msj.exec() #Finalmente se muestra la cajita de mensaje.



    def __init__(self, parent=None): #Este inicializador de la clase sirve para hacer todas las conexiones necesarias, ponerle nombre a la ventana, entre otras cosas.
        super().__init__(parent)
        self.ui = Ui_ventana()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.textEdit)
        self.setWindowTitle("Editor de Texto")
        self.ui.actionSalir.triggered.connect(self.salir)
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionNuevo.triggered.connect(self.nuevo)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionCerrar.triggered.connect(self.cerrar)
