import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
import qdarkstyle

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Fractal Tree")
        self.setWindowIcon(QtGui.QIcon('fractal2.png'))
        self.home()

    def home(self):

        label = QtGui.QLabel("\t\tIn Honour of one of the first researchers on fractals:\n\t          Gaston Julia (on the eve of the anniversary of his passing)\n\t           This serves to educate about the beauty of fractal trees.\nIf you liked this little reminder, enter a close friend's email to continue this recursive process!", self)
        label.move(30,20)
        label.setFixedWidth(440)
        label.setFixedHeight(60)
        
        btn = QtGui.QPushButton("Send", self)
        btn.move(75,140)
        btn.resize(350,30)
        
        textbox = QLineEdit(self)
        textbox.move(75,100)
        textbox.resize(350,30)
        textbox.setPlaceholderText("Email Address")
        
        def onClick(self):
            txt = textbox.text()
            print txt
        btn.clicked.connect(onClick)
        self.show()

def run():        
    app = QtGui.QApplication(sys.argv)
    #style_string = pyqtcss.get_style("dark_blue")
    #app.setStyleSheet(style_string)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    GUI = Window()
    sys.exit(app.exec_())

run()
