import sys
from PyQt5 import uic, QtWidgets, QtGui
from random import randint, choice

qtCreatorFile = "ExamenBasico.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton_iniciar.clicked.connect(self.iniciar_examen)
        self.pushButton_verificar.clicked.connect(self.verificar_respuesta)

        self.respuestas_correctas = 0
        self.total_preguntas = 5
        self.preguntas_realizadas = 0
        self.examen_completado = False

    def iniciar_examen(self):
        self.respuestas_correctas = 0
        self.preguntas_realizadas = 0
        self.examen_completado = False
        self.label_resultado.setText("")
        self.lineEdit_respuesta.setText("")
        self.realizar_pregunta()

    def realizar_pregunta(self):
        if not self.examen_completado and self.preguntas_realizadas < self.total_preguntas:
            num1 = randint(1, 10)
            num2 = randint(1, 10)
            operadores = ['+', '-', '*', '/']
            operador = choice(operadores)

            if operador == '+':
                respuesta = num1 + num2
            elif operador == '-':
                respuesta = num1 - num2
            elif operador == '*':
                respuesta = num1 * num2
            else:
                respuesta = num1 / num2

            self.label_pregunta.setText(f"{num1} {operador} {num2} = ?")
            self.respuesta_correcta = respuesta
            self.lineEdit_respuesta.clear()
        else:
            if not self.examen_completado:
                self.mostrar_calificacion()

    def verificar_respuesta(self):
        if not self.examen_completado:
            respuesta_ingresada = self.lineEdit_respuesta.text()
            try:
                respuesta_ingresada = float(respuesta_ingresada)
                if respuesta_ingresada == self.respuesta_correcta:
                    self.respuestas_correctas += 1
                self.preguntas_realizadas += 1
                self.realizar_pregunta()
            except ValueError:
                self.label_resultado.setText("Ingresa un número válido")

    def mostrar_calificacion(self):
        self.examen_completado = True
        calificacion = (self.respuestas_correctas / self.total_preguntas) * 10
        mensaje = f"{calificacion}"
        self.label_resultado.setText(mensaje)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
