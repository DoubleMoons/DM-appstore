#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout


class StoreTab(QWidget):
    def __init__(self, parent=None):
        super(StoreTab, self).__init__()
        self.setObjectName('RecommendTab')
        self.parent = parent

        self.label = QLabel('RecommendTab')

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)

        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = StoreTab()
    widget.show()
    app.exec_(sys.exit())
