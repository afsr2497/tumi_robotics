from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class view_0(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.main_widgets()
    
    def main_widgets(self):
        #Definicion de las principales caracteristicas de la ventana
        self.setWindowIcon(QIcon("icons/tumi_icon.png"))
        self.setWindowTitle("Tumi Robotics - Mobile Robots")
        self.setMaximumSize(360,480)
        self.setMinimumSize(360,480)
        self.setStyleSheet(open("views/styles.css","r").read())

        #Configuracion de la ventana en el centro de la pantalla
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

        #Definicion de los elementos del view_0
        self.frame_logo = QFrame(self)
        self.label_logo = QLabel(self.frame_logo)
        self.logo_pixmap = QPixmap("images/tumi_logo.png")
        self.frame_seleccion = QFrame(self)
        self.label_seleccion = QLabel(self.frame_seleccion)
        self.label_seleccion.setWordWrap(True)
        self.combo_seleccion = QComboBox(self.frame_seleccion)
        self.frame_opciones = QFrame(self)
        self.btn_crear = QPushButton(self.frame_opciones)
        self.btn_iniciar = QPushButton(self.frame_opciones)
        self.btn_cerrar = QPushButton(self.frame_opciones)

        #Definicion de los selectores para el estilo
        self.frame_logo.setObjectName("small_frame")
        self.frame_seleccion.setObjectName("big_frame")
        self.frame_opciones.setObjectName("small_frame")
        self.label_seleccion.setObjectName("nombre_ind")
        self.btn_iniciar.setObjectName("btn_opciones")
        self.btn_crear.setObjectName("btn_opciones")
        self.btn_cerrar.setObjectName("btn_opciones")

        #Definicion de dimensiones de objetos criticos
        self.label_logo.setMaximumSize(256,256)
        self.label_logo.setMinimumSize(256,256)

        #Definicion de los layouts de los elementos en la ventana
        self.main_layout = QVBoxLayout(self)
        self.layout_logo = QVBoxLayout(self.frame_logo)
        self.layout_seleccion = QHBoxLayout(self.frame_seleccion)
        self.layout_opciones = QHBoxLayout(self.frame_opciones)

        #Agregado de los componentes a los layouts
        self.layout_opciones.addWidget(self.btn_crear,1)
        self.layout_opciones.addWidget(self.btn_iniciar,1)
        self.layout_opciones.addWidget(self.btn_cerrar,1)
        self.layout_seleccion.addWidget(self.label_seleccion,1)
        self.layout_seleccion.addWidget(self.combo_seleccion,1)
        self.label_logo.setPixmap(self.logo_pixmap)
        self.layout_logo.addWidget(self.label_logo,Qt.AlignCenter)
        self.main_layout.addWidget(self.frame_logo,6,Qt.AlignCenter)
        self.main_layout.addWidget(self.frame_seleccion,2)
        self.main_layout.addWidget(self.frame_opciones,2)

        #Label form elements
        self.label_seleccion.setText("Seleccione el robot")
        self.btn_crear.setText("Crear")
        self.btn_iniciar.setText("Iniciar")
        self.btn_cerrar.setText("Cerrar")
