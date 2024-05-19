import sys
from PyQt5 import uic, QtWidgets, QtCore
import time

qtCreatorFile = "SimulacionSemaforo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configurar botones
        self.btn_start.clicked.connect(self.iniciar_semaforo)
        self.btn_end.clicked.connect(self.detener_semaforo)
        self.colores = ['green', 'yellow', 'red']
        self.indice_color = 0
        self.semaphore_running = False

    def iniciar_semaforo(self):
        if not self.semaphore_running:
            self.semaphore_running = True
            self.btn_start.setEnabled(False)
            self.btn_end.setEnabled(True)
            self.actualizar_semaforo()

    def detener_semaforo(self):
        self.semaphore_running = False
        self.btn_start.setEnabled(True)
        self.btn_end.setEnabled(False)

    def actualizar_semaforo(self):
        if self.semaphore_running:
            color = self.colores[self.indice_color]
            self.indice_color = (self.indice_color + 1) % len(self.colores)

            for lbl in [self.semaphore_image_green, self.semaphore_image_yellow, self.semaphore_image_red]:
                lbl.setStyleSheet("background-color: white ")
            if color == 'red':
                self.semaphore_image_red.setStyleSheet("background-color: red")
            elif color == 'yellow':
                self.semaphore_image_yellow.setStyleSheet("background-color: yellow")
            elif color == 'green':
                self.semaphore_image_green.setStyleSheet("background-color: green")
            QtCore.QTimer.singleShot(2000, self.actualizar_semaforo)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
