import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QColor

qtCreatorFile = "IntensidadFoco.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.valorR.setMinimum(0)
        self.valorR.setMaximum(255)
        self.valorR.setSingleStep(1)
        self.valorR.setValue(255)
        self.valorR.valueChanged.connect(self.actualiza_color)

    def actualiza_color(self):
        value = self.valorR.value()
        color = QColor(value, value, value)
        style_sheet = f"background-color: {color.name()};"
        self.colorburguer.setStyleSheet(style_sheet)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
