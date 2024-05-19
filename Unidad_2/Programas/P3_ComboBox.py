import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
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

        self.combo_personas.addItem("Selecciona...", 0)
        self.combo_personas.addItem("Alan", 1)
        self.combo_personas.addItem("Diego", 2)
        self.combo_personas.addItem("Joseph", 3)
        self.combo_personas.addItem("Emmanuel", 4)
        self.combo_personas.addItem("Isaac", 5)

        self.combo_personas.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        print("Text: " + self.combo_personas.currentText())
        print("Index: " + str(self.combo_personas.currentIndex()))
        print("Data: " + str(self.combo_personas.currentData()))

        dataClave = self.combo_personas.currentData()
        imagen = self.datos_integrantes[dataClave][-1]
        self.Img_persona.setPixmap(QtGui.QPixmap(imagen))


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

