# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAGD_A.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cagd_0(object):
    def setupUi(self, cagd_0):
        cagd_0.setObjectName("cagd_0")
        cagd_0.resize(550, 520)#窗口大小
        self.tabWidget_menu = QtWidgets.QTabWidget(cagd_0)
        self.tabWidget_menu.setGeometry(QtCore.QRect(0, 0, 580, 50))#菜单栏大小
        self.tabWidget_menu.setObjectName("tabWidget_menu")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 33))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.label_k = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_k.setObjectName("label_k")
        self.horizontalLayout_1.addWidget(self.label_k)
        self.spinBox_k = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_k.setMinimum(1)
        self.spinBox_k.setMaximum(10)
        self.spinBox_k.setProperty("value", 3)
        self.spinBox_k.setObjectName("spinBox_k")
        self.horizontalLayout_1.addWidget(self.spinBox_k)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)#弹簧长度
        self.horizontalLayout_1.addItem(spacerItem)
        self.label_type = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_type.setObjectName("label_type")
        self.horizontalLayout_1.addWidget(self.label_type)
        self.comboBox_type = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.horizontalLayout_1.addWidget(self.comboBox_type)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)#弹簧长
        self.horizontalLayout_1.addItem(spacerItem1)
        self.pushButton_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_1.addWidget(self.pushButton_start)
        self.pushButton_finish = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.horizontalLayout_1.addWidget(self.pushButton_finish)
        self.pushButton_adjust = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_adjust.setObjectName("pushButton_adjust")
        self.horizontalLayout_1.addWidget(self.pushButton_adjust)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)#弹簧长
        self.horizontalLayout_1.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_1)
        spacerItem3 = QtWidgets.QSpacerItem(80, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)#弹簧长
        self.horizontalLayout_2.addItem(spacerItem3)
        self.tabWidget_menu.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_menu.addTab(self.tab_2, "")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(cagd_0)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 550, 300))#opengl窗口1大小
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)#opengl窗口与周围的距离
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(cagd_0)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 380, 550, 130))#基函数的窗口大小
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.retranslateUi(cagd_0)
        self.tabWidget_menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cagd_0)

    def retranslateUi(self, cagd_0):
        _translate = QtCore.QCoreApplication.translate
        cagd_0.setWindowTitle(_translate("cagd_0", "CAGD期末作业"))
        self.label_k.setText(_translate("cagd_0", "次数"))
        self.label_type.setText(_translate("cagd_0", "曲线类型"))
        self.comboBox_type.setItemText(0, _translate("cagd_0", "均匀B样条"))
        self.comboBox_type.setItemText(1, _translate("cagd_0", "分段Bezier"))
        self.comboBox_type.setItemText(2, _translate("cagd_0", "准均匀B样条"))
        self.comboBox_type.setItemText(3, _translate("cagd_0", "非均匀B样条"))
        self.pushButton_start.setText(_translate("cagd_0", "开始选点"))
        self.pushButton_finish.setText(_translate("cagd_0", "结束选点"))
        self.pushButton_adjust.setText(_translate("cagd_0", "拖动点调整曲线"))
        self.tabWidget_menu.setTabText(self.tabWidget_menu.indexOf(self.tab), _translate("cagd_0", "曲线"))
        self.tabWidget_menu.setTabText(self.tabWidget_menu.indexOf(self.tab_2), _translate("cagd_0", "曲面"))

