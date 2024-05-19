import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P15_MaquinaEstados_SumaNumeros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MaquinaEstados2(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)

        self.btn_accion.clicked.connect(self.accion)
        self.txt_com.returnPressed.connect(self.accion)
        self.txt_valores.returnPressed.connect(self.enviar_valor)

        self.valores = []

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
        valor = self.txt_valores.text()
        if valor.isdigit():
            self.arduino.write(valor.encode())
            self.valores.append(valor)
            self.txt_valores.clear()

            if len(self.valores) == 2:
                self.valores = []

    def lecturaArduino(self):
        if self.arduino is not None and self.arduino.isOpen():
            while self.arduino.inWaiting():
                cadena = self.arduino.readline().decode().strip()
                if cadena.startswith("Suma de A y B: "):
                    suma = cadena.split(": ")[1]
                    mensaje = "Suma de A y B: " + suma
                    self.txt_resultado.setText(mensaje)
                elif cadena.startswith("Desea repetir?"):
                    mensaje = cadena.strip()
                    self.txt_repetir.setText(mensaje)
                else:
                    print(cadena)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MaquinaEstados2()
    window.show()
    sys.exit(app.exec_())