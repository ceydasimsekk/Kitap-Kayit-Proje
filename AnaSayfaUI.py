# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1344, 1005)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet("QWidget#frmLogin,QWidget#frmPopup,QWidget#frmHostInfo,QWidget#frmLogout,QWidget#frmConfig,QWidget#frmData,QWidget#frmDefence,QWidget#frmHost,QWidget#frmMain,QWidget#frmPwd,QWidget#frmSelect,QWidget#frmMessageBox{\n"
"    border:1px solid #0F7DBE;\n"
"    border-radius:0px;    \n"
"}\n"
"\n"
".QFrame{\n"
"    border:1px solid #50A3F0;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #50A3F0;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background: none;\n"
"    selection-background-color: #0F7DBE;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { \n"
"    lineedit-password-character: 9679; \n"
"}\n"
"\n"
".QGroupBox{\n"
"    border: 1px solid #50A3F0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
".QPushButton{\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 5px;    \n"
"    min-height: 20px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
".QPushButton[focusPolicy=\"0\"] {\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 0px;    \n"
"    min-height: 10px;\n"
"    border-radius:3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
".QPushButton:hover{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA);\n"
"}\n"
"\n"
".QPushButton:pressed{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3);\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(25, 134, 199, 0), stop:1 #50A3F0);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(238, 0, 0, 128), stop:1 rgba(238, 44, 44, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 2px; \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/qss_icons/img_rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/qss_icons/img_rc/checkbox_checked.png); \n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 15px; \n"
"    height: 15px; \n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    image: url(:/qss_icons/img_rc/radio_normal.png); \n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    image: url(:/qss_icons/img_rc/radio_selected.png); \n"
"}\n"
"\n"
"QComboBox,QDateEdit{\n"
"    border-radius: 3px;\n"
"    padding: 1px 10px 1px 5px;\n"
"    border: 1px solid #50A3F0;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px; \n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-left-color: #50A3F0;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit::down-arrow {\n"
"    image: url(:/qss_icons/img_rc/array_down.png); \n"
"}\n"
"\n"
"QMenu {\n"
"    background-color:#F0F0F0;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::item {    \n"
"    padding: 2px 12px 2px 12px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #50A3F0;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    border: 1px solid #50A3F0;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 5px; \n"
"    margin: 0.5px;\n"
"    background-color: #0F7DBE;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal { \n"
"    background: #808080; \n"
"    height: 8px; \n"
"    border-radius: 3px; \n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    height: 8px; \n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 13px; \n"
"    margin-top: -3px; \n"
"    margin-bottom: -3px; \n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,stop:0.6 #F0F0F0, stop:0.778409 #50A3F0);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #0F7DBE);\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical {\n"
"    background:#808080; \n"
"    width: 8px; \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    width: 8px;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 14px; \n"
"    margin-left: -3px;\n"
"    margin-right: -3px;\n"
"    border-radius: 6px;\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0, stop:0.778409 #50A3F0);\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6 #F0F0F0,stop:0.778409 #0F7DBE);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-top:10px; \n"
"    padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height:10px; \n"
"    background-color:rgba(0,0,0,0%); \n"
"    padding-left:10px; padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    width:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    height:10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: bottom; \n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/add-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/add-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: top; \n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/sub-line_vertical.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    height:10px;\n"
"    width:10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    border-image:url(:/qss_icons/img_rc/sub-line_horizontal.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {\n"
"    width:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"    height:10px;\n"
"    background: #C0C0C0;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 0px ; \n"
"}\n"
"\n"
"QTreeView,QListView,QTableView{\n"
"    border: 1px solid #50A3F0; \n"
"    selection-background-color: #0F7DBE;\n"
"    selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QTableView::item:selected, QListView::item:selected, QTreeView::item:selected {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QTableView::item:hover, QListView::item:hover, QTreeView::item:hover {\n"
"    color: #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QTableView::item, QListView::item, QTreeView::item {\n"
"    padding: 5px; \n"
"    margin: 0px; \n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    padding:3px;\n"
"    margin:0px;\n"
"    color:#F0F0F0;\n"
"    border: 1px solid #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom-left-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    color: #F0F0F0;\n"
"    min-width: 60px;\n"
"    min-height: 20px;\n"
"    padding: 3px 8px 3px 8px;\n"
"    margin:1px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #50A3F0, stop:1 #489CEA); \n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0F7DBE, stop:1 #1582C3); \n"
"}\n"
"\n"
"QStatusBar::item {\n"
"     border: 1px solid #50A3F0;\n"
"     border-radius: 3px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.KitapBilgileri = QtWidgets.QGroupBox(self.centralwidget)
        self.KitapBilgileri.setGeometry(QtCore.QRect(150, 10, 1031, 591))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.KitapBilgileri.setFont(font)
        self.KitapBilgileri.setObjectName("KitapBilgileri")
        self.leSayfaSayisi = QtWidgets.QLineEdit(self.KitapBilgileri)
        self.leSayfaSayisi.setGeometry(QtCore.QRect(151, 138, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.leSayfaSayisi.setFont(font)
        self.leSayfaSayisi.setTabletTracking(False)
        self.leSayfaSayisi.setAutoFillBackground(False)
        self.leSayfaSayisi.setObjectName("leSayfaSayisi")
        self.label_6 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_6.setGeometry(QtCore.QRect(70, 200, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.leKitapAd = QtWidgets.QLineEdit(self.KitapBilgileri)
        self.leKitapAd.setGeometry(QtCore.QRect(151, 80, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.leKitapAd.setFont(font)
        self.leKitapAd.setTabletTracking(False)
        self.leKitapAd.setAutoFillBackground(False)
        self.leKitapAd.setObjectName("leKitapAd")
        self.leTur = QtWidgets.QLineEdit(self.KitapBilgileri)
        self.leTur.setGeometry(QtCore.QRect(151, 167, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.leTur.setFont(font)
        self.leTur.setTabletTracking(False)
        self.leTur.setAutoFillBackground(False)
        self.leTur.setObjectName("leTur")
        self.leYazarAd = QtWidgets.QLineEdit(self.KitapBilgileri)
        self.leYazarAd.setGeometry(QtCore.QRect(151, 109, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.leYazarAd.setFont(font)
        self.leYazarAd.setTabletTracking(False)
        self.leYazarAd.setAutoFillBackground(False)
        self.leYazarAd.setObjectName("leYazarAd")
        self.label_5 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_5.setGeometry(QtCore.QRect(70, 170, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.leYayinevi = QtWidgets.QLineEdit(self.KitapBilgileri)
        self.leYayinevi.setGeometry(QtCore.QRect(151, 196, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.leYayinevi.setFont(font)
        self.leYayinevi.setTabletTracking(False)
        self.leYayinevi.setAutoFillBackground(False)
        self.leYayinevi.setObjectName("leYayinevi")
        self.label_2 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.KitapBilgileri)
        self.label.setGeometry(QtCore.QRect(71, 51, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leKitapNo = QtWidgets.QLineEdit(self.KitapBilgileri)
        self.leKitapNo.setGeometry(QtCore.QRect(151, 51, 201, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.leKitapNo.setFont(font)
        self.leKitapNo.setTabletTracking(False)
        self.leKitapNo.setAutoFillBackground(False)
        self.leKitapNo.setObjectName("leKitapNo")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.KitapBilgileri)
        self.calendarWidget_2.setGeometry(QtCore.QRect(520, 350, 401, 231))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.cwBaslangic = QtWidgets.QCalendarWidget(self.KitapBilgileri)
        self.cwBaslangic.setGeometry(QtCore.QRect(50, 350, 391, 236))
        self.cwBaslangic.setObjectName("cwBaslangic")
        self.label_10 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_10.setGeometry(QtCore.QRect(190, 320, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_11.setGeometry(QtCore.QRect(680, 320, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.KitabiDerecelendir = QtWidgets.QSpinBox(self.KitapBilgileri)
        self.KitabiDerecelendir.setGeometry(QtCore.QRect(650, 260, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.KitabiDerecelendir.setFont(font)
        self.KitabiDerecelendir.setMaximum(5)
        self.KitabiDerecelendir.setSingleStep(1)
        self.KitabiDerecelendir.setProperty("value", 0)
        self.KitabiDerecelendir.setObjectName("KitabiDerecelendir")
        self.textEdit = QtWidgets.QTextEdit(self.KitapBilgileri)
        self.textEdit.setGeometry(QtCore.QRect(520, 30, 341, 211))
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_8.setGeometry(QtCore.QRect(520, 10, 231, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.KitapBilgileri)
        self.label_9.setGeometry(QtCore.QRect(520, 270, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btnKayitGuncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btnKayitGuncelle.setGeometry(QtCore.QRect(360, 620, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnKayitGuncelle.setFont(font)
        self.btnKayitGuncelle.setObjectName("btnKayitGuncelle")
        self.btnKayitEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnKayitEkle.setGeometry(QtCore.QRect(150, 620, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnKayitEkle.setFont(font)
        self.btnKayitEkle.setObjectName("btnKayitEkle")
        self.btnKaydiSil = QtWidgets.QPushButton(self.centralwidget)
        self.btnKaydiSil.setGeometry(QtCore.QRect(570, 620, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnKaydiSil.setFont(font)
        self.btnKaydiSil.setObjectName("btnKaydiSil")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 670, 1171, 261))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(112)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(68)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.btnTumKayit = QtWidgets.QPushButton(self.centralwidget)
        self.btnTumKayit.setGeometry(QtCore.QRect(1030, 620, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTumKayit.setFont(font)
        self.btnTumKayit.setObjectName("btnTumKayit")
        self.btnKayitAra = QtWidgets.QPushButton(self.centralwidget)
        self.btnKayitAra.setGeometry(QtCore.QRect(780, 620, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnKayitAra.setFont(font)
        self.btnKayitAra.setObjectName("btnKayitAra")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1344, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.KitapBilgileri.setTitle(_translate("MainWindow", "Kitap Bilgileri"))
        self.leSayfaSayisi.setInputMask(_translate("MainWindow", "9999999999"))
        self.label_6.setText(_translate("MainWindow", "Yayınevi:"))
        self.label_5.setText(_translate("MainWindow", "Tür:"))
        self.label_2.setText(_translate("MainWindow", "Kitap Ad:"))
        self.label.setText(_translate("MainWindow", "Kitap No:"))
        self.label_4.setText(_translate("MainWindow", "Sayfa Sayısı:"))
        self.label_3.setText(_translate("MainWindow", "Yazar Ad:"))
        self.leKitapNo.setInputMask(_translate("MainWindow", "9999999999999"))
        self.leKitapNo.setPlaceholderText(_translate("MainWindow", "13 haneli  ISBN numarasını giriniz"))
        self.label_10.setText(_translate("MainWindow", "Kitap Başlangıç"))
        self.label_11.setText(_translate("MainWindow", "Kitap Bitiş"))
        self.label_8.setText(_translate("MainWindow", "Kitap Hakkında Kısaca Düşünceler:"))
        self.label_9.setText(_translate("MainWindow", "Kitabı Derecelendir:"))
        self.btnKayitGuncelle.setText(_translate("MainWindow", "KAYIT GÜNCELLE"))
        self.btnKayitEkle.setText(_translate("MainWindow", "KAYIT EKLE"))
        self.btnKaydiSil.setText(_translate("MainWindow", "KAYDI SİL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Kitap No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kitap Ad"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yazar Ad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sayfa Sayısı"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tür"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Yayınevi"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Kitap Başlangıç"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Kitap Bitiş"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Derecelendir"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Düşünceler"))
        self.btnTumKayit.setText(_translate("MainWindow", "TÜM KAYDI LİSTELE"))
        self.btnKayitAra.setText(_translate("MainWindow", "KAYIT ARA"))

