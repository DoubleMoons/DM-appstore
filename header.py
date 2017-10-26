#! /usr/bin/ python3
# -*- coding: utf-8 -*-


import sys
import webbrowser
from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QApplication, QPushButton, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from search_bar import SearchBar
from login_dialog import LoginDialog
from about_dialog import AboutDialog
from feedback_dialog import FeedbackDialog
from setting_dialog import SettingDialog


class Header(QFrame):
    def __init__(self, parent=None):
        super(Header, self).__init__()
        self.setObjectName('Header')
        self.parent = parent

        with open('QSS/header.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        self.settingDialog = SettingDialog()
        self.feedbackDialog = FeedbackDialog()
        self.aboutDialog = AboutDialog()
        self.setMainmenu()
        self.setButtons()
        self.setLabels()
        self.setsearchBar()
        self.setLines()
        self.loginDialog = LoginDialog()
        self.setLayouts()
        self.bindConnect()

    def setButtons(self):
        """创建所有的按钮。"""

        self.loginButton = QPushButton("未登录 ▼", self)
        self.loginButton.setObjectName("loginButton")

        self.menuButton = QPushButton("☰")
        self.menuButton.setObjectName('menuButton')
        self.menuButton.setMinimumSize(21, 17)
        self.menuButton.setMenu(self.mainMenu)

        self.minButton = QPushButton('_', self)
        self.minButton.setObjectName("minButton")
        self.minButton.setMinimumSize(21, 17)

        self.closeButton = QPushButton('×', self)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setMinimumSize(21, 17)

        self.prevButton = QPushButton("<")
        self.prevButton.setObjectName("prevButton")
        self.prevButton.setMaximumSize(28, 22)
        self.prevButton.setMinimumSize(28, 22)

        self.nextButton = QPushButton(">")
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setMaximumSize(28, 22)
        self.nextButton.setMinimumSize(28, 22)

    def setLabels(self):
        """创建所需的所有标签。"""
        self.logo = QLabel()
        self.logo.setObjectName('logo')
        self.pixmap = QPixmap('resource/format.png')
        self.logo.setPixmap(self.pixmap)
        self.logo.setFixedSize(32, 32)

        self.title = QLabel()
        self.title.setObjectName('title')
        self.title.setText("<b>PEI SC<b>")

        self.userPic = QLabel()
        self.userPic.setObjectName('userPic')
        self.pixmap = QPixmap('resource/nouser.png')
        self.userPic.setPixmap(self.pixmap)
        self.userPic.setFixedSize(22, 22)

    def setsearchBar(self):
        """创建搜素框。"""
        self.searchBar = SearchBar(self)
        self.searchBar.setPlaceholderText("搜索软件")

    def setLines(self):
        """设置装饰用小细线。"""
        self.line1 = QFrame(self)
        self.line1.setObjectName("line1")
        self.line1.setFrameShape(QFrame.VLine)
        self.line1.setFrameShadow(QFrame.Plain)
        self.line1.setMaximumSize(1, 25)

    def setMainmenu(self):
        self.mainMenu = QMenu()
        self.settingAction = QAction(QIcon("resource/search.png"), " 设置", self.mainMenu)
        self.feedbackAction = QAction(QIcon("resource/search.png"), " 反馈", self.mainMenu)
        self.submitappAction = QAction(QIcon("resource/search.png"), " 提交软件", self.mainMenu)
        self.websiteAction = QAction(QIcon("resource/search.png"), " 官方网站", self.mainMenu)
        self.aboutAction = QAction(QIcon("resource/search.png"), " 关于", self.mainMenu)

        self.mainMenu.addAction(self.settingAction)
        self.mainMenu.addAction(self.feedbackAction)
        self.mainMenu.addAction(self.submitappAction)
        self.mainMenu.addAction(self.websiteAction)
        self.mainMenu.addAction(self.aboutAction)

    def setLayouts(self):
        """设置布局。"""
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.addWidget(self.logo)
        self.mainLayout.addWidget(self.title)
        self.mainLayout.addSpacing(70)
        self.mainLayout.addWidget(self.prevButton)
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.searchBar)
        self.mainLayout.addStretch(1)
        self.mainLayout.addWidget(self.userPic)
        self.mainLayout.addSpacing(7)
        self.mainLayout.addWidget(self.loginButton)
        self.mainLayout.addSpacing(7)
        self.mainLayout.addWidget(self.line1)
        self.mainLayout.addSpacing(30)
        self.mainLayout.addWidget(self.menuButton)
        self.mainLayout.addSpacing(3)
        self.mainLayout.addWidget(self.minButton)
        self.mainLayout.addSpacing(3)
        self.mainLayout.addWidget(self.closeButton)

        self.setLayout(self.mainLayout)

    def bindConnect(self):
        self.minButton.clicked.connect(self.parent.showMinimized)
        self.closeButton.clicked.connect(self.parent.close)
        self.loginButton.clicked.connect(self.ShowLoginDialog)
        self.settingAction.triggered.connect(self.ShowSettingDialog)
        self.feedbackAction.triggered.connect(self.ShowFeedbackDialog)
        self.submitappAction.triggered.connect(self.OpenSubmitUrl)
        self.websiteAction.triggered.connect(self.OpenOfficialWebsite)
        self.aboutAction.triggered.connect(self.ShowAboutDialog)

    def ShowLoginDialog(self):
        self.loginDialog.open()

    def ShowSettingDialog(self):
        self.settingDialog.open()

    def ShowFeedbackDialog(self):
        self.feedbackDialog.open()

    def OpenSubmitUrl(self):
        webbrowser.open('http://open.soft.360.cn')

    def OpenOfficialWebsite(self):
        webbrowser.open('http://www.baidu.com')

    def ShowAboutDialog(self):
        self.aboutDialog.open()

    """重写鼠标事件，实现窗口拖动。"""
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.m_drag = True
            self.parent.m_DragPosition = event.globalPos()-self.parent.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.parent.move(event.globalPos()-self.parent.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    header = Header()
    header.show()
    sys.exit(app.exec_())


