# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'horde_attempt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

#horde_output = the output screen
#genHorde = The button pushed to generate the horde
#dungeon_diff = slider that determines how hard the dungeon is
#wage_disp = slider that determines wage disparity

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def __init__(self):
        self.B = 50
        self.range_list = []
        self.H = 0
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horde_output = QtWidgets.QLabel(self.centralwidget)
        self.horde_output.setWordWrap(True)
        self.horde_output.setGeometry(QtCore.QRect(120, 320, 361, 231))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.horde_output.setFont(font)
        self.horde_output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horde_output.setWordWrap(False)
        self.horde_output.setObjectName("horde_output")
        
        self.genHorde = QtWidgets.QPushButton(self.centralwidget)
        self.genHorde.setGeometry(QtCore.QRect(240, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.genHorde.setFont(font)
        self.genHorde.setObjectName("genHorde")
        self.genHorde.clicked.connect(self.clicked)
        
        self.dungeon_diff = QtWidgets.QSlider(self.centralwidget)
        self.dungeon_diff.setGeometry(QtCore.QRect(120, 240, 361, 22))
        self.dungeon_diff.setMinimum(1)
        self.dungeon_diff.setMaximum(20)
        self.dungeon_diff.setOrientation(QtCore.Qt.Horizontal)
        self.dungeon_diff.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.dungeon_diff.setTickInterval(1)
        self.dungeon_diff.setObjectName("dungeon_diff")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.wage_disp = QtWidgets.QSlider(self.centralwidget)
        self.wage_disp.setGeometry(QtCore.QRect(220, 150, 160, 22))
        self.wage_disp.setMinimum(1)
        self.wage_disp.setMaximum(3)
        self.wage_disp.setOrientation(QtCore.Qt.Horizontal)
        self.wage_disp.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.wage_disp.setTickInterval(1)
        self.wage_disp.setObjectName("wage_disp")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 120, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuHorde = QtWidgets.QMenu(self.menubar)
        self.menuHorde.setObjectName("menuHorde")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.menubar.addAction(self.menuHorde.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.horde_output.setText(_translate("MainWindow", "TextLabel"))
        self.genHorde.setText(_translate("MainWindow", "Generate Horde"))
        self.label.setText(_translate("MainWindow", "Set Dungeon Difficulty"))
        self.label_2.setText(_translate("MainWindow", "Set Wage Disparity"))
        self.menuHorde.setTitle(_translate("MainWindow", "Horde"))

    def gen_bpower(self, n):	
        self.c = self.Power(self.B/(n*2), ["Copper Ring", "Polished Silverware", "Dagger", "Sword", "Spear", "Shield"], {"Copper Ring": 8, "Polished Silverware": 20, "Dagger": 2, "Sword": 15, "Spear": 1, "Shield": 10, "Simple Amulet": 5})
        self.b = self.Power(self.B, ["Weak Magic Ring", "Weak Magic Bracer", "Ornate Necklace", "Potion of Healing", "Potion of Slickness"], {"Weak Magic Ring": 40, "Weak Magic Bracer": 35, "Ornate Necklace":75, "Potion of Healing": 50, "Potion of Slickness": 35})
        self.b1 = self.Power(self.B * (n*2), ["Potion of Greater Healing", "Masterwork Weapon", "Drow Poison", "Rare Fang"], {"Potion of Greater Healing": 200, "Masterwork Weapon" : 300, "Drow Poison": 175, "Rare Fang": 100})
        self.b2 = self.Power(self.B * (n*8), ["Potion of Superior Healing", "+1 Weapon"], {"Potion of Superior Healing": 800, "+1 Weapon": 2000})
        self.b3 = self.Power(self.B * (n*32), ["Potion of Supreme Healing", "+2 Weapon"], {"Potion of Supreme Healing": 3200, "+2 Weapon": 8000})
        self.b4 = self.Power(self.B * (n*256), ["Ambrosia", "Scroll of One-Thousand Swords", "Grimoir of Nemesis", "Ashen Staff", "The Hero's Sword", "+3 Weapon"], {"Ambrosia": 12000, "Scroll of One-Thousand Swords": 8000, "Grimoir of Nemesis": 10000, "Ashen Staff": 15000, "The Hero's Sword": 25000, "+3 Weapon": 18000})
        self.range_list = [self.c, self.b, self.b1, self.b2, self.b3, self.b4]
    
    def gen_gold(self, dif):
        i = dif % 4
        m_tier = self.range_list[int(dif/4)]
        self.H = int((m_tier.bpower *(3.5 * (i + 1.45)) + 65) * random.uniform(0.85, 1.15))

    def gen_loot(self, dif):
        m_tier = self.range_list[int(dif/4)]
        arr_num = len(m_tier.loot)
        loot = m_tier.loot[random.randint(0,(arr_num - 1))]	
        self.H = self.H - m_tier.loot_val[loot]
        return(loot)

    def clicked(self):
        self.gen_bpower(self.wage_disp.value())
        self.gen_gold(self.dungeon_diff.value())
        #!!! Check this out, added recently
        loot_amount = random.randint(1, 3)
        loot_total = ""
        
        while(loot_amount != 0):
            loot = self.gen_loot(self.dungeon_diff.value())
            loot_total += loot + ", "
            loot_amount = loot_amount - 1
		
        print(loot_total)
        self.horde_output.setText("The horde contains;" + "\n" + str(self.H) + " gold pieces." + "\n" + loot_total)
        self.horde_output.setWordWrap(True)
        #self.horde_output.setText("The Button was Pressed" + "\n" + str(self.dungeon_diff.value()) + "\n" + str(self.wage_disp.value()))
        
        

    class Power():
        def __init__(self, bpower, loot = [], loot_val = {}):
            self.bpower = bpower
            print(str(self.bpower))
            self.loot = loot
            self.loot_val = loot_val
        def print_bp(self):
            print(str(self.bpower))
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
