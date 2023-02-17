from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ScrollBar(QWidget):
    def __init__(self, parent=None):
        super(ScrollBar, self).__init__(parent)

    def startFadeIn(self):
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.animation = QPropertyAnimation(effect, b"opacity")
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setDuration(500)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animation)
        self.anim_group.start()

    def startFadeOut(self):
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.animation = QPropertyAnimation(effect, b"opacity")
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.setDuration(500)
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animation)
        self.anim_group.start()

    def startAnimation(self):
        self.startFadeIn()
        loop = QEventLoop()
        self.animation.finished.connect(loop.quit)
        loop.exec_()
        QTimer.singleShot(2000, self.startFadeOut)
