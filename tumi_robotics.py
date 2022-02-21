from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from views import view_1,view_0, view_2
from controllers import view_0_con,view_1_con,view_2_con
from model.robot import robot
import sys

if __name__=='__main__':
    tumi_robotics = QApplication(sys.argv)
    tumi_view = view_0.view_0()
    robot_view = view_1.view_1()
    inspeccion_view = view_2.view_2()
    tumi_con = view_0_con.view_0_con(tumi_view,robot_view,inspeccion_view)
    robot_con = view_1_con.view_1_con(tumi_view,robot_view)
    inspeecion_con = view_2_con.view_2_con(inspeccion_view)
    tumi_con.iniciar()
    sys.exit(tumi_robotics.exec_())