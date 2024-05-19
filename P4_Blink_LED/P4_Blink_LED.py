import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P4_Blink_LED.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class PotenciometroApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.arduino = None

        self.btn_accion.clicked.connect(self.accion)
        self.txt_com.returnPressed.connect(self.accion)

    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            try:
                self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
                self.arduino.write(b'C')
                self.btn_accion.setText("DESCONECTAR")
            except serial.SerialException:
                print("Error al abrir el puerto serie")
        elif texto_boton == "DESCONECTAR" and self.arduino is not None and self.arduino.isOpen():
            self.arduino.close()
            self.arduino = None
            self.btn_accion.setText("CONECTAR")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PotenciometroApp()
    window.show()
    sys.exit(app.exec_())
