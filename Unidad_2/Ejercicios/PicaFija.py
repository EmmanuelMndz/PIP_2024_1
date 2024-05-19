import sys
from PyQt5 import uic, QtWidgets
import random

qtCreatorFile = "PicaFija.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class AdivinarNumeroApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_comenzar.clicked.connect(self.iniciar_juego)
        self.btn_comprobar.clicked.connect(self.comprobar_numero)

        self.numero_secreto = ''
        self.intentos = 0

    def random_num(self):
        cifras_disponibles = [str(i) for i in range(1, 10)]
        self.numero_secreto = ''
        for _ in range(4):
            digito = random.choice(cifras_disponibles)
            self.numero_secreto += digito
            cifras_disponibles.remove(digito)

    def iniciar_juego(self):
        self.random_num()
        self.intentos = 0
        self.txt_resultados.clear()
        self.txt_resultados.append("¡Juego iniciado!\nIntroduce un número de 4 cifras. \n")

    def comprobar_numero(self):
        self.intentos += 1
        numero_ingresado = self.txt_numero_ingresado.text()

        if len(numero_ingresado) != 4 or not numero_ingresado.isdigit() or '0' in numero_ingresado or len(set(numero_ingresado)) != 4:
            self.txt_resultados.append("Por favor, introduce un número válido de 4 cifras sin ceros ni cifras repetidas.")
            return

        picas, fijas = self.contador(numero_ingresado)

        if fijas == 4:
            self.txt_resultados.append(f"¡Felicidades! ¡Has adivinado el número en {self.intentos} intentos!")
            self.txt_resultados.append(f"El número secreto era: {self.numero_secreto}")
            self.txt_numero_ingresado.setReadOnly(True)
            return

        self.txt_resultados.clear()
        self.txt_resultados.append(f"Intento #{self.intentos}: - Fijas: {fijas}, Picas: {picas}")

    def contador(self, numero_ingresado):
        print("numero secreto: "+self.numero_secreto)
        picas = 0
        fijas = 0
        for i in range(4):
            if self.numero_secreto[i] == numero_ingresado[i]:
                fijas += 1
            elif numero_ingresado[i] in self.numero_secreto:
                picas += 1
        return picas, fijas

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AdivinarNumeroApp()
    window.show()
    sys.exit(app.exec_())