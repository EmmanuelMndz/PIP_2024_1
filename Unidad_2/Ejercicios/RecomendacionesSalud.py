import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap

qtCreatorFile = "RecomendacionesSalud.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.calcular_imc)

    def calcular_imc(self):
        altura_texto = self.lineEdit_altura.text()
        peso_texto = self.lineEdit_peso.text()

        if altura_texto and peso_texto:
            try:
                altura = float(altura_texto)
                peso = float(peso_texto)

                if altura > 0 and peso > 0:
                    # Calcular el IMC
                    imc = peso / (altura ** 2)
                    self.label_imc.setText(f"Tu IMC es: {imc:.2f}")

                    if imc < 18.5:
                        self.label_recomendaciones.setText(
                            "Estás bajo peso. Te recomendamos una dieta "
                            "equilibrada y ejercicios de fuerza.")
                        self.label_imagen.setPixmap(QPixmap("C:/Users/Joseph Stefano/Desktop/PIP_2024_1/Resource/bajo_peso.jpg"))
                    elif 18.5 <= imc < 24.9:
                        self.label_recomendaciones.setText(
                            "Tu peso es normal. Sigue manteniendo un "
                            "estilo de vida saludable.")
                        self.label_imagen.setPixmap(QPixmap("C:/Users/Joseph Stefano/Desktop/PIP_2024_1/Resource/normal.jpg"))
                    elif 25 <= imc < 29.9:
                        self.label_recomendaciones.setText(
                            "Tienes sobrepeso. Te recomendamos reducir la "
                            "ingesta de calorías y hacer más ejercicio.")
                        self.label_imagen.setPixmap(QPixmap("C:/Users/Joseph Stefano/Desktop/PIP_2024_1/Resource/sobrepeso.jpg"))
                    elif imc >= 30:
                        self.label_recomendaciones.setText(
                            "Tienes obesidad. Es importante consultar a un "
                            "profesional de la salud para recibir asesoramiento.")
                        self.label_imagen.setPixmap(QPixmap("C:/Users/Joseph Stefano/Desktop/PIP_2024_1/Resource/obesidad.jpg"))
                    else:
                        self.label_recomendaciones.setText(
                            "Error al calcular el IMC.")
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "La altura y el peso deben ser valores positivos.")
            except ValueError:
                QtWidgets.QMessageBox.critical(self, "Error", "La altura y el peso deben ser números válidos.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Por favor ingresa la altura y el peso.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
