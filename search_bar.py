#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor


class SearchBar(QLineEdit):
    """创建一个可自定义图片的输入框。"""
    def __init__(self, parent=None):
        super(SearchBar, self).__init__()
        self.setObjectName("SearchLine")
        self.parent = parent
        self.setMinimumSize(218, 20)
        with open('QSS/searchLine.qss', 'r') as f:
            self.setStyleSheet(f.read())

        self.button = QPushButton(self)
        self.button.setMaximumSize(13, 13)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))

        self.setTextMargins(3, 0, 19, 0)

        self.spaceItem = QSpacerItem(150, 10, QSizePolicy.Expanding)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addSpacerItem(self.spaceItem)
        # self.mainLayout.addStretch(1)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addSpacing(10)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)
    
    def setButtonSlot(self, funcName):
        self.button.clicked.connect(funcName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SearchBar()
    widget.show()
    sys.exit(app.exec_())
