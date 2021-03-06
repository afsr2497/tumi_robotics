from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys 

class view_2(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.main_widgets()
    
    def main_widgets(self):
        #Set the main features of the window
        self.setWindowIcon(QIcon("icons/tumi_icon.png"))
        self.setWindowTitle("Tumi Robotics - Mobile Robots")
        self.setMinimumSize(800,480)
        self.setStyleSheet(open("views/styles.css","r").read())

        #Definition of the components of the main window
        self.frame_camaras = QFrame(self)
        self.frame_cam1 = QFrame(self.frame_camaras)
        self.cam1_lab = QLabel(self.frame_cam1)
        self.cam1_vid = QLabel(self.frame_cam1)
        self.frame_cam2=QFrame(self.frame_camaras)
        self.cam2_lab = QLabel(self.frame_cam2)
        self.cam2_vid = QLabel(self.frame_cam2)
        self.frame_ind = QFrame(self)
        self.frame_rob = QFrame(self.frame_ind)
        self.frame_btn = QFrame(self.frame_ind)
        self.btn_connect = QPushButton(self.frame_btn)
        self.btn_disconn = QPushButton(self.frame_btn)
        self.btn_enCam = QPushButton(self.frame_btn)
        self.btn_dsCam = QPushButton(self.frame_btn)
        self.frame_vis = QFrame(self.frame_ind)
        self.frame_datos = QFrame(self.frame_vis)
        self.frame_bat = QFrame(self.frame_datos)
        self.frame_vel = QFrame(self.frame_datos)
        self.frame_light = QFrame(self.frame_datos)
        self.frame_sensors = QFrame(self.frame_vis)
        self.frame_com = QFrame(self.frame_sensors)
        self.frame_icom = QFrame(self.frame_sensors)
        self.com_1 = QLabel(self.frame_com)
        self.com_2 = QLabel(self.frame_com)
        self.com_3 = QLabel(self.frame_com)
        self.com_4 = QLabel(self.frame_com)
        self.com_5 = QLabel(self.frame_com)
        self.com_6 = QLabel(self.frame_com)
        self.icom_1 = QProgressBar(self.frame_icom)
        self.icom_2 = QProgressBar(self.frame_icom)
        self.icom_3 = QProgressBar(self.frame_icom)
        self.icom_4 = QProgressBar(self.frame_icom)
        self.icom_5 = QProgressBar(self.frame_icom)
        self.icom_6 = QProgressBar(self.frame_icom)
        self.frame_rep = QFrame(self.frame_ind)
        self.frame_ter = QFrame(self.frame_ind)

        #Set the id selector for the elements of the window
        self.frame_camaras.setObjectName("big_frame")
        self.frame_ind.setObjectName("big_frame")
        self.frame_cam1.setObjectName("middle_frame")
        self.frame_cam2.setObjectName("middle_frame")
        self.cam1_lab.setObjectName("small_frame")
        self.cam1_vid.setObjectName("small_frame")
        self.cam2_lab.setObjectName("small_frame")
        self.cam2_vid.setObjectName("small_frame")
        self.frame_rob.setObjectName("small_frame")
        self.frame_btn.setObjectName("small_frame")
        self.frame_vis.setObjectName("small_frame")
        self.frame_rep.setObjectName("small_frame")
        self.frame_ter.setObjectName("small_frame")
        self.btn_connect.setObjectName("btn_main")
        self.btn_disconn.setObjectName("btn_main")
        self.btn_enCam.setObjectName("btn_main")
        self.btn_dsCam.setObjectName("btn_main")

        #Definition of dimenssion of critic components
        self.com_1.setMaximumSize(80,10)
        self.com_1.setMinimumSize(80,10)
        self.com_2.setMaximumSize(80,10)
        self.com_2.setMinimumSize(80,10)
        self.com_3.setMaximumSize(80,10)
        self.com_3.setMinimumSize(80,10)
        self.com_4.setMaximumSize(80,10)
        self.com_4.setMinimumSize(80,10)
        self.com_5.setMaximumSize(80,10)
        self.com_5.setMinimumSize(80,10)
        self.com_6.setMaximumSize(80,10)
        self.com_6.setMinimumSize(80,10)
        self.icom_1.setMaximumSize(10,10)
        self.icom_2.setMaximumSize(10,10)
        self.icom_3.setMaximumSize(10,10)
        self.icom_4.setMaximumSize(10,10)
        self.icom_5.setMaximumSize(10,10)
        self.icom_6.setMaximumSize(10,10)
        self.btn_connect.setMinimumSize(40,40)
        self.btn_disconn.setMinimumSize(40,40)
        self.btn_enCam.setMinimumSize(40,40)
        self.btn_dsCam.setMinimumSize(40,40)
        self.btn_connect.setMaximumSize(80,80)
        self.btn_disconn.setMaximumSize(80,80)
        self.btn_enCam.setMaximumSize(80,80)
        self.btn_dsCam.setMaximumSize(80,80)
        self.cam1_vid.setMinimumSize(600,400)
        self.cam1_vid.setMaximumSize(600,400)
        self.cam2_vid.setMinimumSize(600,400)
        self.cam2_vid.setMaximumSize(600,400)
       

        #Definitions of the layouts
        self.main_layout = QVBoxLayout(self)
        self.layout_camaras = QHBoxLayout(self.frame_camaras)
        self.layout_cam1 = QVBoxLayout(self.frame_cam1)
        self.layout_cam2 = QVBoxLayout(self.frame_cam2)
        self.layout_ind = QHBoxLayout(self.frame_ind)
        self.layout_vis = QHBoxLayout(self.frame_vis)
        self.layout_datos = QVBoxLayout(self.frame_datos)
        self.layout_sensors = QHBoxLayout(self.frame_sensors)
        self.layout_com = QVBoxLayout(self.frame_com)
        self.layout_icom = QVBoxLayout(self.frame_icom)
        self.layout_btn = QGridLayout(self.frame_btn)

        #Setting the position of the components in layouts
        self.layout_btn.addWidget(self.btn_connect,1,1,Qt.AlignCenter)
        self.layout_btn.addWidget(self.btn_disconn,1,2,Qt.AlignCenter)
        self.layout_btn.addWidget(self.btn_enCam,2,1,Qt.AlignCenter)
        self.layout_btn.addWidget(self.btn_dsCam,2,2,Qt.AlignCenter)
        self.layout_com.addWidget(self.com_1,1,Qt.AlignLeft|Qt.AlignCenter)
        self.layout_com.addWidget(self.com_2,1,Qt.AlignLeft|Qt.AlignCenter)
        self.layout_com.addWidget(self.com_3,1,Qt.AlignLeft|Qt.AlignCenter)
        self.layout_com.addWidget(self.com_4,1,Qt.AlignLeft|Qt.AlignCenter)
        self.layout_com.addWidget(self.com_5,1,Qt.AlignLeft|Qt.AlignCenter)
        self.layout_com.addWidget(self.com_6,1,Qt.AlignLeft|Qt.AlignCenter)
        self.layout_icom.addWidget(self.icom_1,1,Qt.AlignCenter)
        self.layout_icom.addWidget(self.icom_2,1,Qt.AlignCenter)
        self.layout_icom.addWidget(self.icom_3,1,Qt.AlignCenter)
        self.layout_icom.addWidget(self.icom_4,1,Qt.AlignCenter)
        self.layout_icom.addWidget(self.icom_5,1,Qt.AlignCenter)
        self.layout_icom.addWidget(self.icom_6,1,Qt.AlignCenter)
        self.layout_sensors.addWidget(self.frame_com,6)
        self.layout_sensors.addWidget(self.frame_icom,3)
        self.layout_datos.addWidget(self.frame_bat,1)
        self.layout_datos.addWidget(self.frame_vel,1)
        self.layout_datos.addWidget(self.frame_light,1)
        self.layout_vis.addWidget(self.frame_datos,1)
        self.layout_vis.addWidget(self.frame_sensors,1)
        self.layout_ind.addWidget(self.frame_rob,5)
        self.layout_ind.addWidget(self.frame_btn,6)
        self.layout_ind.addWidget(self.frame_vis,15)
        self.layout_ind.addWidget(self.frame_rep,6)
        self.layout_ind.addWidget(self.frame_ter,5)
        self.layout_cam1.addWidget(self.cam1_lab,2)
        self.layout_cam1.addWidget(self.cam1_vid,25,Qt.AlignCenter)
        self.layout_cam2.addWidget(self.cam2_lab,2)
        self.layout_cam2.addWidget(self.cam2_vid,25,Qt.AlignCenter)
        self.layout_camaras.addWidget(self.frame_cam1)
        self.layout_camaras.addWidget(self.frame_cam2)
        self.main_layout.addWidget(self.frame_camaras,20)
        self.main_layout.addWidget(self.frame_ind,8)
