import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P1_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_integrantes = {
            1: ["Alan", "Dormir", 20, "o+", ":/Integrantes/Img_alan.jpg"],
            2: ["Diego", "Jugar", 20, "o-", ":/Integrantes/Img_diego.jpg"],
            3: ["Joseph", "Faltar", 21, "o+", ":/Integrantes/Img_joseph.jpg"],
            4: ["Emmanuel", "Saltar", 20, "o-", ":/Integrantes/emmanuel.jpeg"],
            5: ["Joseph", "Faltar", 21, "o+", ":/Integrantes/duck.jpeg"],
        }

        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.index_control = 0

        self.btn_atras.setEnabled(False)

    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_integrantes[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            ##change img
            self.Img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 1:
             self.btn_atras.setEnabled(False)


    def adelante(self):
        if self.index_control < 5:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            datos = self.datos_integrantes[self.index_control]
            print(datos)
            ##change img
            self.Img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
        if self.index_control == 5:
             self.btn_adelante.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
