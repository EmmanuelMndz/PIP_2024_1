import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P7_EscrituraDatosArduino.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class LedControlApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.arduino = None
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)

        self.btn_accion.clicked.connect(self.accion)
        self.txt_numero.returnPressed.connect(self.enviar_valor)

    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            try:
                self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
                self.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")
            except serial.SerialException:
                print("Error al abrir el puerto serie")
        elif texto_boton == "DESCONECTAR" and self.arduino is not None and self.arduino.isOpen():
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
        else:
            if self.arduino is not None and not self.arduino.isOpen():
                self.arduino.open()
                self.segundoPlano.start(100)
                self.btn_accion.setText("DESCONECTAR")

    def enviar_valor(self):
        valor = self.txt_numero.text()
        if self.arduino is not None and self.arduino.isOpen():
            self.arduino.write(valor.encode())
            valor_recibido = self.arduino.readline().strip().decode()
            self.txt_valores.append(valor_recibido)

    def lecturaArduino(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.arduino.inWaiting():
                cadena = self.arduino.readline()
                cadena = cadena.decode()
                cadena = cadena.strip()
                if cadena != "":
                    self.txt_valores.append(cadena)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LedControlApp()
    window.show()
    sys.exit(app.exec_())
