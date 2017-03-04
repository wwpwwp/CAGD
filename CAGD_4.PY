from CAGD_A import Ui_cagd_0  
import crash_on_ipy
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,\
     QLineEdit,QLabel,QVBoxLayout,QHBoxLayout,QPushButton,\
     QMessageBox
from PyQt5.QtOpenGL import QGLWidget
from OpenGL import GL,GLU
from PyQt5 import QtGui,QtCore
from deboor_in import deboor
from basis_in import Basis

global myn,mystart,myfinish,myk,mytype,mypoint,myu,adjust,my_mouse_move_i
myn=0
mystart=0                  #选点标志
myfinish=0                 #画线标志
myadjust=False             #调整点位置开关
my_mouse_move=0            #要调整的点
myk=3                      #次数
mypoint=[[0],[0]]          #点坐标
myu=[]                     #节点
mytype=0                   #类型
for i in range(50):
    myu.append(i/10)
    
    
class OpenglWidget_1(QGLWidget):
    def __init__(self):
        super().__init__()
#        self.resize(300, 300)
        
    def paintGL(self):
        GL.glClearColor(1.0, 1.0, 1.0, 0.0)             #白颜色
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)       
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(-20.0, 530.0, -20.0, 280.0)      #左下角右上角x左下角右上角y
        
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        GL.glPointSize(5.0)                             #点大小设置

        self.myline1()                                  #画方框
        self.mypp1()                                    #选择点
        if myfinish and myn:
            self.mypp2()                                #画线
        
    def mypp1(self):                                    #选择点
        for i in range(myn):
            GL.glColor3f(0.0, 0.0, 0.0)
            GL.glBegin(GL.GL_POINTS)
            GL.glVertex2d(mypoint[0][i+1],mypoint[1][i+1])
            GL.glEnd()
    def mypp2(self):                                    #画线
        GL.glColor3f(1.0, 0.0, 1.0)
        for i in range(myn-1):                          #画线
            GL.glBegin(GL.GL_LINES)
            GL.glVertex2d(mypoint[0][i+1],mypoint[1][i+1])
            GL.glVertex2d(mypoint[0][i+2],mypoint[1][i+2])
            GL.glEnd()
        if myadjust:
            GL.glColor3f(1.0, 0.0, 0.0)
        else:
            GL.glColor3f(0.0, 0.0, 1.0)
        if mytype==0:                                #均匀B样条画线
            my_pp2_a=myk/(myk+myn)                   #起始节点
            my_pp2_a_1=myk+myn                       #节点个数
            my_pp2_a_2=(myn-myk)/(myk+myn)/100       #节点步长
                
            for i in range(100):                     #每步处理                
                my_pp2_a2=my_pp2_a+my_pp2_a_2
                debi=0
                debj=0
                for j in range(my_pp2_a_1):
                    if myu[j]<=my_pp2_a<myu[j+1]:
                        debi=j                 
                debj=debi-myk
                x,y=deboor(myu,mypoint,my_pp2_a,myk,debj,debi,myk)
                x2,y2=deboor(myu,mypoint,my_pp2_a2,myk,debj,debi,myk)
                GL.glBegin(GL.GL_LINES)
                GL.glVertex2d(x,y)
                GL.glVertex2d(x2,y2)
                GL.glEnd()
                my_pp2_a=my_pp2_a2
                    
        if mytype==1:                                #分段Bezier画线
            my_pp2_b=0                               #起始节点
            my_pp2_b_1=myn+myk                       #节点个数
            my_pp2_b_2=0.01                          #节点步长   
            for i in range(100):                     #每步处理                
                my_pp2_b2=my_pp2_b+my_pp2_b_2
                debi=0
                debj=0
                for j in range(my_pp2_b_1):
                    if myu[j]<=my_pp2_b<myu[j+1]:
                        debi=j                 
                debj=debi-myk
                x,y=deboor(myu,mypoint,my_pp2_b,myk,debj,debi,myk)
                x2,y2=deboor(myu,mypoint,my_pp2_b2,myk,debj,debi,myk)
                GL.glBegin(GL.GL_LINES)
                GL.glVertex2d(x,y)
                GL.glVertex2d(x2,y2)
                GL.glEnd()
                my_pp2_b=my_pp2_b2
                
        if mytype==2:                                #准均匀B样条画线
            my_pp2_c=0                               #起始节点
            my_pp2_c_1=myn+myk                       #节点个数
            my_pp2_c_2=0.01                          #节点步长   
            for i in range(100):                     #每步处理                
                my_pp2_c2=my_pp2_c+my_pp2_c_2
                debi=0
                debj=0
                for j in range(my_pp2_c_1):
                    if myu[j]<=my_pp2_c<myu[j+1]:
                        debi=j                 
                debj=debi-myk
                x,y=deboor(myu,mypoint,my_pp2_c,myk,debj,debi,myk)
                x2,y2=deboor(myu,mypoint,my_pp2_c2,myk,debj,debi,myk)
                GL.glBegin(GL.GL_LINES)
                GL.glVertex2d(x,y)
                GL.glVertex2d(x2,y2)
                GL.glEnd()
                my_pp2_c=my_pp2_c2
     
    def myline1(self):                               #画方框
        GL.glColor3f(0.0, 1.0, 0.0)
        GL.glBegin(GL.GL_LINES)
        GL.glVertex2d(0, 0)
        GL.glVertex2d(520,0)
        GL.glVertex2d(0, 0)
        GL.glVertex2d(0,260)
        GL.glVertex2d(520,260)
        GL.glVertex2d(520,0)
        GL.glVertex2d(520,260)
        GL.glVertex2d( 0,260)
        GL.glVertex2d(520,130)
        GL.glVertex2d(0,130)
        GL.glVertex2d(260,0)
        GL.glVertex2d(260,260)
        GL.glVertex2d(130,0)
        GL.glVertex2d(130,260)
        GL.glVertex2d(390,0)
        GL.glVertex2d(390,260)
        GL.glEnd()

    def resizeGL(self,w,h):
        GL.glViewport(0, 0, w, h)
        
    def initializeGL(self):
        GL.glClearColor(1.0, 0.0, 1.0, 0.0)
        GL.glClearDepth(1.0)

class OpenglWidget_2(QGLWidget):
    def __init__(self):
        super().__init__()
#            self.resize(300, 300)
        
    def paintGL(self):
        GL.glClearColor(1.0, 1.0, 1.0, 0.0)             #白颜色
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)       
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(-20.0, 530.0, -50.0, 600.0)      #左下角右上角x左下角右上角y
        
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        self.myline1()                                  #画方框        
        if myfinish:
            self.mypb()                                 #画线
        
    def myline1(self):                                  #画方框
        GL.glColor3f(0.0, 1.0, 0.0)
        GL.glBegin(GL.GL_LINES)
        GL.glVertex2d(0, 0)
        GL.glVertex2d(520,0)
        GL.glVertex2d(0, 0)
        GL.glVertex2d(0,550)
        GL.glVertex2d(520,550)
        GL.glVertex2d(520,0)
        GL.glVertex2d(520,550)
        GL.glVertex2d( 0,550)
        '''
        GL.glVertex2d(260,0)
        GL.glVertex2d(260,550)
        GL.glVertex2d(130,0)
        GL.glVertex2d(130,550)        
        GL.glVertex2d(390,0)
        GL.glVertex2d(390,550)
        GL.glVertex2d(0,0)
        GL.glVertex2d(130,550)
        '''
        GL.glEnd()
    def mypb(self):
        GL.glColor3f(1.0, 0.6, 0.0)
        if mytype==0 or mytype==2 or mytype==1:                                #均匀准均匀B样条画线                      
            for mypb_i in range(myn):                     #每步处理
                mypb_start=myu[mypb_i]#起始位置
                mypb_a=mypb_start#小线段的第一个点   
                y=Basis(myu,mypb_a,mypb_i,myk)
                mypb_step=(myu[mypb_i+myk+1]-myu[mypb_i])/100
                for j in range(100):
                    mypb_a2=mypb_a+mypb_step
                    y2=Basis(myu,mypb_a2,mypb_i,myk)
                    GL.glBegin(GL.GL_LINES)
                    GL.glVertex2d(mypb_a*520,y*550)
                    GL.glVertex2d(mypb_a2*520,y2*550)
                    GL.glEnd()
                    mypb_a=mypb_a2
                    y=y2

    def resizeGL(self,w,h):
        GL.glViewport(0, 0, w, h)
        
    def initializeGL(self):
        GL.glClearColor(1.0, 0.0, 1.0, 0.0)
        GL.glClearDepth(1.0)
       

class mywindow(QWidget,Ui_cagd_0):  
    def __init__(self):  
        super().__init__()
        self.setupUi(self)
        self.myow1=OpenglWidget_1()
        self.myvbox1=QVBoxLayout()
        self.myvbox1.addWidget(self.myow1)
        self.verticalLayout_4.addLayout(self.myvbox1)
        self.myow2=OpenglWidget_2()
        self.myvbox2=QVBoxLayout()
        self.myvbox2.addWidget(self.myow2)
        self.verticalLayout_5.addLayout(self.myvbox2)
                
        self.pushButton_start.clicked.connect(self.ButtonPoint)
        self.pushButton_finish.clicked.connect(self.ButtonLine)
        self.spinBox_k.valueChanged.connect(self.B_Degree)
        self.comboBox_type.currentIndexChanged.connect(self.B_Type)
        self.pushButton_adjust.clicked.connect(self.B_Adjust)
        
    def ButtonPoint(self):                      #选点预处理
        global mystart,myfinish,myn,mypoint,myu
        myfinish=0
        mystart=1
        mypoint=[[0],[0]]
        myn=0
        myu=[]
        self.myow1.update()
        self.myow2.update()
    def ButtonLine(self):                       #画线预处理
        global mystart,myfinish,myu
        mystart=0
        myfinish=1
        if mytype==0 :                          #均匀B样条
            myu=[]           
            mytp=myk+myn                        #节点段数
            for i in range(mytp+1):
                myu.append(i/mytp)

        if mytype==1:                           #分段Bezier
            if myn:
                if (myn-1)%myk:
                    mystart=1
                    myfinish=0
                    mywarning=QMessageBox.warning(self,"警告",\
                    "输入点出错：\n如果有n+1个点，n应是次数k的整数倍。\n请继续选点。")
##                    if mywarning==QMessageBox.Ok:
##                    mystart=1
##                    myfinish=0
                    

                    
                else:                
                    myu=[0]*(myk+1)
                    mytp_1=(myn-1)//myk             #节点段数   
                    for i in range(1,mytp_1):
                        myu.extend([i/mytp_1]*myk)
                    myu.extend([1]*(myk+1))
                
        if mytype==2 :                          #准均匀B样条
            myu=[]           
            mytp=myn-myk                        #节点段数
            myu.extend([0]*(myk))
            for i in range(mytp+1):
                myu.append(i/mytp)
            myu.extend([1]*myk)
        

            
        self.myow1.update()
        self.myow2.update()
        
    def B_Degree(self):                                       #设置次数
        global myk
        myk=self.spinBox_k.value()
        self.ButtonLine()
        '''
        global mystart,myfinish,myn,mypoint
        myfinish=0
        mystart=0
        mypoint=[[0],[0]]
        myn=0
        self.myow1.update()
        '''
    def B_Type(self):                                         #设置曲线类型
        global mytype
        mytype=(self.comboBox_type.currentIndex())
        self.ButtonLine()
    def B_Adjust(self):
        global myadjust
        myadjust=(not myadjust)
        
    def mousePressEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton:
            
            if mystart:
##                opengl左下角是0,0这和显示界面是不同的
##                所以要用以下公式计算坐标
##                其中10,340是由界面位置决定的
##                1.8，20是由opengl中定义坐标系决定的
                my_mouse_x=((event.pos().x()-20))
                my_mouse_y =340-(event.pos().y())
                if -20<my_mouse_x<520 and -20<my_mouse_y<280:
                    mypoint[0].append(my_mouse_x)
                    mypoint[1].append(my_mouse_y)
                    global myn                    
                    myn=myn+1
                    self.myow1.update()
        if myadjust:
            global my_mouse_move_i
            my_mouse_x=((event.pos().x()-20))
            my_mouse_y =340-(event.pos().y())
            if -20<my_mouse_x<520 and -20<my_mouse_y<280:
                for i in range(1,myn+1):
                    if -10<(my_mouse_x-mypoint[0][i])<10 and -10<(my_mouse_y-mypoint[1][i])<10:
                        my_mouse_move_i=i
                        
    def mouseMoveEvent(self,event):
        global mypoint
        if myfinish:
            mypoint[0][my_mouse_move_i]=((event.pos().x()-20))
            mypoint[1][my_mouse_move_i]=340-(event.pos().y())
            self.myow1.update()
    def mouseReleaseEvent(self,event):
        global my_mouse_move_i 
        my_mouse_move_i=0
        
if __name__=="__main__":  
    app=QApplication(sys.argv)  
    myshow=mywindow()  
    myshow.show()  
    sys.exit(app.exec_())  
