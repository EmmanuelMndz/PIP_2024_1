import sys
import serial
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P9_ControlEDS_Array.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class LedControlApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = serial.Serial(port='COM5', baudrate=9600, timeout=1)  # Reemplaza 'COM5' con el puerto COM correcto
        self.arduino.timeout = 1

        # Inicializar los estados de los LEDs
        self.estados = [False] * 8

        self.btn_accion.clicked.connect(self.accion)

        self.btn_led_1.clicked.connect(lambda: self.toggle_led(0))
        self.btn_led_2.clicked.connect(lambda: self.toggle_led(1))
        self.btn_led_3.clicked.connect(lambda: self.toggle_led(2))
        self.btn_led_4.clicked.connect(lambda: self.toggle_led(3))
        self.btn_led_5.clicked.connect(lambda: self.toggle_led(4))
        self.btn_led_6.clicked.connect(lambda: self.toggle_led(5))
        self.btn_led_7.clicked.connect(lambda: self.toggle_led(6))
        self.btn_led_8.clicked.connect(lambda: self.toggle_led(7))

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

    def toggle_led(self, idx):
        # Cambiar el estado del LED correspondiente
        self.estados[idx] = not self.estados[idx]
        # Enviar el estado actualizado al Arduino
        self.arduino.write(str(idx + 1).encode())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LedControlApp()
    window.show()
    sys.exit(app.exec_())
