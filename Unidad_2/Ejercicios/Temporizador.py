import sys
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTime

qtCreatorFile = "Temporizador.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.mostrar_gif()

        # Área de los Signals
        self.btn_iniciar.clicked.connect(self.iniciar)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_temporizador)

    def mostrar_gif(self):
        # Ruta al archivo GIF
        ruta_gif = r"C:/Users/Joseph Stefano/Desktop/PIP_2024_1/Resource/reloj_gif.gif"

        # Crear un objeto QMovie con el GIF
        movie = QMovie(ruta_gif)
        self.label.setMovie(movie)

        # Reproducir el GIF
        movie.start()

    def iniciar(self):
        tiempo_str, ok = QtWidgets.QInputDialog.getText(self, 'Configurar Temporizador', 'Ingrese el tiempo:')
        if ok:
            tiempo = self.convertir_a_segundos(tiempo_str)
            if tiempo is not None:
                self.tiempo_restante = tiempo
                self.txt_contador.setText(self.formatear_tiempo(self.tiempo_restante))
                self.timer.start(1000)

    def convertir_a_segundos(self, tiempo_str):
        tiempo_str = tiempo_str.lower()  # Convertir a minúsculas para simplificar la manipulación
        tiempo_str = tiempo_str.replace("seg", "")  # Eliminar "seg" de la cadena si está presente
        partes = tiempo_str.split(":")
        horas, minutos, segundos = 0, 0, 0

        # Analizar las partes de la cadena y determinar horas, minutos y segundos
        if len(partes) == 1:  # Solo segundos o minutos
            if "m" in partes[0]:  # Si hay "m" en la cadena, considerarlo como minutos
                minutos = int(partes[0].replace("m", ""))
            else:  # De lo contrario, considerarlo como segundos
                segundos = int(partes[0])
        elif len(partes) == 2:  # Horas y minutos o minutos y segundos
            if "m" in partes[1]:  # Si hay "m" en la segunda parte, considerarlo como minutos
                horas = int(partes[0])
                minutos = int(partes[1].replace("m", ""))
            else:  # De lo contrario, considerarlo como minutos y segundos
                minutos = int(partes[0])
                segundos = int(partes[1])
        elif len(partes) == 3:  # Horas, minutos y segundos
            horas = int(partes[0])
            minutos = int(partes[1])
            segundos = int(partes[2])

        # Calcular el total de segundos
        total_segundos = horas * 3600 + minutos * 60 + segundos
        return total_segundos

    def formatear_tiempo(self, segundos):
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        segundos = segundos % 60
        return "{:02}:{:02}:{:02}".format(horas, minutos, segundos)

    def actualizar_temporizador(self):
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.txt_contador.setText(self.formatear_tiempo(self.tiempo_restante))
        else:
            self.timer.stop()
            QtWidgets.QMessageBox.information(self, "Temporizador", "¡¡¡Temporizador finalizado!!!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
