import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class MascotasWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Cambia el título de la ventana
        self.setWindowTitle("Información de Animales Domésticos")
        
        # Crear un layout vertical
        layout = QVBoxLayout()
        
        # Lista para almacenar los widgets de cada mascota
        self.animales_domesticos = []
        for i in range(1, 4):
            # Etiqueta para cada mascota
            layout.addWidget(QLabel(f"Animal Doméstico {i}"))
            
            # Campo de entrada para el nombre
            nombre = QLineEdit(self)
            nombre.setPlaceholderText(f"Nombre del animal {i}")
            layout.addWidget(nombre)
            
            # Campo de entrada para la especie
            especie = QLineEdit(self)
            especie.setPlaceholderText(f"Especie del animal {i}")
            layout.addWidget(especie)
            
            # Campo de entrada para la edad
            edad = QLineEdit(self)
            edad.setPlaceholderText(f"Edad del animal {i}")
            layout.addWidget(edad)
            
            # Añadir los campos de entrada a la lista
            self.animales_domesticos.append((nombre, especie, edad))
        
        # Botón para mostrar los datos
        self.boton = QPushButton("Mostrar Información", self)
        self.boton.clicked.connect(self.mostrar_informacion)
        layout.addWidget(self.boton)
        
        # Establecer el layout para la ventana principal
        self.setLayout(layout)

    def mostrar_informacion(self):
        # Método para mostrar los datos ingresados de cada mascota
        for idx, (nombre, especie, edad) in enumerate(self.animales_domesticos, start=1):
            print(f"Animal Doméstico {idx}:")
            print(f"Nombre: {nombre.text()}")
            print(f"Especie: {especie.text()}")
            print(f"Edad: {edad.text()}")
            print("---")

# Crear la aplicación y la ventana
app = QApplication(sys.argv)
ventana = MascotasWindow()
ventana.show()
sys.exit(app.exec_())
