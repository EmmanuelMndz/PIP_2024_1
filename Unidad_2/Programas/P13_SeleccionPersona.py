import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P13_SeleccionPersona.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_alan.clicked.connect(self.clic_alan)
        self.rb_alan.toggled.connect(self.toggle_alan)

    # Área de los Slots
    def clic_alan(self):
        self.lineEdit.setText("Hiciste clic a Alan")

    def toggle_alan(self):
        estado = self.rb_alan.isChecked()
        print(f"Alan cambió de estado (toggle). Nuevo Estado: {estado}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
