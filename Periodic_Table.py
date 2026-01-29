
'''I still have to add colors to P-Block'''

'''Double tap the top to resize the window to fullscreen if the wiindow does not fit in teh screen during run-time'''

'''The moment the table is created(genTable), teh random tile is already created but it is not added until teh table gets updated'''

import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
import random

FONT=QFont("Helvetica", 14, QFont.Bold)

ELEMENTS= "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba ⤷ La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra ⤷ Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og ".split()
print(len(ELEMENTS))


global counter
counter=0

def reopen(cl:QtWidgets.QWidget):
    cl.close()
    cl.__init__()
    cl.show()
    


app = QtWidgets.QApplication(sys.argv)  # Create the application


class message(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #self.setGeometry(1000,100,200,200)
        l=QtWidgets.QLabel("Double tap the top to resize the window")
        l.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.Layout=QtWidgets.QVBoxLayout()
        self.Layout.addWidget(l)

        b=QtWidgets.QPushButton("OK")
        self.Layout.addWidget(b)
        b.clicked.connect(self.close)
        self.setLayout(self.Layout)



class periodicTable(QtWidgets.QWidget):
    def __init__(self,w=None,h=None):
        super().__init__()
        screen = QtWidgets.QApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        if not w:self.setGeometry(0,0,screen_size.width(), screen_size.height())
        else: self.setGeometry(0,0,w,h)
        self.setWindowTitle("Identify the position of the Element in the Periodic Table")
        print("Window Size:", self.width(), self.height())




        self.elementD={}    #D={"Hydrogen": widgetContainerName}

        self.elementLayout=QtWidgets.QGridLayout()


        self.genTable()  

        QtCore.QTimer.singleShot(5000, self.updateTable)    #Updates teh table after 5000ms(5s)
        
        self.bttnGrp=QtWidgets.QButtonGroup()
        self.bttnGrp.setExclusive(True)
        self.bttnGrp.buttonClicked.connect(self.check)
       


        self.setLayout(self.elementLayout)




    def genRows(self, rows:int, x:int, layout:QtWidgets.QGridLayout, elementList:list=None, color='white', spaceUp:int=0):
        '''Generates Rows'''
        for i in range(rows):
            if elementList: 
                self.widget=rightClickable(elementList[i],self)
                self.elementD[elementList[i]]=self.widget
            else: 
                self.widget=QtWidgets.QPushButton()
            self.widget.setCheckable(True)
            self.widget.setStyleSheet(f"width: 120px; height: 60px; background-color: {color} ;")
            self.widget.setFont(FONT)
            layout.addWidget(self.widget,i+spaceUp,x)



    def genTable(self):
        """Creates 7 periods x 18 Groups  """

        def dBlock(x:int, L:list=None):
            x+=1
            if L: self.genRows(4,x,self.elementLayout,L, spaceUp=3, color='#4682B4')
            else: self.genRows(4,x,self.elementLayout,spaceUp=3)
            
        
        def pBlock(x:int, L:list=None,color='white'):
            x+=11
            if L:self.genRows(6,x,self.elementLayout,L,color=color,spaceUp=1)
            else: self.genRows(6,x,self.elementLayout,spaceUp=1)


        def fBlock(y:int,L:list, color):
            row=y+7
            column=2
            for i in range(15):
                widget=rightClickable(L[i],self) 
                widget.setCheckable(True)
                widget.setStyleSheet(f"width: 120px; height: 60px;  background-color: {color} ;")
                widget.setFont(FONT)
                self.elementLayout.addWidget(widget,row,column+i)
                self.elementD[L[i]]=widget 
                    
                    


        self.genRows(7,0,self.elementLayout, "H Li Na K Rb Cs Fr".split(' '),color='#fa0542')    #G-1
        self.genRows(6,1,self.elementLayout, "Be Mg Ca Sr Ba Ra".split(' '), color='#E78F24',spaceUp=1)    #G-2

        dBlock(1,'Sc Y ⤷ ⤷'.split(' '))   #G-3
        dBlock(2,'Ti Zr Hf Rf'.split(' '))  #G-4
        dBlock(3,'V Nb Ta Db'.split())  #G-5
        dBlock(4,'Cr Mo W Sg'.split())  #G-6
        dBlock(5,'Mn Tc Re Bh'.split())     #G-7
        dBlock(6,'Fe Ru Os Hs'.split())     #G-8    
        dBlock(7,'Co Rh Ir Mt'.split())    #G-9
        dBlock(8,'Ni Pd Pt Ds'.split())    #G-10
        dBlock(9,'Cu Ag Au Rg'.split())    #G-11
        dBlock(10,'Zn Cd Hg Cn'.split())   #G-12

        pBlock(1,'B Al Ga In Tl Nh'.split())    #G-13
        pBlock(2,'C Si Ge Sn Pb Fl'.split())    #G-14
        pBlock(3,'N P As Sb Bi Mc'.split())     #G-15
        pBlock(4,'O S Se Te Po Lv'.split())     #G-16
        pBlock(5,'F Cl Br I At Ts'.split())     #G-17

        self.genRows(7,17,self.elementLayout,'He Ne Ar Kr Xe Rn Og'.split(),color='#f2f20f')    #G-18 Noble gases



        line2 = QtWidgets.QFrame()
        line2.setFrameShape(QtWidgets.QFrame.HLine)
        line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        line2.setStyleSheet("border: 2px solid black;")



        self.elementLayout.addWidget(line2, 7, 2, 1, 15)  # Row 7, from column 2 to 16

        fBlock(1,'La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu'.split(),color='#87c49e')
        fBlock(2,'Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr'.split(),color='#2E8B57')

        self.colorPBlock()


        self.tile=self.genTile()
        self.tile.setFont(FONT)
        self.wToBeClicked=self.elementD[self.tile.text()]
        print(self.wToBeClicked, self.tile.text(), "IS to be clicked")
            



    def colorPBlock(self):
        metalloids="B Si Ge As Sb Te At".split()
        postTransitionMetals="Al Ga In Tl Sn Pb Fl Bi Po".split()
        polyAtomic='C P S Se'.split()
        diAtomic="N O F Cl Br I".split()
        unknown="Nh Mc Lv Ts".split()

        for i in metalloids:
            self.elementD[i].setStyleSheet(f"width: 120px; height: 60px;  background-color: #9370DB ;")

        for i in postTransitionMetals:
            self.elementD[i].setStyleSheet(f"width: 120px; height: 60px;  background-color: #FFB6C1 ;")

        for i in polyAtomic:
            self.elementD[i].setStyleSheet(f"width: 120px; height: 60px;  background-color: #87c49e ;")

        for i in diAtomic:
            self.elementD[i].setStyleSheet(f"width: 120px; height: 60px;  background-color: #87c49e ;")

        for i in unknown:
            self.elementD[i].setStyleSheet(f"width: 120px; height: 60px;  background-color: #D3D3D3;")
        





    def updateTable(self):
            """Updates the table after 5 seconds"""

            try:
                for i in self.findChildren(QtWidgets.QPushButton):
                    i.setText("")
                    self.bttnGrp.addButton(i)                

            except: 
                pass


            v_line = QtWidgets.QFrame()
            v_line.setFrameShape(QtWidgets.QFrame.VLine)  # Vertical line
            v_line.setStyleSheet("border: 2px solid black;")
            self.elementLayout.addWidget(v_line,0,18,10,1)

            self.tileLayout=QtWidgets.QHBoxLayout()
            self.elementLayout.addLayout(self.tileLayout,0,19)
            spacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.tileLayout.addItem(spacer1)
            
            self.tileLayout.addWidget(self.tile)



            def nextClicked(bttn):
                w, h = self.width(), self.height()
                self.close()
                self.__init__(w=w,h=h)
                self.show()

            self.nextBttn=QtWidgets.QPushButton("Next")     #Pass to the next element
            self.nextBttn.clicked.connect(nextClicked)
            self.nextBttn.setFont(QFont("Helvetica", 12))
            self.elementLayout.addWidget(self.nextBttn,7,19)



            


    def genTile(self):
        """Generate a random tile with an Element"""
        a=random.randint(1,118)
        label=QtWidgets.QLabel(ELEMENTS[a-1])
        return label
    


    def check(self,button):
        '''Checks whether teh selected tile is correct'''
        if button is self.wToBeClicked:
            print(f"{button} is clicked")
            global counter
            counter+=1
            w, h = self.width(), self.height()
            self.close()
            self.__init__(w,h)
            self.show()
            
            self.w=congratsWindow()
            self.w.show()
            
           

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

class rightClickable(QtWidgets.QPushButton):
    rightClicked = pyqtSignal()  # Define custom signal
    #p=periodicTable()

    def __init__(self, text, p:periodicTable):
        super().__init__(text)
        self.p=p

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:  # Check if right-clicked
            print("Right-clicked!", self.text())
            self.showContextMenu(event.globalPos())
            self.rightClicked.emit()  # Emit the custom signal

        else:
            super().mousePressEvent(event)  # Maintain normal button behavior

    def showContextMenu(self,position):
        menu = QtWidgets.QMenu(self)
        element = "Not Found"
        menu.setStyleSheet("background-color: White; padding: 10px;")
        for k,v in self.p.elementD.items():
            if id(v)==id(self):
                element = k
                break

        label1 = QtWidgets.QAction(element, self)
        label1.setFont(QFont("Helvetica", 9, QFont.Bold))
        label1.setEnabled(False)  # Disable to make it non-clickable
        
        menu.addAction(label1)
        menu.exec_(position)




#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

        
class congratsWindow(QtWidgets.QWidget):
    def __init__(self):
        '''A window to tell teh user he/she is correct'''
        super().__init__()
        self.setGeometry(1600, 500, 500, 200)
        l=QtWidgets.QLabel(f"{counter} Correct! 👍")
        l.setFont(FONT)
        self.Layout=QtWidgets.QVBoxLayout()
        self.Layout.addWidget(l)
        self.setLayout(self.Layout)


if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)  # Create the application
    window = periodicTable()  # Create the main window instance
    window.show()  # Show the window
    
    me=message()
    me.show()
    sys.exit(app.exec_())  # Start the event loop


   