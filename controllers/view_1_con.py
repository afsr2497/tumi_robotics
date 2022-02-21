from email import message
from tkinter import messagebox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from views import view_0, view_1, view_2
from model.robot import robot
import pickle
import re

class view_1_con:
    def __init__(self,tumi_view,robot_view):
        self.tumi_view = tumi_view
        self.robot_view = robot_view

        #Conexion con funciones de los botones
        self.robot_view.btn_cerrar.clicked.connect(self.robot_view.close)
        self.robot_view.btn_aplicar.clicked.connect(self.save_robot)

    def save_robot(self):
        cargar_robots = open("robots/tumi.obj","rb")
        tumi_robots = pickle.load(cargar_robots)
        cargar_robots.close()
        nombre = self.robot_view.nombre.text()
        ip = self.robot_view.ip.text()
        tumi_robot = robot(nombre,ip)
        if tumi_robots is not None:
            tumi_robots.append(tumi_robot)
        else:
            tumi_robots = [tumi_robot]
        tumi_save = open("robots/tumi.obj","wb")
        pickle.dump(tumi_robots,tumi_save)
        tumi_save.close()
        self.actualizar_robots()
        self.robot_view.close()
    
    def actualizar_robots(self):
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
                self.tumi_view.combo_seleccion.addItem(elemento.nombre + elemento.ip)