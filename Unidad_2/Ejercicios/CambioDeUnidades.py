import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

qtCreatorFile = "CambioDeUnidades.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Conversor Métrico")

        self.btn_long.clicked.connect(self.Clongitud)
        self.btn_masa.clicked.connect(self.Cmasa)
        self.btn_temp.clicked.connect(self.Ctemperatura)

        self.tabWidget.setTabText(0, "Longitud")
        self.tabWidget.setTabText(1, "Masa")
        self.tabWidget.setTabText(2, "Temperatura")

    def Clongitud(self):
        value = float(self.lineEdit_length.text())
        self.label_cm.setText(str(value * 100))
        self.label_km.setText(str(value / 1000))

    def Cmasa(self):
        value = float(self.lineEdit_mass.text())
        self.label_kg.setText(str(value / 1000))
        self.label_mg.setText(str(value * 1000))

    def Ctemperatura(self):
        celsius = float(self.lineEdit_temperature.text())
        # Convertir Celsius a Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        # Convertir Celsius a Kelvin
        kelvin = celsius + 273.15
        self.label_fahrenheit.setText(str(fahrenheit))
        self.label_kelvin.setText(str(kelvin))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
