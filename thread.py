import zipfile

from PyQt5.QtCore import *


class New_Thread(QThread):

    finishSignal = pyqtSignal(str)

    def __init__(self, programs, path, parent=None,):
        super(New_Thread, self).__init__(parent)
        self.programs = programs
        self.path = path
        self.result = False # 判断线程是否执行结束的标记
    def run(self):
        zip_file = zipfile.ZipFile("auto_install.zip", "r")
        for _ in self.programs:
            for name in zip_file.namelist():
                if _ in name:
                    zip_file.extract(name, self.path)
            self.finishSignal.emit(str(_))

        zip_file.extract('auto_install.exe', self.path)
        zip_file.close()
        self.result = True
        self.finishSignal.emit(str(_))