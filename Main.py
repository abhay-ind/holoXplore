import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ErrorMessagePane import ErrorMessagePane
from RootFolder import Example, get_drives


class MapWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MapWindow, self).__init__(parent)
        self.scrollArea = QScrollArea()
        drives = get_drives()
        self.folderWidget = Example("", drives)
        self._scene = QtWidgets.QGraphicsScene(self)
        self._view = QtWidgets.QGraphicsView(self._scene)
        self._view.setTransformationAnchor(
            QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self._view.setDragMode(QtWidgets.QGraphicsView.DragMode.ScrollHandDrag)
        self._scene.addWidget(self.folderWidget)
        self.setCentralWidget(self._view)
        self.setMinimumSize(700,500)

        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key.Key_Plus),
            self._view,
            context=QtCore.Qt.WidgetShortcut,
            activated=self.zoom_in,
        )

        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.Key.Key_Minus),
            self._view,
            context=QtCore.Qt.WidgetShortcut,
            activated=self.zoom_out,
        )

    @QtCore.pyqtSlot()
    def zoom_in(self):
        scale_tr = QtGui.QTransform()
        scale_tr.scale(1.25, 1.25)

        tr = self._view.transform() * scale_tr
        self._view.setTransform(tr)

    @QtCore.pyqtSlot()
    def zoom_out(self):
        scale_tr = QtGui.QTransform()
        scale_tr.scale(1.25, 1.25)

        scale_inverted, invertible = scale_tr.inverted()

        if invertible:
            tr = self._view.transform() * scale_inverted
            self._view.setTransform(tr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapWindow()
    ex.show()
    sys.exit(app.exec_())
