# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listView.setFont(font)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionciao = QtWidgets.QAction(MainWindow)
        self.actionciao.setObjectName("actionciao")
        self.actionciccio = QtWidgets.QAction(MainWindow)
        self.actionciccio.setObjectName("actionciccio")
        self.actionpupu = QtWidgets.QAction(MainWindow)
        self.actionpupu.setObjectName("actionpupu")
        self.actionpapa = QtWidgets.QAction(MainWindow)
        self.actionpapa.setObjectName("actionpapa")
        self.actionpopo = QtWidgets.QAction(MainWindow)
        self.actionpopo.setObjectName("actionpopo")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionciao.setText(_translate("MainWindow", "ciao"))
        self.actionciccio.setText(_translate("MainWindow", "ciccio"))
        self.actionpupu.setText(_translate("MainWindow", "pupu"))
        self.actionpapa.setText(_translate("MainWindow", "papa"))
        self.actionpopo.setText(_translate("MainWindow", "popo"))
