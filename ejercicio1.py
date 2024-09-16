import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

# Definición de la clase VentanaPrincipal que hereda de QWidget
class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        # Establece el título de la ventana
        self.setWindowTitle('Información Personal')
        # Define la geometría de la ventana (posición x, posición y, ancho, alto)
        self.setGeometry(200, 150, 350, 250)
        
        # Creación de etiquetas con texto
        self.nombre_label = QLabel('Nombre Completo: María Gómez', self)
        self.edad_label = QLabel('Edad: 30 años', self)
        
        # Alineación de las etiquetas al centro
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.edad_label.setAlignment(Qt.AlignCenter)
        
        # Crear un layout vertical y añadir las etiquetas al layout
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.edad_label)
        
        # Establecer el layout para la ventana principal
        self.setLayout(layout)

# Bloque principal que se ejecuta cuando se inicia la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crear una instancia de la aplicación
    ventana = VentanaPrincipal()  # Crear una instancia de la ventana principal
    ventana.show()  # Mostrar la ventana principal
    sys.exit(app.exec_())  # Ejecutar el bucle de eventos de la aplicación
