import sys
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui

from PyQt5.QtCore import QSize, QDir, QUrl, QPoint, QRect, Qt
from PyQt5.QtGui import QMovie, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from menuGeneral import *
class mgGIF(QWidget):
    def __init__(self, px, py, h, w, parent=None):
        super(mgGIF, self).__init__(parent)
        self.resize(QSize(h, w))
        self.move(py, px)

        movie = QMovie("C:/Users/Ahmed/Desktop/snakee/img/manette1.png")
        movie.start()
        self.labelImage = QLabel(self)
        self.labelImage.setMovie(movie)
        self.labelImage.setScaledContents(True)


class mnButtons(QWidget):

    def __init__(self, score, parent=None):
        font = QFont()
        font.setBold(True)
        font.setFamily("TheSansCorrespondence")
        font.setPointSize(18)


        self.www = fenetreMG()
        super(mnButtons, self).__init__(parent)

        self.resize(QSize(1350, 1350))
        self.selector = QLabel(self)
        self.selector.resize(870, 480)
        self.selector.move(300, 720)
        self.selector.setStyleSheet("background-color: #91a196; color: red; border: 4px dashed white; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; border-top: 0px;")

        self.titlechoix = QLabel("YOUR SCORE : "+score, self)
        self.titlechoix.setAlignment(Qt.AlignCenter)
        self.titlechoix.resize(870, 120)
        self.titlechoix.move(300, 600)
        self.titlechoix.setStyleSheet("background-color: white; color: black; border: 4px dashed white; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        self.titlechoix.setFont(font)

        font.setPointSize(15)

        self.players2 = QPushButton('GAME OVER !', self)
        self.players2.resize(810, 120)
        self.players2.move(330, 810)
        self.players2.setStyleSheet("background-color: #ffdf7c; color: black; border-top-left-radius: 20px;  border-top-right-radius: 20px; ")
        self.players2.setFont(font)

        self.playersai = QPushButton('Menu', self)
        self.playersai.resize(390, 120)
        self.playersai.move(330, 960)
        self.playersai.setStyleSheet("background-color: #bfff7f; color: black; border-bottom-left-radius: 20px;")
        self.playersai.setFont(font)

        self.training = QPushButton('Exit', self)
        self.training.resize(390, 120)
        self.training.move(750, 960)
        self.training.setStyleSheet("background-color: #edc596; color: black; border-bottom-right-radius: 20px;")
        self.training.setFont(font)



class scoreFenetre(QMainWindow):
    def __init__(self, score, parent=None):
        super(scoreFenetre, self).__init__(parent)
        self.resize(1500, 1500)

        self.startUIWindow(score)

        self.filename = "C:/Users/Ahmed/Desktop/snakee/soz.mp3"
        self.fullpath = QDir.current().absoluteFilePath(self.filename)
        self.media = QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()


    def startUIWindow(self, score):
        self.Fenetre = mgGIF(50, 400, 900, 1500, self)
        self.Window = mnButtons(score, self)


        self.setWindowTitle("Mon Snake")
        self.setStyleSheet("background-color: #005FFD")


        self.show()

        self.Window.playersai.clicked.connect(self.decr)
        self.Window.training.clicked.connect(self.close)



    def decr(self):

        self.hide()
        self.Window.www.show()
    def closeEvent(self, event):
        self.closet = leavingFN(self)
        event.ignore()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = scoreFenetre("45")
    sys.exit(app.exec_())