import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P8_ControlLedPorUsuario.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)
        self.txt_valor.editingFinished.connect(self.encender_led)

    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            try:
                self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
                self.btn_accion.setText("DESCONECTAR")
            except serial.SerialException:
                print("Error al abrir el puerto serie")
        elif texto_boton == "DESCONECTAR" and self.arduino is not None and self.arduino.isOpen():
            self.arduino.close()
            self.arduino = None
            self.btn_accion.setText("RECONECTAR")
        else:
            if self.arduino is not None and not self.arduino.isOpen():
                self.arduino.open()
                self.btn_accion.setText("DESCONECTAR")

    def encender_led(self):
        valor = self.txt_valor.text()
        if self.arduino is not None and self.arduino.isOpen():
            try:
                valor_int = int(valor)
                if valor_int > 0:
                    self.arduino.write(b'13H')
                    self.txt_estado.setText("LED ENCENDIDO")
                elif valor_int <= 0:
                    self.arduino.write(b'13L')
                    self.txt_estado.setText("LED APAGADO")
                else:
                    self.txt_estado.setText("Valor no válido")
            except ValueError:
                self.txt_estado.setText("Ingrese un valor numérico")
        else:
            self.txt_estado.setText("Arduino no conectado")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
