import sys
from time import sleep

from PyQt5.QtWidgets import QApplication, QMainWindow

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
        _translate = QtCore.QCoreApplication.translate
        menu_dir = {'Wechat': '微信', 'NF3': 'Net Framework3', '360drv': '360驱动大师', 'Chrome': '谷歌浏览器', 'TXvideo': '腾讯视频',
                    'IQIYI': '爱奇艺(推荐)', 'DX': 'DirectX9', '163music': '网易云音乐', 'SougouPY': '搜狗输入法', 'QQmusic': 'QQ音乐',
                    'Dtalk': '钉钉', 'Kugou': '酷狗音乐(推荐)', '2345explorer': '2345浏览器(推荐)', '2345pinyin': '2345拼音输入法(推荐)', 'WPS': 'WPS(推荐)',
                    'sys_cra': '系统优化', 'T20': '天正建筑T20', 'PSCS3': 'PhotoShop CS3', 'PSCC2018': 'PhotoShop CC2018',
                    'OFFICE2013': 'Office 2013 Professional', 'PRCC2018': 'Premiere CC2018', 'Xunlei': '迅雷11', 'npplus': 'NotePad++',
                    'baidu_Netdisk': '百度网盘'}

        self.lineEdit.setText(_translate(
            "mainwindow", f"正在解压{menu_dir[_] if _ in menu_dir else _}..."))
        self.programers_bar_value = (
            1 - len(self.choose) / self.initialValue) * 100     # 计算进度
        self.progressBar.setProperty("value", self.programers_bar_value)
        self.choose.remove(menu_dir[_] if _ in menu_dir else _)

    def pushButton_clicked(self):
        """按下解压按钮执行的操作
        """
        self.frame_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        if self.checkBox_1.isChecked():
            self.choose.append('系统优化')
        if self.checkBox_2.isChecked():
            self.choose.append('QQ')
        if self.checkBox_3.isChecked():
            self.choose.append('微信')
        if self.checkBox_4.isChecked():
            self.choose.append('钉钉')
        if self.checkBox_5.isChecked():
            self.choose.append('Winrar')
        if self.checkBox_6.isChecked():
            self.choose.append('NotePad++')
        if self.checkBox_7.isChecked():
            self.choose.append('百度网盘')
        if self.checkBox_8.isChecked():
            self.choose.append('VCRedist')
        if self.checkBox_9.isChecked():
            self.choose.append('Net Framework3')
        if self.checkBox_10.isChecked():
            self.choose.append('DirectX9')
        if self.checkBox_11.isChecked():
            self.choose.append('Office 2013 Professional')
        if self.checkBox_12.isChecked():
            self.choose.append('WPS(推荐)')
        if self.checkBox_13.isChecked():
            self.choose.append('360驱动大师')
        if self.checkBox_14.isChecked():
            self.choose.append('谷歌浏览器')
        if self.checkBox_15.isChecked():
            self.choose.append('2345浏览器(推荐)')
        if self.checkBox_16.isChecked():
            self.choose.append('腾讯视频')
        if self.checkBox_17.isChecked():
            self.choose.append('爱奇艺(推荐)')
        if self.checkBox_18.isChecked():
            self.choose.append('PhotoShop CS3')
        if self.checkBox_19.isChecked():
            self.choose.append('PhotoShop CC2018')
        if self.checkBox_20.isChecked():
            self.choose.append('Premiere CC2018')
        if self.checkBox_21.isChecked():
            self.choose.append('网易云音乐')
        if self.checkBox_22.isChecked():
            self.choose.append('QQ音乐')
        if self.checkBox_23.isChecked():
            self.choose.append('酷狗音乐(推荐)')
        if self.checkBox_24.isChecked():
            self.choose.append('迅雷11')
        if self.checkBox_25.isChecked():
            self.choose.append('搜狗输入法')
        if self.checkBox_26.isChecked():
            self.choose.append('2345拼音输入法(推荐)')
        if self.checkBox_27.isChecked():
            self.choose.append('3DMAX2014')
        if self.checkBox_28.isChecked():
            self.choose.append('CAD2014')
        if self.checkBox_29.isChecked():
            self.choose.append('CAD2007')
        if self.checkBox_30.isChecked():
            self.choose.append('天正建筑T20'
                               )
        self.initialValue = len(self.choose)
        self.Unzip = New_Thread(menu_format(self.choose), self.path)
        self.Unzip.finishSignal.connect(self.change_edit_text)
        self.Unzip.unzip()
        self.programers_bar_value = (
            1 - len(self.choose) / self.initialValue) * 100     # 计算进度
        self.progressBar.setProperty("value", self.programers_bar_value)
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate(
            "mainwindow", "安装包解压完毕,程序将在5秒后自动关闭......"))
        menu_to_file(path=self.path, choose=menu_format(self.choose))
        sleep(5)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
