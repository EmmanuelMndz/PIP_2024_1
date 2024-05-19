import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P1_Intro.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class LedControlApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.arduino = None

        self.btn_accion.clicked.connect(self.accion)

    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            try:
                self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
                self.btn_accion.setText("DESCONECTAR")
                self.lbl_estado.setText("¡Hola! Este es mi primer programa.")
            except serial.SerialException:
                print("Error al abrir el puerto serie")
        elif texto_boton == "DESCONECTAR" and self.arduino is not None and self.arduino.isOpen():
            self.arduino.close()
            self.arduino = None
            self.btn_accion.setText("CONECTAR")
            self.lbl_estado.setText("Desconectado")
        else:
            if self.arduino is not None and not self.arduino.isOpen():
                self.arduino.open()
                self.btn_accion.setText("DESCONECTAR")
                self.lbl_estado.setText("Conexión establecida. ¡Hola! Este es mi primer programa.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LedControlApp()
    window.show()
    sys.exit(app.exec_())
