# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(623, 380)
        mainwindow.setMinimumSize(QtCore.QSize(623, 380))
        mainwindow.setMaximumSize(QtCore.QSize(623, 380))
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 581, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 15, 54, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 391, 20))
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(470, 10, 40, 23))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(520, 10, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 90, 581, 231))
        self.frame_2.setBaseSize(QtCore.QSize(0, 1))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 562, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_31 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_31.setObjectName("checkBox_31")
        self.gridLayout_2.addWidget(self.checkBox_31, 1, 2, 1, 1)
        self.checkBox_32 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_32.setObjectName("checkBox_32")
        self.gridLayout_2.addWidget(self.checkBox_32, 1, 3, 1, 1)
        self.checkBox_33 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_33.setObjectName("checkBox_33")
        self.gridLayout_2.addWidget(self.checkBox_33, 1, 1, 1, 1)
        self.checkBox_34 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_34.setObjectName("checkBox_34")
        self.gridLayout_2.addWidget(self.checkBox_34, 2, 0, 1, 1)
        self.checkBox_35 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_35.setObjectName("checkBox_35")
        self.gridLayout_2.addWidget(self.checkBox_35, 4, 0, 1, 1)
        self.checkBox_36 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_36.setObjectName("checkBox_36")
        self.gridLayout_2.addWidget(self.checkBox_36, 2, 1, 1, 1)
        self.checkBox_37 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_37.setObjectName("checkBox_37")
        self.gridLayout_2.addWidget(self.checkBox_37, 1, 0, 1, 1)
        self.checkBox_38 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_38.setObjectName("checkBox_38")
        self.gridLayout_2.addWidget(self.checkBox_38, 3, 0, 1, 1)
        self.checkBox_39 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_39.setObjectName("checkBox_39")
        self.gridLayout_2.addWidget(self.checkBox_39, 3, 2, 1, 1)
        self.checkBox_40 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_40.setObjectName("checkBox_40")
        self.gridLayout_2.addWidget(self.checkBox_40, 3, 1, 1, 1)
        self.checkBox_41 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_41.setObjectName("checkBox_41")
        self.gridLayout_2.addWidget(self.checkBox_41, 3, 3, 1, 1)
        self.checkBox_42 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_42.setObjectName("checkBox_42")
        self.gridLayout_2.addWidget(self.checkBox_42, 0, 0, 1, 1)
        self.checkBox_43 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_43.setObjectName("checkBox_43")
        self.gridLayout_2.addWidget(self.checkBox_43, 2, 3, 1, 1)
        self.checkBox_44 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_44.setObjectName("checkBox_44")
        self.gridLayout_2.addWidget(self.checkBox_44, 0, 1, 1, 1)
        self.checkBox_45 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_45.setObjectName("checkBox_45")
        self.gridLayout_2.addWidget(self.checkBox_45, 0, 3, 1, 1)
        self.checkBox_46 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_46.setObjectName("checkBox_46")
        self.gridLayout_2.addWidget(self.checkBox_46, 0, 2, 1, 1)
        self.checkBox_47 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_47.setObjectName("checkBox_47")
        self.gridLayout_2.addWidget(self.checkBox_47, 2, 2, 1, 1)
        self.checkBox_48 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_48.setObjectName("checkBox_48")
        self.gridLayout_2.addWidget(self.checkBox_48, 4, 3, 1, 1)
        self.checkBox_49 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_49.setObjectName("checkBox_49")
        self.gridLayout_2.addWidget(self.checkBox_49, 5, 0, 1, 1)
        self.checkBox_50 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_50.setObjectName("checkBox_50")
        self.gridLayout_2.addWidget(self.checkBox_50, 5, 1, 1, 1)
        self.checkBox_51 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_51.setObjectName("checkBox_51")
        self.gridLayout_2.addWidget(self.checkBox_51, 4, 1, 1, 1)
        self.checkBox_52 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_52.setObjectName("checkBox_52")
        self.gridLayout_2.addWidget(self.checkBox_52, 4, 2, 1, 1)
        self.checkBox_53 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_53.setObjectName("checkBox_53")
        self.gridLayout_2.addWidget(self.checkBox_53, 6, 0, 1, 1)
        self.checkBox_54 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_54.setObjectName("checkBox_54")
        self.gridLayout_2.addWidget(self.checkBox_54, 6, 2, 1, 1)
        self.checkBox_55 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_55.setObjectName("checkBox_55")
        self.gridLayout_2.addWidget(self.checkBox_55, 5, 3, 1, 1)
        self.checkBox_56 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_56.setObjectName("checkBox_56")
        self.gridLayout_2.addWidget(self.checkBox_56, 5, 2, 1, 1)
        self.checkBox_57 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_57.setObjectName("checkBox_57")
        self.gridLayout_2.addWidget(self.checkBox_57, 6, 1, 1, 1)
        self.checkBox_58 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_58.setObjectName("checkBox_58")
        self.gridLayout_2.addWidget(self.checkBox_58, 6, 3, 1, 1)
        self.checkBox_59 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_59.setObjectName("checkBox_59")
        self.gridLayout_2.addWidget(self.checkBox_59, 7, 0, 1, 1)
        self.checkBox_60 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_60.setObjectName("checkBox_60")
        self.gridLayout_2.addWidget(self.checkBox_60, 7, 3, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 7, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 7, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(110, 70, 260, 15))
        self.progressBar.setToolTipDuration(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.frame.raise_()
        self.frame_2.raise_()
        self.label_2.raise_()
        self.progressBar.raise_()
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 23))
        self.menubar.setObjectName("menubar")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "安装文件解压器 v0.1 by:冼叔叔"))
        self.label.setText(_translate("mainwindow", "解压路径："))
        self.lineEdit.setText(_translate("mainwindow", "D:\\"))
        self.toolButton.setText(_translate("mainwindow", "..."))
        self.pushButton.setText(_translate("mainwindow", "解压"))
        self.label_2.setText(_translate("mainwindow", "解压程序选择："))
        self.checkBox_31.setText(_translate("mainwindow", "百度网盘"))
        self.checkBox_32.setText(_translate("mainwindow", "VCRedist"))
        self.checkBox_33.setText(_translate("mainwindow", "NotePad++"))
        self.checkBox_34.setText(_translate("mainwindow", "Net Framework3"))
        self.checkBox_35.setText(_translate("mainwindow", "Office 2013 Professional"))
        self.checkBox_36.setText(_translate("mainwindow", "DirectX9"))
        self.checkBox_37.setText(_translate("mainwindow", "Winrar"))
        self.checkBox_38.setText(_translate("mainwindow", "谷歌浏览器"))
        self.checkBox_39.setText(_translate("mainwindow", "腾讯视频"))
        self.checkBox_40.setText(_translate("mainwindow", "2345浏览器(推荐)"))
        self.checkBox_41.setText(_translate("mainwindow", "爱奇艺(推荐)"))
        self.checkBox_42.setText(_translate("mainwindow", "系统优化"))
        self.checkBox_43.setText(_translate("mainwindow", "WPS(推荐)"))
        self.checkBox_44.setText(_translate("mainwindow", "QQ"))
        self.checkBox_45.setText(_translate("mainwindow", "钉钉"))
        self.checkBox_46.setText(_translate("mainwindow", "微信"))
        self.checkBox_47.setText(_translate("mainwindow", "360驱动大师"))
        self.checkBox_48.setText(_translate("mainwindow", "Premiere CC2018"))
        self.checkBox_49.setText(_translate("mainwindow", "网易云音乐"))
        self.checkBox_50.setText(_translate("mainwindow", "QQ音乐"))
        self.checkBox_51.setText(_translate("mainwindow", "PhotoShop CS3"))
        self.checkBox_52.setText(_translate("mainwindow", "PhotoShop CC2018"))
        self.checkBox_53.setText(_translate("mainwindow", "搜狗输入法"))
        self.checkBox_54.setText(_translate("mainwindow", "3DMAX2014"))
        self.checkBox_55.setText(_translate("mainwindow", "迅雷11"))
        self.checkBox_56.setText(_translate("mainwindow", "酷狗音乐(推荐)"))
        self.checkBox_57.setText(_translate("mainwindow", "2345拼音输入法(推荐)"))
        self.checkBox_58.setText(_translate("mainwindow", "CAD2014"))
        self.checkBox_59.setText(_translate("mainwindow", "CAD2007"))
        self.checkBox_60.setText(_translate("mainwindow", "天正建筑T20"))
        self.radioButton_3.setText(_translate("mainwindow", "全选"))
        self.radioButton_4.setText(_translate("mainwindow", "取消全选"))
