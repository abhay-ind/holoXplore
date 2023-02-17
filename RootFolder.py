import imp
from random import randint
import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from FileButton import FileButton
from Folder import FolderWidget
from ScrollBar import ScrollBar
from ScrollCharacters import ScrollCharacters

import string
from ctypes import windll

colorDictionary = {0: "#309975", 1: "#58b368"}
colorBack = {0: "#dad873", 1: "#efeeb4"}
colorText = {0: "#ffffff", 1: "#ffffff"}


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter+":\\")
        bitmask >>= 1

    return drives


def getDirectoryDetails(dir_path1):
    import os

    dir_path = dir_path1
    # folder path
    # list to store files
    res = []
    files = []
    dirs = []
    # Iterate directory
    try:
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                files.append(path)
            else:
                dirs.append(path)
    except:
        print("restricted access")
    res.extend(dirs)
    res.extend(files)
    return dir_path, res


def dictionary(level, maxfiles):
    dict = {}
    initial_seed = randint(0, maxfiles)
    for i in range(0, initial_seed):
        randomKey = ''.join(random.choices(string.ascii_letters +
                                           string.digits, k=randint(3, 20)))
        fileOrFolder = randint(0, 1)
        if level == 7 or fileOrFolder == 0:
            dict[randomKey] = randomKey
        else:
            dict[randomKey] = dictionary(level+1, maxfiles)

    return dict


class Example(QWidget):
    def __init__(self, path, directory):
        super().__init__()
        self.setWindowTitle("Test")
        self.path = path
        self.directory = directory
        pwd = self.directory
        self.vlayout = QVBoxLayout()
        widgetList = []
        count = 0

        for key in pwd:
            if count % 4 == 0:
                if count != 0:
                    self.vlayout.addLayout(self.hlayout)
                self.hlayout = QHBoxLayout()
                self.hlayout.setSpacing(0)

            cLayout = QVBoxLayout()
            cLayout.addStretch()
            button = FileButton(" "+pwd[count]+" ")
            button.clicked.connect(self.popupnew)
            cLayout.addWidget(button)
            isFolder = os.path.isdir(os.path.join(self.path, key))
            if isFolder == False:
                color = "#f56038"
            else:
                color = colorDictionary[0]
            cWidget = FolderWidget(
                self.path, key, 0, colorBack[0], color, colorText[0])
            button.setStyleSheet("background: "+color+";margin: 0;" +
                                 "border : solid "+color+"; border-width : 1px;"+"border-radius: 4px;padding: 15px;background-color: " +
                                 color+";color: "+colorText[0]+"; font-weight: bold; ")
            cLayout.setSpacing(0)
            cWidget.setLayout(cLayout)
            self.hlayout.addWidget(cWidget)
            widgetList.append(cWidget)
            count += 1
        if (count == 0):
            return
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addStretch()
        self.setLayout(self.vlayout)

        # self.lineEntry.textChanged.connect(self.onChanged)

    def popupnew(self):
        parentWidget = self.sender().parent()
        level = parentWidget.level
        next = parentWidget.directory
        basePath = parentWidget.basePath
        if parentWidget.opened == True:
            for child in parentWidget.children():
                if isinstance(child, FolderWidget) or isinstance(child, ScrollBar):
                    child.setParent(None)
            parentWidget.opened = False
            return
        parentWidget.opened = True

        fullFilePath = os.path.join(basePath, next)
        if os.path.isfile(fullFilePath):
            os.startfile(fullFilePath)
            return
        if os.path.isdir(fullFilePath):
            for child in self.sender().parent().children():

                if isinstance(child, QVBoxLayout):
                    count = 0
                    currentDirectoryPath, files = getDirectoryDetails(
                        os.path.join(basePath, next))
                    fileAndScroll = QHBoxLayout()
                    fileLayout = QVBoxLayout()
                    if isinstance(parentWidget, FolderWidget):
                        parentWidget.files = files
                    initialsSet = []
                    for key in files:
                        initial = key[0].upper()
                        if initial not in initialsSet:
                            initialsSet.append(initial)
                        if count % 4 == 0:
                            if (count != 0) and hlayout is not None:
                                fileLayout.addLayout(hlayout)
                            hlayout = QHBoxLayout()
                            hlayout.setSpacing(0)

                        scroller = None
                        isFolder = os.path.isdir(
                            os.path.join(currentDirectoryPath, key))

                        cLayout = QVBoxLayout()
                        button = FileButton(" "+key+" ")
                        button.clicked.connect(self.popupnew)
                        cLayout.addWidget(button)
                        color = None
                        if isFolder == False:
                            color = "#f56038"
                        else:
                            color = colorDictionary[(level+1) % 2]
                        cWidget = FolderWidget(currentDirectoryPath, key, self.sender(
                        ).parent().level+1, colorBack[(level+1) % 2], color, colorText[(level+1) % 2])
                        button.setStyleSheet("background: "+color+";margin: 0;" +
                                             "border : solid "+color+"; border-width : 1px;" +
                                             "border-radius: 4px;padding: 15px;background-color: " +
                                             color+";color: "+colorText[(level+1) % 2]+"; font-weight: bold; ")
                        cLayout.setSpacing(0)

                        cWidget.setLayout(cLayout)
                        hlayout.addWidget(cWidget)
                        count += 1
                    if (count == 0):
                        return
                    fileLayout.addLayout(hlayout)
                    scrollerWidget = ScrollBar()
                    scroller = QVBoxLayout()
                    for character in initialsSet:
                        letter = ScrollCharacters()
                        letter.setText(character)
                        letter.setStyleSheet("background: #f56038; margin: 0;" +
                           "border : solid #f56038; border-width : 1px;"+"border-radius: 4px;padding: 5px;background-color: #f56038;color: #ffffff; font-weight: bold; ")

                        scroller.addWidget(letter)
                    fileAndScroll.addLayout(fileLayout)
                    scrollerWidget.setLayout(scroller)
                    scrollerWidget.show()
                    fileAndScroll.addWidget(scrollerWidget)
                    child.addLayout(fileAndScroll)

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()

    def displayImage(self):
        self.im = QPixmap("./image.jpg")
        self.label = QLabel()
        self.label.setPixmap(self.im)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)
