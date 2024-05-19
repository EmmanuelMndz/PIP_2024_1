import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P5_VerticalSlider.ui"  # Nombre del archivo aquí.
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

        self.vs_personas.setMinimum(1)
        self.vs_personas.setMaximum(5)
        self.vs_personas.setSingleStep(1)
        self.vs_personas.setValue(1)
        self.vs_personas.valueChanged.connect(self.cambia)

    def cambia(self):
        dataClave = self.vs_personas.value()
        print(dataClave)
        imagen = self.datos_integrantes[dataClave][-1]
        self.Img_persona.setPixmap(QtGui.QPixmap(imagen))


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

