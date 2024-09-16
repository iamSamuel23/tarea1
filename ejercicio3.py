import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        # Cambia el título de la ventana
        self.setWindowTitle('Ingresar DNI y Nombre')
        # Define la geometría de la ventana (posición x, posición y, ancho, alto)
        self.setGeometry(150, 150, 350, 300)
        
        # Creación de etiquetas
        self.dni_label = QLabel('Número de DNI:', self)
        self.nombre_label = QLabel('Nombre Completo:', self)
        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)
        
        # Campo de entrada para el DNI
        self.dni_input = QLineEdit(self)
        self.dni_input.setPlaceholderText("Número de DNI")
        # Campo de entrada para el nombre
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText("Nombre completo")
        
        # Botón para mostrar los datos ingresados
        self.boton_mostrar = QPushButton('Mostrar Información', self)
        self.boton_mostrar.clicked.connect(self.mostrar_datos)
        
        # Crear un layout vertical y añadir los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.dni_label)
        layout.addWidget(self.dni_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_label)
        
        # Establecer el layout para la ventana principal
        self.setLayout(layout)
    
    def mostrar_datos(self):
        # Método para mostrar los datos ingresados
        dni = self.dni_input.text()  # Obtiene el texto ingresado en el campo de entrada del DNI
        nombre = self.nombre_input.text()  # Obtiene el texto ingresado en el campo de entrada del nombre
        
        # Verifica si ambos campos tienen datos
        if dni and nombre:
            self.resultado_label.setText(f'DNI: {dni}\nNombre: {nombre}')  # Actualiza la etiqueta con el DNI y el nombre
        else:
            self.resultado_label.setText('Por favor, ingrese ambos datos.')  # Muestra un mensaje si faltan datos

# Bloque principal que se ejecuta cuando se inicia la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crear una instancia de la aplicación
    ventana = VentanaPrincipal()  # Crear una instancia de la ventana principal
    ventana.show()  # Mostrar la ventana principal
    sys.exit(app.exec_())  # Ejecutar el bucle de eventos de la aplicación
