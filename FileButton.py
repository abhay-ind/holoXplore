from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore


class FileButton(QPushButton):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        parentFolderWidget = (self.parent())
        self.setStyleSheet("background: "+parentFolderWidget.textColor+";" +
                           "border : solid "+parentFolderWidget.backgdColor +
                           "; border-width : 1px;" +
                           "margin: 0;border-radius: 4px;padding: 15px;background-color: " +
                           parentFolderWidget.textColor+";color: "+parentFolderWidget.backgdColor+"; font-weight: bold; ")
        return super().enterEvent(a0)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        parentFolderWidget = (self.parent())
        self.setStyleSheet("background: "+parentFolderWidget.backgdColor+";margin: 0;" +
                           "border : solid "+parentFolderWidget.backgdColor +
                           "; border-width : 1px;"+"border-radius: 4px;padding: 15px;background-color: " +
                           parentFolderWidget.backgdColor+";color: "+parentFolderWidget.textColor+"; font-weight: bold; ")
        return super().leaveEvent(a0)
