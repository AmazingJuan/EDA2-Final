# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
    QTextEdit, QToolBar, QWidget)
import rc_Recursos

class Ui_ventana(object):
    def setupUi(self, ventana):
        if not ventana.objectName():
            ventana.setObjectName(u"ventana")
        ventana.resize(800, 600)
        self.actionAbrir = QAction(ventana)
        self.actionAbrir.setObjectName(u"actionAbrir")
        icon = QIcon()
        icon.addFile(u":/imagenes/icons/open-folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbrir.setIcon(icon)
        self.actionGuardar = QAction(ventana)
        self.actionGuardar.setObjectName(u"actionGuardar")
        icon1 = QIcon()
        icon1.addFile(u":/imagenes/icons/guardar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionGuardar.setIcon(icon1)
        self.actionSalir = QAction(ventana)
        self.actionSalir.setObjectName(u"actionSalir")
        icon2 = QIcon()
        icon2.addFile(u":/imagenes/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSalir.setIcon(icon2)
        self.actionNuevo = QAction(ventana)
        self.actionNuevo.setObjectName(u"actionNuevo")
        icon3 = QIcon()
        icon3.addFile(u":/imagenes/icons/nuevo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNuevo.setIcon(icon3)
        self.actionCerrar = QAction(ventana)
        self.actionCerrar.setObjectName(u"actionCerrar")
        icon4 = QIcon()
        icon4.addFile(u":/imagenes/icons/salir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCerrar.setIcon(icon4)
        self.actionCerrar.setMenuRole(QAction.MenuRole.TextHeuristicRole)
        self.centralwidget = QWidget(ventana)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QRect(360, 210, 104, 71))
        ventana.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ventana)
        self.statusbar.setObjectName(u"statusbar")
        ventana.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(ventana)
        self.toolBar.setObjectName(u"toolBar")
        ventana.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionNuevo)
        self.toolBar.addAction(self.actionAbrir)
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addAction(self.actionCerrar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(ventana)

        QMetaObject.connectSlotsByName(ventana)
    # setupUi

    def retranslateUi(self, ventana):
        ventana.setWindowTitle(QCoreApplication.translate("ventana", u"ventana", None))
        self.actionAbrir.setText(QCoreApplication.translate("ventana", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("ventana", u"Guardar", None))
        self.actionSalir.setText(QCoreApplication.translate("ventana", u"Salir", None))
        self.actionNuevo.setText(QCoreApplication.translate("ventana", u"Nuevo", None))
        self.actionCerrar.setText(QCoreApplication.translate("ventana", u"Cerrar archivo", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("ventana", u"toolBar", None))
    # retranslateUi

