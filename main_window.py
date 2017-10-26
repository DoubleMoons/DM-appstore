#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QTabWidget,
                             QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from header360 import Header
from sidebar import SideBar
from systemtray import SystemTray

from store_tab import StoreTab
from update_tab import UpdateTab
from uninstall_tab import UninstallTab
from more_tab import MoreTab


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName('MainWindow')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon('resource/format.ico'))
        self.setWindowTitle('PEI SoftwareCenter')
        self.resize(900, 600)

        with open('QSS/window.qss', 'r') as f:
            self.setStyleSheet(f.read())

        self.header = Header(self)
        self.sidebar = SideBar(self)
        self.storeTab = StoreTab(self)
        self.updateTab = UpdateTab(self)
        self.moreTab = MoreTab(self)
        self.uninstallTab = UninstallTab(self)
        self.set_lines()
        self.systemTray = SystemTray('resource/logo.png', self)
        self.systemTray.activated.connect(self.showNormal)

        self.mainTabs = QTabWidget(self)
        self.mainTabs.tabBar().setObjectName('mainTabs')

        self.mainTabs.addTab(self.storeTab, '')
        self.mainTabs.addTab(self.updateTab, '')
        self.mainTabs.addTab(self.uninstallTab, '')
        self.mainTabs.addTab(self.moreTab, '')
#        self.mainTabs.addTab(self.detailTab, '')

        self.mainTabs.setCurrentIndex(0)

        self.set_layouts()

    def set_lines(self):
        self.line1 = QFrame(self)
        self.line1.setObjectName('line1')
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Plain)
        self.line1.setLineWidth(2)

    def set_layouts(self):
        self.content_layout = QHBoxLayout()
        self.content_layout.setStretch(0, 70)
        self.content_layout.setStretch(1, 570)
        self.content_layout.addWidget(self.sidebar)
        self.content_layout.addWidget(self.mainTabs)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.line1)
        self.main_layout.addLayout(self.content_layout)

        self.main_layout.addStretch(1)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
