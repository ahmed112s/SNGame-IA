import sys
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui

from PyQt5.QtCore import QSize, QDir, QUrl, QPoint, QRect, Qt
from PyQt5.QtGui import QMovie, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
class mgGIF(QWidget):
    def __init__(self, px, py, h, w, parent=None):
        super(mgGIF, self).__init__(parent)
        self.resize(QSize(h, w))
        self.move(py, px)

        movie = QMovie("C:/Users/Ahmed/Desktop/snakee/img/200w.webp")
        movie.setScaledSize(QSize(self.height(), self.width()))

        movie.start()
        self.labelImage = QLabel(self)
        self.labelImage.setMovie(movie)
        self.labelImage.setScaledContents(True)



class mnButtons(QWidget):

    def __init__(self, parent=None):
        font = QFont()
        font.setBold(True)
        font.setFamily("TheSansCorrespondence")
        font.setPointSize(15)


        super(mnButtons, self).__init__(parent)

        self.resize(QSize(1100, 1000))
        self.selector = QLabel(self)
        self.selector.resize(780, 130)
        self.selector.move(200, 580)
        self.selector.setStyleSheet("background-color: #2E44F9; color: red; border: 4px dashed white; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; border-top: 0px;")

        self.titlechoix = QLabel("Do you really want to leave?", self)
        self.titlechoix.setAlignment(Qt.AlignCenter)
        self.titlechoix.resize(780, 80)
        self.titlechoix.move(200, 500)
        self.titlechoix.setStyleSheet("background-color: #FA3681; color: black; border: 4px dashed white; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        self.titlechoix.setFont(font)

        font.setPointSize(15)

        self.playersai = QPushButton('Yes :(', self)
        self.playersai.resize(360, 80)
        self.playersai.move(220, 600)
        self.playersai.setStyleSheet("background-color: white; color: black; border-radius: 20px;")
        self.playersai.setFont(font)

        self.training = QPushButton('No :D', self)
        self.training.resize(360, 80)
        self.training.move(600, 600)
        self.training.setStyleSheet("background-color: white; color: black; border-radius: 20px;")
        self.training.setFont(font)



class leavingFN(QMainWindow):
    def __init__(self, parent=None):
        super(leavingFN, self).__init__(parent)
        self.resize(1200, 1200)

        self.startUIWindow()

        self.filename = "C:/Users/Ahmed/Desktop/snakee/soz.mp3"
        self.fullpath = QDir.current().absoluteFilePath(self.filename)
        self.media = QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()


    def startUIWindow(self):
        self.Fenetre = mgGIF(150, 500, 200, 200, self)
        self.Window = mnButtons(self)


        self.setWindowTitle("Snake Exit")
        self.setStyleSheet("background-color: black")

        self.show()

        self.Window.playersai.clicked.connect(self.adios)
        self.Window.training.clicked.connect(self.stay)

    def adios(self):

        exit(0)

    def stay(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = leavingFN()
    sys.exit(app.exec_())