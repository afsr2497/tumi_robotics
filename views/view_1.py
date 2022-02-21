from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys 

class view_1(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.main_widgets()
    
    def main_widgets(self):
        self.setWindowIcon(QIcon("icons/tumi_icon.png"))
        self.setWindowTitle("Tumi Robotics - Crear robot")
        self.setWindowModality(Qt.ApplicationModal)
        self.setMinimumSize(300,240)
        self.setMaximumSize(300,240)
        self.setStyleSheet(open("views/styles.css","r").read())

        #Configuracion de la ventana en el centro de la pantalla
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())
        
        #Elements on the window
        self.frame_datos = QFrame(self)
        self.label_nombre = QLabel(self.frame_datos)
        self.label_ip = QLabel(self.frame_datos)
        self.nombre = QLineEdit(self.frame_datos)
        self.ip = QLineEdit(self.frame_datos)
        self.frame_opciones = QFrame(self)
        self.btn_aplicar = QPushButton(self.frame_opciones)
        self.btn_cerrar = QPushButton(self.frame_opciones)

        #Setting the name of the elements to apply styling
        self.frame_datos.setObjectName("big_frame")
        self.frame_opciones.setObjectName("middle_frame")
        self.btn_aplicar.setObjectName("btn_opciones")
        self.btn_cerrar.setObjectName("btn_opciones")  
        self.label_nombre.setObjectName("nombre_ind")
        self.label_ip.setObjectName("nombre_ind")

        #Creating the layouts of the parent elements
        self.main_layout = QVBoxLayout(self)
        self.layout_datos = QGridLayout(self.frame_datos)
        self.layout_datos.setColumnStretch(1,1)
        self.layout_datos.setColumnStretch(2,1)
        self.layout_datos.setRowStretch(1,1)
        self.layout_datos.setRowStretch(2,1)
        self.layout_opciones = QHBoxLayout(self.frame_opciones)

        #Adding the elements to the layouts
        self.layout_datos.addWidget(self.label_nombre,1,1)
        self.layout_datos.addWidget(self.label_ip,2,1)
        self.layout_datos.addWidget(self.nombre,1,2)
        self.layout_datos.addWidget(self.ip,2,2)
        self.layout_opciones.addWidget(self.btn_aplicar)
        self.layout_opciones.addWidget(self.btn_cerrar)
        self.main_layout.addWidget(self.frame_datos,7)
        self.main_layout.addWidget(self.frame_opciones,3)

        #Setting the labels of the different elements
        self.label_nombre.setText("Nombre del robot")
        self.label_ip.setText("IP del robot")
        self.btn_aplicar.setText("Crear robot")
        self.btn_cerrar.setText("Cerrar")