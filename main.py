from ventana import * #Se importan todo lo que contiene el modulo ventana.
app = QApplication(sys.argv) 
widget = ventana() #Se inicializa un objeto de la clase ventana.
widget.show() #Se muestra el widget donde estará el editor de texto.
sys.exit(app.exec())
