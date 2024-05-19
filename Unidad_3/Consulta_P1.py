from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("App1")
        self.setFixedWidth(200)
        self.setFixedHeight(200)
        self.texto = QLineEdit("Texto")
        self.boton = QPushButton(text="Oprimir", )
        self.boton.clicked.connect(self.funcion_boton)
        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def funcion_boton(self):
        print("Hola mundo")
        self.texto.setText("Hola Mundo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = MyApp()
    application.show()
    sys.exit(app.exec())


