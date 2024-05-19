import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
import random

qtCreatorFile = "MemorizarPatronesColores.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        # Área de los Signals
        self.btn_jugar.clicked.connect(self.iniciar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_1.clicked.connect(lambda: self.botonPresionado(self.btn_1))
        self.btn_2.clicked.connect(lambda: self.botonPresionado(self.btn_2))
        self.btn_3.clicked.connect(lambda: self.botonPresionado(self.btn_3))
        self.btn_4.clicked.connect(lambda: self.botonPresionado(self.btn_4))
        self.btn_5.clicked.connect(lambda: self.botonPresionado(self.btn_5))

        # Lista de colores
        self.lista_colores = [
            QtGui.QColor("red"),
            QtGui.QColor("green"),
            QtGui.QColor("blue"),
            QtGui.QColor("yellow"),
            QtGui.QColor("purple")
        ]

        self.botones = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5]
        self.patronCorrecto = []
        self.colorSeleccionado = []
        self.juegoIniciado = False

    # Área de los Slots
    def iniciar(self):
        if not self.juegoIniciado:
            self.btn_jugar.setEnabled(False)
            self.patronCorrecto = random.sample(self.lista_colores, len(self.botones))
            self.mostrarPatron()
            self.juegoIniciado = True

    def mostrarPatron(self):
        for color, boton in zip(self.patronCorrecto, self.botones):
            self.mostrarColorEnBoton(boton, color)
            QtCore.QCoreApplication.processEvents()
            QtCore.QThread.msleep(500)

        self.limpiarColoresBotones()
        self.habilitarBotones()

    def mostrarColorEnBoton(self, boton, color):
        boton.setStyleSheet(f"background-color: {color.name()}; border: 1px solid black;")

    def botonPresionado(self, boton):
        if self.juegoIniciado:
            idx = self.botones.index(boton)
            color = self.lista_colores[idx]
            if color in self.colorSeleccionado:
                self.colorSeleccionado.remove(color)
                self.limpiarColorEnBoton(boton)
            else:
                self.mostrarColorEnBoton(boton, color)
                self.colorSeleccionado.append(color)
            if len(self.colorSeleccionado) == len(self.patronCorrecto):
                self.verificarPatron()

    def limpiarColoresBotones(self):
        for boton in self.botones:
            boton.setStyleSheet("")

    def limpiarColorEnBoton(self, boton):
        boton.setStyleSheet("")

    def habilitarBotones(self):
        for boton in self.botones:
            boton.setEnabled(True)

    def deshabilitarBotones(self):
        for boton in self.botones:
            boton.setEnabled(False)

    def verificarPatron(self):
        if self.colorSeleccionado == self.patronCorrecto:
            QtWidgets.QMessageBox.information(self, "¡Ganaste!", "Lograste recordar el patron")
        else:
            QtWidgets.QMessageBox.information(self, "Perdiste", "Intentalo de nuevo")

        self.deshabilitarBotones()
        self.juegoIniciado = False

    def reiniciar(self):
        self.colorSeleccionado = []
        self.limpiarColoresBotones()
        self.habilitarBotones()
        self.btn_jugar.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
