import sys,os
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui
from leavingFenetre import *
import subprocess
from PyQt5.QtCore import QSize, QDir, QUrl, QPoint, QRect, Qt
from PyQt5.QtGui import QMovie, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
class mgGIF(QWidget):
    def __init__(self, px, py, h, w, parent=None):
        super(mgGIF, self).__init__(parent)
        self.resize(QSize(h, w))
        self.move(py, px)

        movie = QMovie("C:/Users/Ahmed/Desktop/snakee/img/pyth.png")
        movie.start()
        self.labelImage = QLabel(self)
        self.labelImage.setMovie(movie)
        self.labelImage.setScaledContents(True)

class mgGUIDE(QWidget):
    def __init__(self, px, py, h, w, parent=None):
        super(mgGUIDE, self).__init__(parent)
        self.resize(QSize(h, w))
        self.move(py, px)

        movie = QMovie("C:/Users/Ahmed/Desktop/snakee/img/dead.gif")
        movie.start()
        self.labelImage = QLabel(self)
        self.labelImage.setMovie(movie)
        self.labelImage.setScaledContents(True)

class mgMODE(QWidget):
    def __init__(self, px, py, h, w, parent=None):
        super(mgMODE, self).__init__(parent)
        self.resize(QSize(h, w))
        self.move(py, px)

        movie = QMovie("C:/Users/Ahmed/Desktop/snakee/img/sg2.png")
        movie.start()
        self.labelImage = QLabel(self)
        self.labelImage.setMovie(movie)
        self.labelImage.setScaledContents(True)



class mnButtons(QWidget):

    def __init__(self, parent=None):
        font = QFont()
        font.setBold(True)
        font.setFamily("TheSansCorrespondence")
        font.setPointSize(18)


        self.www = QWidget()
        super(mnButtons, self).__init__(parent)

        self.resize(QSize(2000, 1800))
        self.selector = QLabel(self)
        self.selector.resize(1360, 420)
        self.selector.move(300, 580)
        self.selector.setStyleSheet("background-color: #91a196; color: red; border: 4px dashed white; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; border-top: 0px;")

        self.titlechoix = QLabel("CHOIX DE MODE JEU", self)
        self.titlechoix.setAlignment(Qt.AlignCenter)
        self.titlechoix.resize(1360, 180)
        self.titlechoix.move(300, 500)
        self.titlechoix.setStyleSheet("background-color: #FA3681; color: black; border: 4px dashed white; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        self.titlechoix.setFont(font)

        font.setPointSize(20)

        self.players2 = QPushButton('2-PLAYERS', self)
        self.players2.resize(490, 80)
        self.players2.move(320, 740)
        self.players2.setStyleSheet("background-color: #ffdf7c; color: black; border-top-left-radius: 20px; ")
        self.players2.setFont(font)

        self.players1 = QPushButton('1-PLAYER', self)
        self.players1.resize(490, 80)
        self.players1.move(1150,740)
        self.players1.setStyleSheet("background-color: #8fe9df; color: black; border-top-right-radius: 20px;")
        self.players1.setFont(font)

        self.playersai = QPushButton('AI-PLAYER', self)
        self.playersai.resize(1320, 120)
        self.playersai.move(320, 850)
        self.playersai.setStyleSheet("background-color: #45FA1B; color: black; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px;")
        self.playersai.setFont(font)





class fenetreMG(QMainWindow):
    def __init__(self, parent=None):
        super(fenetreMG, self).__init__(parent)
        self.resize(2000, 1800)

        self.startUIWindow()

        self.filename = "C:/Users/Ahmed/Desktop/snakee/soz.mp3"
        self.fullpath = QDir.current().absoluteFilePath(self.filename)
        self.media = QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()


    def startUIWindow(self):
        self.Fenetre = mgGIF(-20, 755, 1000, 1000, self)
        self.Window = mnButtons(self)
        self.Fenetre = mgGUIDE(1077, 1600, 2200, 1000, self)
        self.Fenetre = mgMODE(1240, 155, 1900, 1900, self)
        self.setWindowTitle("Snake Menu")
        self.setStyleSheet("background-color: black")

        self.show()

        self.Window.playersai.clicked.connect(self.decr3)

        self.Window.players1.clicked.connect(self.decr1)
        self.Window.players2.clicked.connect(self.decr2)

    def decr1(self):

        sleep = subprocess.Popen(['python', 'allcode.py','1'])
        self.hide()
    def decr2(self):

        sleep = subprocess.Popen(['python', 'allcode.py','2'])
        self.hide()

    def decr3(self):

        sleep = subprocess.Popen(['python', 'allcode.py', '3'])
        self.hide()
    def closeEvent(self, event):
        self.closet = leavingFN(self)
        event.ignore()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = fenetreMG()
    sys.exit(app.exec_())