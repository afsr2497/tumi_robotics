from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from views import view_1
import cv2
import numpy

class view_2_con():
    def __init__(self,tumi_view):
        self.tumi_view = tumi_view
        self.tumi_view.btn_connect.clicked.connect(self.btn_connect_clicked)
        self.tumi_view.btn_disconn.clicked.connect(self.btn_disconn_clicked)
        self.tumi_view.btn_enCam.clicked.connect(self.btn_enCam_clicked)
        self.tumi_view.btn_dsCam.clicked.connect(self.btn_dsCam_clicked)
    
    def btn_connect_clicked(self):
        fuente1 = "http://192.168.137.5:8085/?action=stream"
        fuente2 = "http://192.168.137.5:8080/?action=stream"
        self.vid1 = camara(fuente1)
        self.vid1.update_cam.connect(self.update_img)
        self.vid1.start()
        self.vid2 = camara(fuente2)
        self.vid2.update_cam.connect(self.update_img_1)
        self.vid2.start()
        print("hola")
    
    def btn_disconn_clicked(self):
        print("Se presiono el boton desconectado")
    
    def btn_enCam_clicked(self):
        print("Se presionp el boton habilitar camara")
    
    def btn_dsCam_clicked(self):
        print("Se presionp el boton deshabilitar camara")
    
    def update_img(self,img):
        qt_img = self.convert_cv_qt(img)
        self.tumi_view.cam1_vid.setPixmap(qt_img)
    
    def convert_cv_qt(self,img):
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(600, 480, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def update_img_1(self,img):
        qt_img = self.convert1_cv_qt(img)
        self.tumi_view.cam2_vid.setPixmap(qt_img)
    
    def convert1_cv_qt(self,img):
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(600, 480, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


class camara(QThread):
    update_cam = pyqtSignal(numpy.ndarray)
    def __init__(self,fuente):
        super().__init__()
        self.cap = cv2.VideoCapture(fuente)
    
    def run(self):
        while(True):
            ret, cv_img = self.cap.read()
            if ret:
                self.update_cam.emit(cv_img)
