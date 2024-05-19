import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P14_MaquinaEstados_SumaNumeros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MaquinaEstados1(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None
        self.valores = []

        self.btn_accion.clicked.connect(self.accion)
        self.txt_com.returnPressed.connect(self.accion)
        self.txt_valores.returnPressed.connect(self.enviar_valor)

        self.estado = 0

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

    def enviar_valor(self):
        valor = self.txt_valores.text()
        if valor.isdigit():
            self.arduino.write(valor.encode())
            self.valores.append(int(valor))
            self.txt_valores.clear()

            if len(self.valores) == 2:
                suma = sum(self.valores)
                mensaje = "Suma de A y B: " + str(suma)
                self.txt_resultado.setText(mensaje)
                self.valores = []
                self.estado = 2

    def lecturaArduino(self):
        if self.arduino is not None and self.arduino.isOpen():
            while self.arduino.inWaiting():
                cadena = self.arduino.readline().decode().strip()
                if cadena.startswith("Suma de A y B: "):
                    suma = cadena.split(": ")[1]
                    mensaje = "Suma de A y B: " + suma
                    self.txt_resultado.setText(mensaje)
                    self.estado = 3
                elif cadena.startswith("Desea repetir?"):
                    respuesta = cadena.strip()
                    if respuesta == "1":
                        self.estado = 0
                    else:
                        self.estado = 4

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MaquinaEstados1()
    window.show()
    sys.exit(app.exec_())
