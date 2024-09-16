import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        # Cambia el título de la ventana
        self.setWindowTitle('Ingrese su PIN')
        # Define la geometría de la ventana (posición x, posición y, ancho, alto)
        self.setGeometry(150, 150, 350, 250)
        
        # Creación de una etiqueta con instrucciones
        self.instrucciones_label = QLabel('Ingrese su PIN:', self)
        self.instrucciones_label.setAlignment(Qt.AlignCenter)
        
        # Campo de entrada para el PIN
        self.pin_input = QLineEdit(self)
        self.pin_input.setEchoMode(QLineEdit.Password)  # Establece el modo de entrada como contraseña
        self.pin_input.setPlaceholderText("PIN")
        
        # Botón para mostrar el PIN ingresado
        self.boton_mostrar = QPushButton('Mostrar PIN', self)
        self.boton_mostrar.clicked.connect(self.mostrar_pin)
        
        # Etiqueta para mostrar el resultado
        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)
        
        # Crear un layout vertical y añadir los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.instrucciones_label)
        layout.addWidget(self.pin_input)
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_label)
        
        # Establecer el layout para la ventana principal
        self.setLayout(layout)
    
    def mostrar_pin(self):
        # Método para mostrar el PIN ingresado
        pin = self.pin_input.text()  # Obtiene el texto ingresado en el campo de entrada
        self.resultado_label.setText(f'PIN ingresado: {pin}')  # Actualiza la etiqueta con el PIN

# Bloque principal que se ejecuta cuando se inicia la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crear una instancia de la aplicación
    ventana = VentanaPrincipal()  # Crear una instancia de la ventana principal
    ventana.show()  # Mostrar la ventana principal
    sys.exit(app.exec_())  # Ejecutar el bucle de eventos de la aplicación
