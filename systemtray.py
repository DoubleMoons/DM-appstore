#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QAction, QMenu, QSystemTrayIcon, QApplication
from PyQt5.QtGui import QIcon


class SystemTray(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemTray, self).__init__(QIcon(icon))
        self.parent = parent

        self.menu = QMenu(self.parent)
        self.setContextMenu(self.menu)
        self.checkupdateAction = self.menu.addAction('检查更新')
        self.exitAction = self.menu.addAction('退出')
       
        self.checkupdateAction.triggered.connect(self.CheckUpdate)
        self.exitAction.triggered.connect(self.parent.close)

        self.show()

    def CheckUpdate(self):
        pass


