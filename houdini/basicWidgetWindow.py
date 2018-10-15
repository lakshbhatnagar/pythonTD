from hutil.Qt import QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.title = "MyFirstWindow"
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200   
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QtWidgets.QPushButton("Hello", self)
        button.move(100,70) 
        button.clicked.connect(self.on_click)
        self.show()
        
    def on_click(self):
        print('PyQt5 button click')
        import hou
        hou.node("/obj").createNode("geo")
        

window = MainWindow()
