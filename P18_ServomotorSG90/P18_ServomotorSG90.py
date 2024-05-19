import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P18_ServomotorSG90.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ServoControlApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pin_servo = 9
        self.arduino = None

        self.btn_accion.clicked.connect(self.accion)
        self.btn_encender.clicked.connect(self.encender_apagar_motor)
        self.txt_com.returnPressed.connect(self.accion)
        self.btn_encender.clicked.connect(lambda: self.enviar_comando_servo(0))
        self.btn_apagar.clicked.connect(lambda: self.enviar_comando_servo(180))

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
            self.btn_accion.setText("RECONECTAR")
        else:
            if self.arduino is not None and not self.arduino.isOpen():
                self.arduino.open()
                self.btn_accion.setText("DESCONECTAR")

    def enviar_comando_servo(self, angulo):
        if self.arduino is not None and self.arduino.isOpen():
            self.arduino.write(str(angulo).encode())
            QtWidgets.QApplication.processEvents()

    def encender_apagar_motor(self):
        if self.arduino is not None and self.arduino.isOpen():
            if self.btn_encender.isChecked():
                self.arduino.write(b"ON")
                self.btn_encender.setText("Apagar Motor")
            else:
                self.arduino.write(b"OFF")
                self.btn_encender.setText("Encender Motor")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ServoControlApp()
    window.show()
    sys.exit(app.exec_())
