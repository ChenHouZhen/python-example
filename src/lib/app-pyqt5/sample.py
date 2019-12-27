import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()

    # 调整大小
    win.resize(1080, 650)

    # 位置
    win.move(400, 200)

    # 标题
    win.setWindowTitle('Binging Go')

    # 菜单栏
    menu = win.menuBar()
    # 菜单
    file_menu = menu.addMenu("File")
    edit_menu = menu.addMenu("Edit")
    view_menu = menu.addMenu("View")

    # 行为
    new_project_action = QAction('New Project')
    file_menu.addAction(new_project_action)

    exit_action = QAction('Exit')

    # 快捷键
    exit_action.setShortcut('Ctrl+Q')

    # 点击
    exit_action.triggered.connect(win.close)

    file_menu.addAction(exit_action)

    # 窗口显示
    win.show()

    sys.exit(app.exec_())

