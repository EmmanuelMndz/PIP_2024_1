import sys
import serial
from PyQt5 import QtCore, uic, QtWidgets

qtCreatorFile = "P6_TestTiposDatos.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.arduino = None
        self.valor = 0
        self.valores_acumulados = ""

        self.btn_accion.clicked.connect(self.accion)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.enviar_valor)

    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            try:
                self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
                self.btn_accion.setText("DESCONECTAR")
                self.timer.start(100)
            except serial.SerialException:
                print("Error al abrir el puerto serie")
        elif texto_boton == "DESCONECTAR" and self.arduino is not None and self.arduino.isOpen():
            self.timer.stop()
            self.arduino.close()
            self.arduino = None
            self.btn_accion.setText("CONECTAR")

    def enviar_valor(self):
        if self.arduino is not None and self.arduino.isOpen():
            self.arduino.write(str(self.valor).encode())
            valor_recibido = self.arduino.readline().strip().decode()
            self.valores_acumulados += valor_recibido + "\n"
            self.txt_valores.setText(self.valores_acumulados)
            self.valor += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
