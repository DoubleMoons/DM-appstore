#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from base import Header


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__()
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('关于')
        self.setObjectName('AboutDialog')
        self.resize(520, 300)

        self.header = Header('关于', self)
        self.header.setFixedHeight(40)
        self.header.closeButton.clicked.connect(self.close)

        self.aboutImg = QLabel()
        self.aboutImg.setObjectName('aboutImg')
        self.pixmap = QPixmap('resource/format.png')
        self.aboutImg.setPixmap(self.pixmap)
        self.aboutImg.setFixedSize(32, 32)

        self.aboutName = QLabel('DM-appstore')
        self.aboutName.setObjectName('aboutName')

        self.aboutDscr = QLabel('DM-appstore是基于python3和PyQt5创建的ubuntu软件中心')
        self.aboutDscr.setObjectName('aboutDscr')

        self.aboutGithub = QLabel('http://www.baidu.com')
        self.aboutDscr.setObjectName('aboutGithub')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.header)
        self.mainLayout.addStretch(1)
        self.mainLayout.addWidget(self.aboutImg)
        self.mainLayout.addWidget(self.aboutName)
        self.mainLayout.addWidget(self.aboutDscr)
        self.mainLayout.addWidget(self.aboutGithub)
        self.mainLayout.addStretch(1)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AboutDialog()
    widget.show()
    app.exec_()


