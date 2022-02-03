from menuGeneral import *
from PyQt5.QtCore import QSize, QDir, QUrl
from PyQt5.QtGui import QMovie, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel



class monGIF(QWidget):
    def __init__(self, px, py, h, w, parent=None):
        super(monGIF, self).__init__(parent)

        self.resize(QSize(h, w))
        self.move(py, px)

        self.movie = QMovie("C:/Users/Ahmed/Desktop/snakee/img/loa3.gif")
        self.movie.setScaledSize(QSize(self.height(), self.width()))
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()


    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        self.frameRect = currentFrame.rect()

        self.frameRect.moveCenter(self.rect().center())
        if self.frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(self.frameRect.left(), self.frameRect.top(), currentFrame)


class UIWindow(QWidget):
    def __init__(self, parent=None):
        font = QFont()
        font.setBold(True)
        font.setFamily("TheSans")
        font.setPointSize(60)

        super(UIWindow, self).__init__(parent)

        self.resize(QSize(1970, 1970))
        self.dc = 15
        self.decompteur = QPushButton("15", self)
        self.decompteur.resize(300, 120)
        self.decompteur.move(600,1440)
        self.decompteur.setStyleSheet("background-color: white; color: black; ")

        self.labelImage = QLabel(self)
        pixmap = QPixmap("C:/Users/Ahmed/Desktop/snakee/img/logosnake.png")
        self.labelImage.setPixmap(pixmap)

        self.labelImage.setGeometry(450,450, 1100, 1160)
        self.labelImage.setScaledContents(True)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.resize(2000, 1800)
        self.startUIWindow()

        self.filename = "C:/Users/Ahmed/Desktop/snakee/test.mp3"


        self.fullpath = QDir.current().absoluteFilePath(self.filename)
        self.media = QUrl.fromLocalFile(self.fullpath)
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.play()



    def startUIWindow(self):
        monGIF(-60, 750, 510, 600, self)
        self.Window = UIWindow(self)


        self.setWindowTitle("Snake Game")
        self.setStyleSheet("background-color: black")

        QtCore.QTimer.singleShot(1000, self.decompter)
        QtCore.QTimer.singleShot(2000, self.decompter)
        QtCore.QTimer.singleShot(3000, self.decompter)
        QtCore.QTimer.singleShot(4000, self.decompter)
        QtCore.QTimer.singleShot(5000, self.decompter)
        QtCore.QTimer.singleShot(6000, self.decompter)
        QtCore.QTimer.singleShot(7000, self.decompter)
        QtCore.QTimer.singleShot(8000, self.decompter)
        QtCore.QTimer.singleShot(9000, self.decompter)
        QtCore.QTimer.singleShot(10000, self.decompter)
        #QtCore.QTimer.singleShot(11000, self.decompter)
        #QtCore.QTimer.singleShot(12000, self.decompter)
        #QtCore.QTimer.singleShot(13000, self.decompter)
        #QtCore.QTimer.singleShot(14000, self.decompter)
        #QtCore.QTimer.singleShot(15000, self.decompter)

        QtCore.QTimer.singleShot(11000, self.openMG)

        self.show()

    def openMG(self):
        self.close()
        self.newf = fenetreMG()

    def decompter(self):
        self.Window.dc -= 1
        self.Window.decompteur.setText("{0}".format(self.Window.dc))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())