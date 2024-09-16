import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class PersonaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos de una Persona")
        
        layout = QVBoxLayout()
 
        caracteristicas_especificas = [
            "Altura (cm)", "Peso (kg)", "Color de cabello", "Color de ojos", "Tono de piel", # Físicas
            "Personalidad", "Habilidades", "Emociones predominantes", "Nivel de estrés", "Capacidad de concentración" # Mentales
        ]
 
        self.caracteristicas = []
        for i, caracteristica in enumerate(caracteristicas_especificas, start=1):
            label = QLabel(f"{i}. {caracteristica}", self)
            layout.addWidget(label)
            
            campo = QLineEdit(self)
            campo.setPlaceholderText(f"Ingrese {caracteristica}")
            layout.addWidget(campo)
            
            self.caracteristicas.append(campo)
 
        self.boton = QPushButton("Mostrar Datos", self)
        self.boton.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton)
 
        self.setLayout(layout)

    def mostrar_datos(self):
        caracteristicas_especificas = [
            "Altura", "Peso", "Color de cabello", "Color de ojos", "Tono de piel",
            "Personalidad", "Habilidades", "Emociones predominantes", "Nivel de estrés", "Capacidad de concentración"
        ]

        for idx, (campo, nombre) in enumerate(zip(self.caracteristicas, caracteristicas_especificas), start=1):
            print(f"{nombre}: {campo.text()}")
 
app = QApplication(sys.argv)
ventana = PersonaWindow()
ventana.show()
sys.exit(app.exec_())
