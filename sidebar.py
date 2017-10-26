#! /usr/bin/ python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QScrollArea, QListWidget, QListWidgetItem, QFrame, QApplication, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon


class SideBar(QScrollArea):
    def __init__(self, parent=None):
        super(SideBar, self).__init__(parent)
        self.parent = parent
        self.frame = QFrame()

        self.setMaximumWidth(200)
        self.setMinimumHeight(600)
        self.setWidget(self.frame)
        self.setWidgetResizable(True)
        self.frame.setMaximumWidth(180)

        with open('QSS/navigation.qss', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
            self.frame.setStyleSheet(style)

        self.setLabels()
        self.setListviews()
        self.setLayouts()

    def setLabels(self):
        self.recommendLabel = QLabel('精彩推荐')
        self.recommendLabel.setObjectName('recommendLabel')
        self.recommendLabel.setMaximumHeight(27)

        self.appstoreLabel = QLabel('软件仓库')
        self.appstoreLabel.setObjectName('appstoreLabel')
        self.appstoreLabel.setMaximumHeight(27)

    def setListviews(self):
        self.recommendList = QListWidget()
        self.recommendList.setMaximumHeight(110)
        self.recommendList.setObjectName('recommendList')
        self.recommendList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 热门安装"))
        self.recommendList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 装机必备"))
        self.recommendList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 我的收藏"))

        self.appstoreList = QListWidget()
        self.appstoreList.setObjectName('appstoreList')
        self.appstoreList.setMinimumHeight(400)
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 全部"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 影视"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 办公"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 网络"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 游戏"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 图像"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 系统"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 开发"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 驱动"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 科学"))
        self.appstoreList.addItem(QListWidgetItem(QIcon('resource/movie.png'), " 未分类"))

    def setLayouts(self):
        self.mainLayout = QVBoxLayout(self.frame)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.recommendLabel)
        self.mainLayout.addSpacing(3)
        self.mainLayout.addWidget(self.recommendList)
        self.mainLayout.addSpacing(1)
        self.mainLayout.addWidget(self.appstoreLabel)
        self.mainLayout.addSpacing(3)
        self.mainLayout.addWidget(self.appstoreList)
        self.mainLayout.addStretch(1)
        self.setContentsMargins(0, 0, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sidebar = SideBar()
    sidebar.show()
    sys.exit(app.exec_())
