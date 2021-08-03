# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from scripts.system_info import system_info


class Ui_mainwindow(object):
    def __init__(self, path="D:/", choose=[], programers_bar=0):
        self.path = path
        self.choose = choose
        self.programers_bar_value = programers_bar

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(660, 380)
        mainwindow.setMinimumSize(QtCore.QSize(623, 380))
        mainwindow.setMaximumSize(QtCore.QSize(660, 380))
        mainwindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 10, 581, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 571, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 90, 631, 231))
        self.frame_2.setBaseSize(QtCore.QSize(0, 1))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 657, 224))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_37")
        self.gridLayout_2.addWidget(self.checkBox_5, 1, 0, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_16.setObjectName("checkBox_41")
        self.gridLayout_2.addWidget(self.checkBox_16, 3, 3, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_13.setObjectName("checkBox_38")
        self.gridLayout_2.addWidget(self.checkBox_13, 3, 0, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_15.setObjectName("checkBox_39")
        self.gridLayout_2.addWidget(self.checkBox_15, 3, 2, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_14.setObjectName("checkBox_40")
        self.gridLayout_2.addWidget(self.checkBox_14, 3, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_45")
        self.gridLayout_2.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_44")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_43")
        self.gridLayout_2.addWidget(self.checkBox_12, 2, 3, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_46")
        self.gridLayout_2.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_32")
        self.gridLayout_2.addWidget(self.checkBox_8, 1, 3, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_31")
        self.gridLayout_2.addWidget(self.checkBox_7, 1, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 8, 1, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_28.setObjectName("checkBox_58")
        self.gridLayout_2.addWidget(self.checkBox_28, 6, 3, 1, 1)
        self.checkBox_30 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_30.setObjectName("checkBox_60")
        self.gridLayout_2.addWidget(self.checkBox_30, 7, 3, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_24.setObjectName("checkBox_55")
        self.gridLayout_2.addWidget(self.checkBox_24, 5, 3, 1, 1)
        self.checkBox_26 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_26.setObjectName("checkBox_57")
        self.gridLayout_2.addWidget(self.checkBox_26, 6, 1, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_29.setObjectName("checkBox_59")
        self.gridLayout_2.addWidget(self.checkBox_29, 7, 0, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_23.setObjectName("checkBox_56")
        self.gridLayout_2.addWidget(self.checkBox_23, 5, 2, 1, 1)

        if system_info() == "10":
            self.checkBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.checkBox_1.setEnabled(True)
            self.checkBox_1.setObjectName("checkBox_42")
        elif system_info() == "7":
            self.checkBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.checkBox_1.setEnabled(False)
            self.checkBox_1.setObjectName("checkBox_42")

        self.gridLayout_2.addWidget(self.checkBox_1, 0, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 8, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 8, 3, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_33")
        self.gridLayout_2.addWidget(self.checkBox_6, 1, 1, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_36")
        self.gridLayout_2.addWidget(self.checkBox_10, 2, 1, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_17.setObjectName("checkBox_35")
        self.gridLayout_2.addWidget(self.checkBox_17, 4, 0, 1, 1)

        if system_info() == "10":
            self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.checkBox_9.setObjectName("checkBox_34")
            self.checkBox_9.setEnabled(True)
        elif system_info() == "7":
            self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.checkBox_9.setObjectName("checkBox_34")
            self.checkBox_9.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBox_9, 2, 0, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_18.setObjectName("checkBox_51")
        self.gridLayout_2.addWidget(self.checkBox_18, 4, 1, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_21.setObjectName("checkBox_49")
        self.gridLayout_2.addWidget(self.checkBox_21, 5, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_47")
        self.gridLayout_2.addWidget(self.checkBox_11, 2, 2, 1, 1)
        self.checkBox_22 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_22.setObjectName("checkBox_50")
        self.gridLayout_2.addWidget(self.checkBox_22, 5, 1, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_20.setObjectName("checkBox_48")
        self.gridLayout_2.addWidget(self.checkBox_20, 4, 3, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_27.setObjectName("checkBox_54")
        self.gridLayout_2.addWidget(self.checkBox_27, 6, 2, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_25.setObjectName("checkBox_53")
        self.gridLayout_2.addWidget(self.checkBox_25, 6, 0, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_19.setObjectName("checkBox_52")
        self.gridLayout_2.addWidget(self.checkBox_19, 4, 2, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 8, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 60, 571, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar.setEnabled(True)
        self.progressBar.setToolTipDuration(0)
        self.progressBar.setProperty("value", self.programers_bar_value)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        if system_info() == "10":
            self.radioButton_3.toggled['bool'].connect(
                self.checkBox_1.setChecked)
            self.radioButton_3.toggled['bool'].connect(
                self.checkBox_9.setChecked)

        self.radioButton_3.toggled['bool'].connect(self.checkBox_2.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_3.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_4.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_5.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_6.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_7.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_8.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_10.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_11.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_12.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_13.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_14.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_15.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_16.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_17.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_18.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_19.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_20.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_21.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_22.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_23.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_24.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_25.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_26.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_27.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_28.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_29.setChecked)
        self.radioButton_3.toggled['bool'].connect(self.checkBox_30.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_5.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_2.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_3.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_5.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_6.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_12.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_26.setChecked)

        if system_info() == "10":
            self.radioButton_2.toggled['bool'].connect(
                self.checkBox_9.setChecked)

        self.radioButton_2.toggled['bool'].connect(self.checkBox_10.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_16.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_23.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_5.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_12.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_2.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_3.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_8.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_26.setChecked)
        self.radioButton_2.toggled['bool'].connect(self.checkBox_14.setChecked)
        self.radioButton.toggled['bool'].connect(self.checkBox_14.setChecked)

        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        mainwindow.setTabOrder(self.lineEdit, self.pushButton_2)
        mainwindow.setTabOrder(self.pushButton_2, self.pushButton)
        mainwindow.setTabOrder(self.pushButton, self.checkBox_1)
        mainwindow.setTabOrder(self.checkBox_1, self.checkBox_2)
        mainwindow.setTabOrder(self.checkBox_2, self.checkBox_3)
        mainwindow.setTabOrder(self.checkBox_3, self.checkBox_4)
        mainwindow.setTabOrder(self.checkBox_4, self.checkBox_5)
        mainwindow.setTabOrder(self.checkBox_5, self.checkBox_6)
        mainwindow.setTabOrder(self.checkBox_6, self.checkBox_7)
        mainwindow.setTabOrder(self.checkBox_7, self.checkBox_8)
        mainwindow.setTabOrder(self.checkBox_8, self.checkBox_9)
        mainwindow.setTabOrder(self.checkBox_9, self.checkBox_10)
        mainwindow.setTabOrder(self.checkBox_10, self.checkBox_11)
        mainwindow.setTabOrder(self.checkBox_11, self.checkBox_12)
        mainwindow.setTabOrder(self.checkBox_12, self.checkBox_13)
        mainwindow.setTabOrder(self.checkBox_13, self.checkBox_14)
        mainwindow.setTabOrder(self.checkBox_14, self.checkBox_15)
        mainwindow.setTabOrder(self.checkBox_15, self.checkBox_16)
        mainwindow.setTabOrder(self.checkBox_16, self.checkBox_17)
        mainwindow.setTabOrder(self.checkBox_17, self.checkBox_18)
        mainwindow.setTabOrder(self.checkBox_18, self.checkBox_19)
        mainwindow.setTabOrder(self.checkBox_19, self.checkBox_20)
        mainwindow.setTabOrder(self.checkBox_20, self.checkBox_21)
        mainwindow.setTabOrder(self.checkBox_21, self.checkBox_22)
        mainwindow.setTabOrder(self.checkBox_22, self.checkBox_23)
        mainwindow.setTabOrder(self.checkBox_23, self.checkBox_24)
        mainwindow.setTabOrder(self.checkBox_24, self.checkBox_25)
        mainwindow.setTabOrder(self.checkBox_25, self.checkBox_26)
        mainwindow.setTabOrder(self.checkBox_26, self.checkBox_27)
        mainwindow.setTabOrder(self.checkBox_27, self.checkBox_28)
        mainwindow.setTabOrder(self.checkBox_28, self.checkBox_29)
        mainwindow.setTabOrder(self.checkBox_29, self.checkBox_30)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate(
            "mainwindow", "安装文件解压器 v0.1 by:冼叔叔"))
        self.label.setText(_translate("mainwindow", "解压路径："))
        self.lineEdit.setText(_translate("mainwindow", self.path))
        self.pushButton_2.setText(_translate("mainwindow", "浏览..."))
        self.pushButton.setText(_translate("mainwindow", "解压"))
        self.checkBox_5.setText(_translate("mainwindow", "Winrar"))
        self.checkBox_16.setText(_translate("mainwindow", "爱奇艺(推荐)"))
        self.checkBox_13.setText(_translate("mainwindow", "谷歌浏览器"))
        self.checkBox_15.setText(_translate("mainwindow", "腾讯视频"))
        self.checkBox_14.setText(_translate("mainwindow", "2345浏览器(推荐)"))
        self.checkBox_4.setText(_translate("mainwindow", "钉钉"))
        self.checkBox_2.setText(_translate("mainwindow", "QQ"))
        self.checkBox_12.setText(_translate("mainwindow", "WPS(推荐)"))
        self.checkBox_3.setText(_translate("mainwindow", "微信"))
        self.checkBox_8.setText(_translate("mainwindow", "VCRedist"))
        self.checkBox_7.setText(_translate("mainwindow", "百度网盘"))
        self.radioButton_3.setText(_translate("mainwindow", "全选"))
        self.checkBox_28.setText(_translate("mainwindow", "CAD2014"))
        self.checkBox_30.setText(_translate("mainwindow", "天正建筑T20"))
        self.checkBox_24.setText(_translate("mainwindow", "迅雷11"))
        self.checkBox_26.setText(_translate("mainwindow", "2345拼音输入法(推荐)"))
        self.checkBox_29.setText(_translate("mainwindow", "CAD2007"))
        self.checkBox_23.setText(_translate("mainwindow", "酷狗音乐(推荐)"))
        self.checkBox_1.setText(_translate("mainwindow", "系统优化"))
        self.radioButton.setText(_translate("mainwindow", "办公专用"))
        self.radioButton_2.setText(_translate("mainwindow", "一般装机"))
        self.checkBox_6.setText(_translate("mainwindow", "NotePad++"))
        self.checkBox_10.setText(_translate("mainwindow", "DirectX9"))
        self.checkBox_17.setText(_translate(
            "mainwindow", "Office 2013 Professional"))
        self.checkBox_9.setText(_translate("mainwindow", "Net Framework3"))
        self.checkBox_18.setText(_translate("mainwindow", "PhotoShop CS3"))
        self.checkBox_21.setText(_translate("mainwindow", "网易云音乐"))
        self.checkBox_11.setText(_translate("mainwindow", "360驱动大师"))
        self.checkBox_22.setText(_translate("mainwindow", "QQ音乐"))
        self.checkBox_20.setText(_translate("mainwindow", "Premiere CC2018"))
        self.checkBox_27.setText(_translate("mainwindow", "3DMAX2014"))
        self.checkBox_25.setText(_translate("mainwindow", "搜狗输入法"))
        self.checkBox_19.setText(_translate("mainwindow", "PhotoShop CC2018"))
        self.radioButton_4.setText(_translate("mainwindow", "取消选择"))
        self.label_2.setText(_translate("mainwindow", "解压程序选择："))
