import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime, time
from PyQt5.QtGui import QMovie

qtCreatorFile = "SimuladorAlarma.ui" # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.mostrar_gif()

    def mostrar_gif(self):
        ruta_gif = r"C:/Users/Joseph Stefano/Desktop/PIP_2024_1/Resource/reloj_gif.gif"
        movie = QMovie(ruta_gif)
        self.label.setMovie(movie)
        movie.start()

        self.btn_establecer_alarma.clicked.connect(self.establecer_alarma)

        self.hora_alarma = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)

    def establecer_alarma(self):
        hora_alarma, ok = QtWidgets.QInputDialog.getText(self, 'Establecer Alarma', 'Ingrese la hora de la alarma:')
        if ok:
            try:
                self.hora_alarma = self.procesar_formato_hora(hora_alarma)
                self.lbl_alarma.setText("Alarma establecida a las " + hora_alarma)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Error", "Formato de hora incorrecto")

    def procesar_formato_hora(self, hora):
        formatos = ['%H:%M', '%H:%M:%S']
        for formato in formatos:
            try:
                return datetime.strptime(hora, formato).time()
            except ValueError:
                pass
        raise ValueError("Formato no reconocido")

    def actualizar_hora(self):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        self.lbl_hora_actual.setText(hora_actual)

        if self.hora_alarma is not None and hora_actual == self.hora_alarma.strftime("%H:%M:%S"):
            QtWidgets.QMessageBox.information(self, "Alarma", "¡¡¡ALARMA SONANDO!!!")
            self.hora_alarma = None

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
