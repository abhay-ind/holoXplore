from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ScrollBar import ScrollBar


class FolderWidget(QWidget):
    def __init__(self, basePath, directory, level, color, backgdcolor, textColor):
        super().__init__()
        self.basePath = basePath
        self.directory = directory
        self.level = level
        self.opened = False
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        self.files = []
        self.backgdColor = backgdcolor
        self.textColor = textColor

    # def enterEvent(self, a0: QtCore.QEvent) -> None:
    #     initialSet = []
    #     for each in self.files:
    #         initial = each[0].upper()
    #         if initial not in initialSet:
    #             initialSet.append(initial)
    #     if self.opened == True:
    #         for child1 in (self.children()):
    #             if isinstance(child1, ScrollBar):
    #                 child1.setWindowOpacity(1)
    #     return super().enterEvent(a0)

    # def leaveEvent(self, a0: QtCore.QEvent) -> None:
    #     if self.opened == True:
    #         for child1 in (self.children()):
    #             if isinstance(child1, ScrollBar):
    #                 child1.setWindowOpacity(0)
    #     return super().leaveEvent(a0)
