from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from FileButton import FileButton

from Folder import FolderWidget


class ScrollCharacters(QLabel):
    def __init__(self, parent=None):
        super(ScrollCharacters, self).__init__(parent)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("Double Click")
        return super().mouseDoubleClickEvent(a0)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet("background: #ffffff; margin: 0;" +
                           "border : solid #ffffff; border-width : 1px;"+"border-radius: 4px;padding: 5px;background-color: #ffffff;color: #f56038; font-weight: bold; ")
        if (self.parent()) != None:
            folder = (self.parent().parent())
            for each in folder.children():
                if isinstance(each, FolderWidget) and each.directory[0].upper() == self.text().strip():
                    for button in (each.children()):
                        if isinstance(button, FileButton):
                            button.setStyleSheet("background: "+each.textColor+";margin: 0;" +
                                                 "border : solid "+each.textColor +
                                                 "; border-width : 1px;"+"border-radius: 4px;padding: 15px;background-color: "
                                                 + each.textColor+";color: "+each.backgdColor+"; font-weight: bold; ")
        return super().enterEvent(a0)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet("background: #f56038; margin: 0;" +
                           "border : solid #f56038; border-width : 1px;"+"border-radius: 4px;padding: 5px;background-color: #f56038;color: #ffffff; font-weight: bold; ")

        if (self.parent()) != None:
            folder = (self.parent().parent())
            for each in folder.children():
                if isinstance(each, FolderWidget) and each.directory[0].upper() == self.text().strip():
                    for button in (each.children()):
                        if isinstance(button, FileButton):
                            button.setStyleSheet("background: "+each.backgdColor+";margin: 0;" +
                                                 "border : solid "+each.backgdColor +
                                                 "; border-width : 1px;"+"border-radius: 4px;padding: 15px;background-color: "
                                                 + each.backgdColor+";color: "+each.textColor+"; font-weight: bold; ")
        return super().leaveEvent(a0)
