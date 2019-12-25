import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()

    # 调整大小
    win.resize(1080, 650)

    # 位置
    win.move(400, 200)

    # 标题
    win.setWindowTitle('Binging Go')

    # 窗口显示
    win.show()

    sys.exit(app.exec_())

