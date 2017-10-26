#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
import webbrowser
from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QApplication, QPushButton, QMenu, QAction, QVBoxLayout, QToolButton, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from search_bar import SearchBar
from login_dialog import LoginDialog
from about_dialog import AboutDialog
from feedback_dialog import FeedbackDialog
from setting_dialog import SettingDialog


class ToolButton(QToolButton):
    def __init__(self, pic_name, text: str, parent=None):
        super(ToolButton, self).__init__()
        self.parent = parent
        self.pixmap = QPixmap(pic_name)
        self.setIcon(QIcon(self.pixmap))
        self.setIconSize(self.pixmap.size())
        self.setText(text)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


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
        self.loginDialog = LoginDialog()
        self.setLogo()
        self.setTitle()
        self.setToolbutton()
        self.setMainmenu()
        self.setMenuBar()
        self.setSearchBar()
        self.setRightLayout()
        self.setLayouts()
        self.bindConnect()

    def setLogo(self):
        self.logo = QPushButton()
        self.logo.setObjectName('logo')
        self.pixmap = QPixmap('resource/user.png')
        self.logo.setIcon(QIcon(self.pixmap))
        self.logo.setIconSize(self.pixmap.size())

    def setTitle(self):
        self.title = QLabel('DM-appstore')
        self.title.setObjectName('title')
        self.loginButton = QPushButton('登录')
        self.loginButton.setObjectName('loginButton')
        self.loginButton.setFixedWidth(30)

        self.titleLayout = QVBoxLayout()
        self.titleLayout.addStretch(1)
        self.titleLayout.addWidget(self.title)
        self.titleLayout.addWidget(self.loginButton)
        self.titleLayout.addStretch(1)

    def setToolbutton(self):
        self.storeToolbutton = ToolButton('resource/ruanJian.png', '宝库')
        self.updateToolbutton = ToolButton('resource/jiaSu.png', '更新')
        self.uninstallToolbutton = ToolButton('resource/qingLi.png', '卸载')
        self.localToolbutton = ToolButton('resource/tiJian.png', '安装')
        self.moreToolbutton = ToolButton('resource/gongNeng.png', '更多')

        self.toolbtnLayout = QHBoxLayout()
        self.toolbtnLayout.addWidget(self.storeToolbutton)
        self.toolbtnLayout.addSpacing(15)
        self.toolbtnLayout.addWidget(self.updateToolbutton)
        self.toolbtnLayout.addSpacing(15)
        self.toolbtnLayout.addWidget(self.uninstallToolbutton)
        self.toolbtnLayout.addSpacing(15)
        self.toolbtnLayout.addWidget(self.localToolbutton)
        self.toolbtnLayout.addSpacing(15)
        self.toolbtnLayout.addWidget(self.moreToolbutton)

    def setMenuBar(self):
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

        self.minbtnLayout = QHBoxLayout()
        self.minbtnLayout.addStretch(1)
        self.minbtnLayout.addWidget(self.menuButton)
        self.minbtnLayout.addWidget(self.minButton)
        self.minbtnLayout.addWidget(self.closeButton)
        self.minbtnLayout.setContentsMargins(0, 0, 0, 0)

    def setSearchBar(self):
        self.searchBar = SearchBar(self)
        self.searchBar.setPlaceholderText('搜索软件')
        self.searchBar.setMaximumWidth(70)

        self.downloadButton = QPushButton()
        self.pixmap = QPixmap('resource/folder-download.png')
        self.downloadButton.setIcon(QIcon(self.pixmap))
        self.downloadButton.setIconSize(self.pixmap.size())

        self.searchbarLayout = QHBoxLayout()
        self.searchbarLayout.addStretch(1)
        self.searchbarLayout.addWidget(self.searchBar)
        self.searchbarLayout.addWidget(self.downloadButton)

    def setRightLayout(self):
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addLayout(self.minbtnLayout)
        self.rightLayout.addLayout(self.searchbarLayout)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)

    def setLayouts(self):
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.logo)
        self.mainLayout.addLayout(self.titleLayout)
        self.mainLayout.addSpacing(50)
        self.mainLayout.addLayout(self.toolbtnLayout)
        self.mainLayout.addLayout(self.rightLayout)

        self.setLayout(self.mainLayout)

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

    def bindConnect(self):
        self.logo.clicked.connect(self.ShowLoginDialog)
        self.storeToolbutton.clicked.connect(self.ShowStoreTab)
        self.updateToolbutton.clicked.connect(self.ShowUpdateTab)
        self.uninstallToolbutton.clicked.connect(self.ShowUninstallTab)
        self.moreToolbutton.clicked.connect(self.ShowMoreTab)
        self.localToolbutton.clicked.connect(self.ShowLocalTab)
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

    def ShowStoreTab(self):
        self.parent.mainTabs.setCurrentIndex(0)

    def ShowUpdateTab(self):
        self.parent.mainTabs.setCurrentIndex(1)

    def ShowUninstallTab(self):
        self.parent.mainTabs.setCurrentIndex(2)

    def ShowLocalTab(self):
        filename, filetype = QFileDialog.getOpenFileName(self, '打开deb文件', '/home', 'Deb Files(*.deb)')

    def ShowMoreTab(self):
        self.parent.mainTabs.setCurrentIndex(3)

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
            self.parent.m_DragPosition = event.globalPos() - self.parent.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.parent.move(event.globalPos() - self.parent.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Header()
    widget.show()
    sys.exit(app.exec_())
