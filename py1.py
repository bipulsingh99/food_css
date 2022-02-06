import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
class speedometer(QWidget):
    def __init__(self):
        super(speedometer,self).__init__()
        self.width=500
        self.height=500
        self.radius=100
        self.eradius=400
        self.cradius=200
        self.x=150
        self.y=350
        self.angle=0
        self.init_UI()
        
        
    def init_UI(self):
        self.setGeometry(100,100,600,600)
        self.setWindowTitle("speedometer")
        self.inc=QCheckBox("increase",self);
        self.inc.setGeometry(300,400,100,100)
        self.inc.clicked.connect(self.increase)
        
        self.dec=QCheckBox("decrease",self);
        self.dec.setGeometry(400,400,100,100)
        self.dec.clicked.connect(self.decrease)
        
    
    def increase(self):
        self.angle+=10;
        if(self.angle>180):
          self.angle=180
        print(self.angle)
        
        self.x=150+self.cradius-int(self.cradius*math.cos(math.radians(self.angle)))
        self.y=350-int(self.cradius*math.sin(math.radians(self.angle)))
        self.update()
    def decrease(self):
        self.angle-=10;
        print(self.angle)
        if(self.angle<0):
          self.angle=0
        self.x=150+self.cradius-int(self.cradius*math.cos(math.radians(self.angle)))
        self.y=350-int(self.cradius*math.sin(math.radians(self.angle)))
        self.update()
       
    
    
    def draw_circle(self):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.black,  8, Qt.SolidLine))

        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))

        painter.drawEllipse(self.width/2+self.radius-20,self.height/2+self.radius-20, 25,25)
        painter.drawArc(self.width/2-self.radius,self.height/2-self.radius,self.eradius,self.eradius,0*16,180*16)
        
        painter.setPen(QPen(Qt.red,  8, Qt.SolidLine))
        painter.drawLine(self.width/2+self.radius-8,self.height/2+self.radius-8,self.x,self.y)
        painter.setPen(QPen(Qt.blue,  5, Qt.SolidLine))
        for i in range(0,181,10):
          self.x=150+self.cradius-int(self.cradius*math.cos(math.radians(i)))
          self.y=350-int(self.cradius*math.sin(math.radians(i)))

          self.xx=150+(self.cradius-5)-int(self.cradius*math.cos(math.radians(i)))
          self.yy=350-int((self.cradius-5)*math.sin(math.radians(i)))
          painter.drawLine(self.xx,self.yy,self.x,self.y)
        
        

    def paintEvent(self, event):
        self.draw_circle()
       
if __name__=="__main__":
   app=QApplication(sys.argv)
   win=speedometer();
   win.show();
   sys.exit(app.exec_())
