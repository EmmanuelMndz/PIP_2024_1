import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P2_TiposDatos.ui"
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
                # Imprimir valores en el QLineEdit
                valores = "short: {}, byte: {}, int: {}, long: {}, float: {}, double: {}, char: {}, bool: {}, string: {}, array: {}".format(
                    10, 20, 30, 40, 3.14, 6.28, 'a', True, "Hola", [1, 2, 3, 4, 5]
                )
                self.txt_valores.setText(valores)
            except serial.SerialException:
                print("Error al abrir el puerto serie")
        elif texto_boton == "DESCONECTAR" and self.arduino is not None and self.arduino.isOpen():
            self.arduino.close()
            self.arduino = None
            self.btn_accion.setText("CONECTAR")
        else:
            if self.arduino is not None and not self.arduino.isOpen():
                self.arduino.open()
                self.btn_accion.setText("DESCONECTAR")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LedControlApp()
    window.show()
    sys.exit(app.exec_())
