from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from views import view_0, view_1, view_2
import pickle

class view_0_con():
    def __init__(self,tumi_view,robot_view,inspeccion_view):
        self.tumi_view = tumi_view
        self.robot_view = robot_view
        self.inspeccion_view = inspeccion_view
        
        #Conexion con los procedimientos
        self.tumi_view.btn_crear.clicked.connect(self.btn_crear_clicked)
        self.tumi_view.btn_iniciar.clicked.connect(self.btn_iniciar_clicked)
        self.tumi_view.btn_cerrar.clicked.connect(self.tumi_view.close)

        #Add robots to the ComboBox
        self.cargarRobots()

    def iniciar(self):
        self.tumi_view.show()

    def btn_crear_clicked(self):
        self.robot_view.nombre.clear()
        self.robot_view.ip.clear()
        self.robot_view.show()
        
    def btn_iniciar_clicked(self):
        self.inspeccion_view.show()
        self.tumi_view.close()

    def cargarRobots(self):
        self.tumi_view.combo_seleccion.clear()
        self.tumi_view.combo_seleccion.addItem("Seleccionar robot")
        try:
            cargar_robots = open("robots/tumi.obj","rb")
        except:
            tumi_robots = []
            cargar_robots = open("robots/tumi.obj","wb")
            pickle.dump(tumi_robots,cargar_robots)
            cargar_robots = open("robots/tumi.obj","rb")
        tumi_robots = pickle.load(cargar_robots)
        if tumi_robots is not None:
            for elemento in tumi_robots:
                self.tumi_view.combo_seleccion.addItem(elemento.nombre + "   " + elemento.ip)