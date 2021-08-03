import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from os.path import isdir
from os import mkdir
from mainwindow import *
from scripts.menu import menu_format, menu_to_file
from thread import New_Thread


class MainWindow(QMainWindow, Ui_mainwindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.pushButton2_clicked)  # 按下浏览按钮
        self.pushButton.clicked.connect(self.pushButton_clicked)    # 按下解压按钮

    def pushButton2_clicked(self):
        """按下浏览按钮时的操作
        """
        _translate = QtCore.QCoreApplication.translate
        self.path = QFileDialog.getExistingDirectory(None, "选择文件夹路径")
        self.lineEdit.setText(_translate("mainwindow", self.path))

    def change_edit_text(self, _):
        """[通过unzip传入参数修改lineEdit与进度条进度]
        """
        _translate = QtCore.QCoreApplication.translate
        menu_dir = {'Wechat': '微信', 'NF3': 'Net Framework3', '360drv': '360驱动大师', 'Chrome': '谷歌浏览器', 'TXvideo': '腾讯视频',
                    'IQIYI': '爱奇艺(推荐)', 'DX': 'DirectX9', '163music': '网易云音乐', 'SougouPY': '搜狗输入法', 'QQmusic': 'QQ音乐',
                    'Dtalk': '钉钉', 'Kugou': '酷狗音乐(推荐)', '2345explorer': '2345浏览器(推荐)', '2345pinyin': '2345拼音输入法(推荐)', 'WPS': 'WPS(推荐)',
                    'sys_cra': '系统优化', 'T20': '天正建筑T20', 'PSCS3': 'PhotoShop CS3', 'PSCC2018': 'PhotoShop CC2018',
                    'OFFICE2013': 'Office 2013 Professional', 'PRCC2018': 'Premiere CC2018', 'Xunlei': '迅雷11', 'npplus': 'NotePad++',
                    'baidu_Netdisk': '百度网盘'}
        if len(self.choose ) != 0:
            self.lineEdit.setText(_translate(
                "mainwindow", f"正在解压{menu_dir[_] if _ in menu_dir else _}..."))
            self.programers_bar_value = (
                1 - len(self.choose) / self.initialValue) * 100     # 计算进度
            self.progressBar.setProperty("value", self.programers_bar_value)  # 实时更改进度
            self.choose.remove(menu_dir[_] if _ in menu_dir else _)
        if len(self.choose ) == 0:
            self.programers_bar_value = (1 - len(self.choose) / self.initialValue) * 100     # 计算进度
            self.progressBar.setProperty("value", self.programers_bar_value) 
        if len(self.choose) == 0 and self.Unzip.result:  # 解压完后执行的操作
            reply = QMessageBox.information(self,"安装包解压完毕","所有安装包解压完毕，点击确定关闭本程序", QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.close()
            
            
    def check_directory(self):
        """[检测lineEdit上填入的目录是否存在，不存在则创建]
        """
        if not isdir(self.path):
            mkdir(self.path)
    
    def pushButton_clicked(self):
        """按下解压按钮执行的操作
        """
        try:
            self.path = self.lineEdit.text()
            self.frame_2.setEnabled(False)
            self.pushButton.setEnabled(False)
            if self.checkBox_1.isChecked():
                self.choose.append(self.checkBox_1.text())
            if self.checkBox_2.isChecked():
                self.choose.append(self.checkBox_2.text())
            if self.checkBox_3.isChecked():
                self.choose.append(self.checkBox_3.text())
            if self.checkBox_4.isChecked():
                self.choose.append(self.checkBox_4.text())
            if self.checkBox_5.isChecked():
                self.choose.append(self.checkBox_5.text())
            if self.checkBox_6.isChecked():
                self.choose.append(self.checkBox_6.text())
            if self.checkBox_7.isChecked():
                self.choose.append(self.checkBox_7.text())
            if self.checkBox_8.isChecked():
                self.choose.append(self.checkBox_8.text())
            if self.checkBox_9.isChecked():
                self.choose.append(self.checkBox_9.text())
            if self.checkBox_10.isChecked():
                self.choose.append(self.checkBox_10.text())
            if self.checkBox_11.isChecked():
                self.choose.append(self.checkBox_11.text())
            if self.checkBox_12.isChecked():
                self.choose.append(self.checkBox_12.text())
            if self.checkBox_13.isChecked():
                self.choose.append(self.checkBox_13.text())
            if self.checkBox_14.isChecked():
                self.choose.append(self.checkBox_14.text())
            if self.checkBox_15.isChecked():
                self.choose.append(self.checkBox_15.text())
            if self.checkBox_16.isChecked():
                self.choose.append(self.checkBox_16.text())
            if self.checkBox_17.isChecked():
                self.choose.append(self.checkBox_17.text())
            if self.checkBox_18.isChecked():
                self.choose.append(self.checkBox_18.text())
            if self.checkBox_19.isChecked():
                self.choose.append(self.checkBox_19.text())
            if self.checkBox_20.isChecked():
                self.choose.append(self.checkBox_20.text())
            if self.checkBox_21.isChecked():
                self.choose.append(self.checkBox_21.text())
            if self.checkBox_22.isChecked():
                self.choose.append(self.checkBox_22.text())
            if self.checkBox_23.isChecked():
                self.choose.append(self.checkBox_23.text())
            if self.checkBox_24.isChecked():
                self.choose.append(self.checkBox_24.text())
            if self.checkBox_25.isChecked():
                self.choose.append(self.checkBox_25.text())
            if self.checkBox_26.isChecked():
                self.choose.append(self.checkBox_26.text())
            if self.checkBox_27.isChecked():
                self.choose.append(self.checkBox_27.text())
            if self.checkBox_28.isChecked():
                self.choose.append(self.checkBox_28.text())
            if self.checkBox_29.isChecked():
                self.choose.append(self.checkBox_29.text())
            if self.checkBox_30.isChecked():
                self.choose.append(self.checkBox_30.text())


            if len(self.choose) == 0:
                QMessageBox.information(self,"请选择安装包","请选择任意要解压的安装包后继续")  # 当用户没选择任何安装包时弹出提示并恢复解压按钮及frame2
                self.frame_2.setEnabled(True)
                self.pushButton.setEnabled(True)
            else:
                self.check_directory()
                self.initialValue = len(self.choose)  # 获取用户初始选择的程序数用做进度计算
                self.Unzip = New_Thread(menu_format(self.choose), self.path) 
                self.Unzip.finishSignal.connect(self.change_edit_text)  # 将pyqt5的信号传递给self.change函数处理
                self.Unzip.start()  # 启动多线程
                menu_to_file(path=self.path, choose=menu_format(self.choose))
        except Exception as _:
            with open("error.log", "w", encoding="utf-8") as f:
                f.write(str(_))

                              
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
