import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cb_alan.toggled.connect(self.sel_alan)
        self.cb_diego.toggled.connect(self.sel_diego)
        self.cb_joseph.toggled.connect(self.sel_joseph)
        self.cb_emma.toggled.connect(self.sel_emma)
        self.cb_isaac.toggled.connect(self.sel_isaac)

        self.alan = ""
        self.diego = ""
        self.joseph = ""
        self.emma = ""
        self.isaac = ""

    # Área de los Slots
    def sel_alan(self):
        if self.cb_alan.isChecked():
            print("Alan True")
            self.alan = "ALAN\n"
        else:
            print("Alan False")
            self.alan = ""
        self.txt_equipo.setPlainText(self.alan + self.diego + self.joseph + self.emma + self.isaac)

    def sel_diego(self):
        if self.cb_diego.isChecked():
            print("Diego True")
            self.diego = "DIEGO\n"
        else:
            print("Diego False")
            self.diego = ""
        self.txt_equipo.setPlainText(self.alan + self.diego + self.joseph + self.emma + self.isaac)

    def sel_joseph(self):
        if self.cb_joseph.isChecked():
            print("Joseph True")
            self.joseph = "JOSEPH\n"
        else:
            print("Joseph False")
            self.joseph = ""
        self.txt_equipo.setPlainText(self.alan + self.diego + self.joseph + self.emma + self.isaac)

    def sel_emma(self):
        if self.cb_emma.isChecked():
            print("Emma True")
            self.emma = "EMMA\n"
        else:
            print("Emma False")
            self.emma = ""
        self.txt_equipo.setPlainText(self.alan + self.diego + self.joseph + self.emma + self.isaac)

    def sel_isaac(self):
        if self.cb_isaac.isChecked():
            print("Isaac True")
            self.isaac = "ISAAC\n"
        else:
            print("Isaac False")
            self.isaac = ""
        self.txt_equipo.setPlainText(self.alan + self.diego + self.joseph + self.emma + self.isaac)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
