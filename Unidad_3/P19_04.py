import sys
from PyQt5 import uic, QtWidgets
from PyQt6.QtWidgets import QDialog

qtCreatorFile = "AYB.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def myDialog():
    pass


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_sumar.clicked.connect(self.sumar)


        # Área de los Signals
        def sumar(self):
            a = int(self.txt_a.text())
            b = int(self.txt_b.text())
            r = a + b
            self.dialogo = myDialog()
            self.dialogo.setModal(True)
            self.dialogo.txt_resultado.setText(str(r))
            self.dialogo.show()


##############################################################################################

            qtCreatorFile = "RESULTADO.iu" #NOMBRE DEL ARCHIVO AQUI
            ui_dialog, QtBaseClass = vic.loadUiType(qtCreatorFile)

            class MyDialog(QtWidgets,QDialog,Ui_dialog):
                def _init__(self):
                    QtWidgets.QDialog.__init__(self)
                    ui_dialog.__init__(self)
                    self.setupUi(self)

    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

