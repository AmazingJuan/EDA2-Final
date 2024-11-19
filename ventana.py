import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from cryptography.fernet import InvalidToken
from criptografia import Criptografia
from pathlib import Path
from ui_form import Ui_ventana

FILTRO_ARCHIVOS = "Archivos de texto editables (*.eda2)"

class ventana(QMainWindow):
    obj = Criptografia()
    apenasAbrio = True
    autoguardar = False
    archivo = None
    contenidoGuardado = ""

    def salir(self):
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            if not self.archivo is None:
                self.archivo.close()
                self.archivo = None
            self.close()
        else:
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048:
                self.guardar()
                self.salir()
            else:
                self.ui.textEdit.setEnabled(False)
                self.salir()

    def escribirArchivo(self, string):
        self.archivo.seek(0)
        self.archivo.truncate()
        if len(string) > 0:
            self.archivo.write(self.obj.encriptar(string))
        else:
            self.archivo.write(b"")
        self.archivo.flush()

    def abrir(self):
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            rutaSeleccionada = QFileDialog.getOpenFileName(self, "Seleccione un archivo compatible con el editor", "", FILTRO_ARCHIVOS)
            if rutaSeleccionada[0] != "":
                if not self.archivo is None:
                    self.archivo.close()
                    self.archivo = None
                self.archivo = open(rutaSeleccionada[0], "r+b")
                texto = self.archivo.read()
                if len(texto) != 0:
                    try:
                        aux = self.obj.desencriptar(texto)
                        self.ui.textEdit.setPlainText(aux)
                        self.contenidoGuardado = aux
                    except InvalidToken:
                        self.mostrar_mensaje("corrupto")
                else:
                    self.contenidoGuardado = ""
                    self.ui.textEdit.setPlainText("")
                self.ui.textEdit.setEnabled(True)
                nombre_archivo = Path(rutaSeleccionada[0]).name
                self.setWindowTitle(f"Editor de texto - {nombre_archivo}")
        else:
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048:
                self.guardar()
                self.abrir()
            else:
                self.ui.textEdit.setEnabled(False)
                self.abrir()

    def nuevo(self):
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            rutaSeleccionada = QFileDialog.getSaveFileName(self, "Seleccione un archivo compatible con el editor", "", FILTRO_ARCHIVOS)
            if(rutaSeleccionada[0] != ""):
                if not self.archivo is None:
                    self.archivo.close()
                self.ui.textEdit.setPlainText("")
                self.archivo = open(rutaSeleccionada[0], "w+b")
                self.ui.textEdit.setEnabled(True)
                self.contenidoGuardado = ""
                nombre_archivo = Path(rutaSeleccionada[0]).name
                self.setWindowTitle(f"Editor de texto - {nombre_archivo}")
        else:
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048:
                self.guardar()
                self.nuevo()
            else:
                self.ui.textEdit.setEnabled(False)
                self.nuevo()

    def guardar(self):
        if self.ui.textEdit.isEnabled():
            texto = self.ui.textEdit.toPlainText()
            if(texto != self.contenidoGuardado):
                self.escribirArchivo(texto.encode())
                self.contenidoGuardado = texto

    def cerrar(self):
        if self.contenidoGuardado == self.ui.textEdit.toPlainText() or not self.ui.textEdit.isEnabled():
            if self.ui.textEdit.isEnabled():
                self.ui.textEdit.setPlainText("")
                self.ui.textEdit.setEnabled(False)
                self.setWindowTitle(f"Editor de texto")
                if not self.archivo is None:
                    self.archivo.close()
                    self.archivo = None
        else:
            decision = self.mostrar_mensaje("no guardar")
            if decision == 2048:
                self.guardar()
                self.cerrar()
            else:
                self.ui.textEdit.setEnabled(False)
                self.cerrar()


    def mostrar_mensaje(self, razon):
        msj = QMessageBox()
        if razon == "corrupto":
            msj.setWindowTitle("Archivo corrupto")
            msj.setIcon(QMessageBox.Critical)
            msj.setText("El archivo que ha proporcionado está corrupto o dañado, no podemos abrirlo...")
        elif razon == "no guardar":
            msj.setWindowTitle("Archivo sin guardar")
            msj.setIcon(QMessageBox.Warning)
            msj.setStandardButtons(QMessageBox.Save | QMessageBox.No)
            msj.setText("Usted no ha guardado su progreso, ¿desea guardarlo en el archivo actual?")
        return msj.exec()



    def __init__(self, parent=None):
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
