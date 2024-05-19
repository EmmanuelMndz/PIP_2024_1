import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer, Qt
from datetime import datetime

qtCreatorFile = "AlarmaDigital.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_establecer_alarma_2.clicked.connect(self.establecer_alarma)

        self.setFixedSize(331, 371)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)

        self.hora_alarma = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)
        self.lcdNumber.setDigitCount(8)

    def establecer_alarma(self):
        hora_alarma, ok = QtWidgets.QInputDialog.getText(self, 'Establecer Alarma', 'Ingrese la hora de la alarma:')
        if ok:
            self.hora_alarma = hora_alarma
            self.lbl_alarma.setText("Alarma establecida a las " + self.hora_alarma)

    def actualizar_hora(self):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        self.lcdNumber.display(hora_actual)

        if self.hora_alarma != "" and hora_actual == self.hora_alarma:
            QtWidgets.QMessageBox.information(self, "Alarma", "¡¡¡ALARMA SONANDO!!!")
            self.hora_alarma = None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
