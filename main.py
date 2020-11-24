from multiprocessing.dummy import Pool
from random import randint
import random, os, sys, string
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import qCritical
from PyQt5.QtWidgets import QMessageBox
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.genned = 0
        self.current_cpm = 0
        self.generated_codes = 0
        self.to_generate_codes = 0
        self.cpm_ = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 562)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bigThingy = QtWidgets.QLabel(self.centralwidget)
        self.bigThingy.setGeometry(QtCore.QRect(40, 0, 731, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.bigThingy.setFont(font)
        self.bigThingy.setObjectName("bigThingy")
        self.stats = QtWidgets.QLabel(self.centralwidget)
        self.stats.setGeometry(QtCore.QRect(0, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stats.setFont(font)
        self.stats.setObjectName("stats")
        self.cpm = QtWidgets.QLabel(self.centralwidget)
        self.cpm.setGeometry(QtCore.QRect(0, 130, 701, 31))
        self.cpm.setObjectName("cpm")
        self.generated = QtWidgets.QLabel(self.centralwidget)
        self.generated.setGeometry(QtCore.QRect(0, 150, 701, 31))
        self.generated.setObjectName("generated")
        self.to_generate = QtWidgets.QLabel(self.centralwidget)
        self.to_generate.setGeometry(QtCore.QRect(0, 180, 701, 17))
        self.to_generate.setObjectName("to_generate")
        self.settings = QtWidgets.QLabel(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(0, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.settings.setFont(font)
        self.settings.setObjectName("settings")
        self.threads_label = QtWidgets.QLabel(self.centralwidget)
        self.threads_label.setGeometry(QtCore.QRect(0, 360, 67, 17))
        self.threads_label.setObjectName("threads_label")
        self.threads_input = QtWidgets.QLineEdit(self.centralwidget)
        self.threads_input.setGeometry(QtCore.QRect(70, 360, 113, 25))
        self.threads_input.setObjectName("threads_input")
        self.output_file_label = QtWidgets.QLabel(self.centralwidget)
        self.output_file_label.setGeometry(QtCore.QRect(0, 390, 91, 17))
        self.output_file_label.setObjectName("output_file_label")
        self.output_file_input = QtWidgets.QLineEdit(self.centralwidget)
        self.output_file_input.setGeometry(QtCore.QRect(90, 390, 113, 25))
        self.output_file_input.setObjectName("output_file_input")
        self.links = QtWidgets.QLabel(self.centralwidget)
        self.links.setGeometry(QtCore.QRect(710, 90, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.links.setFont(font)
        self.links.setObjectName("links")
        self.youtube = QtWidgets.QPushButton(self.centralwidget)
        self.youtube.setGeometry(QtCore.QRect(710, 140, 89, 25))
        self.youtube.setObjectName("youtube")
        self.github = QtWidgets.QPushButton(self.centralwidget)
        self.github.setGeometry(QtCore.QRect(710, 170, 89, 25))
        self.github.setObjectName("github")
        self.instagram = QtWidgets.QPushButton(self.centralwidget)
        self.instagram.setGeometry(QtCore.QRect(710, 200, 89, 25))
        self.instagram.setObjectName("instagram")
        self.twitter = QtWidgets.QPushButton(self.centralwidget)
        self.twitter.setGeometry(QtCore.QRect(710, 230, 89, 25))
        self.twitter.setObjectName("twitter")
        self.lawliet_host = QtWidgets.QPushButton(self.centralwidget)
        self.lawliet_host.setGeometry(QtCore.QRect(710, 260, 89, 25))
        self.lawliet_host.setObjectName("lawliet_host")
        self.discord = QtWidgets.QPushButton(self.centralwidget)
        self.discord.setGeometry(QtCore.QRect(710, 290, 89, 25))
        self.discord.setObjectName("discord")
        self.threads = QtWidgets.QCheckBox(self.centralwidget)
        self.threads.setGeometry(QtCore.QRect(0, 270, 92, 23))
        self.threads.setObjectName("threads")
        self.extra_fast = QtWidgets.QCheckBox(self.centralwidget)
        self.extra_fast.setGeometry(QtCore.QRect(0, 300, 92, 23))
        self.extra_fast.setObjectName("extra_fast")
        self.codes_to_generate = QtWidgets.QLabel(self.centralwidget)
        self.codes_to_generate.setGeometry(QtCore.QRect(0, 420, 151, 17))
        self.codes_to_generate.setObjectName("codes_to_generate")
        self.codes_to_generate_input = QtWidgets.QLineEdit(self.centralwidget)
        self.codes_to_generate_input.setGeometry(QtCore.QRect(140, 420, 113, 25))
        self.codes_to_generate_input.setObjectName("codes_to_generate_input")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 480, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.debuggingMode = QtWidgets.QCheckBox(self.centralwidget)
        self.debuggingMode.setGeometry(QtCore.QRect(0, 330, 141, 23))
        self.debuggingMode.setObjectName("debuggingMode")
        self.saveCodesAs = QtWidgets.QLabel(self.centralwidget)
        self.saveCodesAs.setGeometry(QtCore.QRect(0, 450, 121, 17))
        self.saveCodesAs.setObjectName("saveCodesAs")
        self.saveAs1 = QtWidgets.QRadioButton(self.centralwidget)
        self.saveAs1.setGeometry(QtCore.QRect(0, 470, 181, 23))
        self.saveAs1.setObjectName("saveAs1")
        self.saveAs2 = QtWidgets.QRadioButton(self.centralwidget)
        self.saveAs2.setGeometry(QtCore.QRect(0, 490, 112, 23))
        self.saveAs2.setObjectName("saveAs2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ez Nitro"))
        self.bigThingy.setText(_translate("MainWindow", "Discord Nitro Generator - By MysteriousK#0420"))
        self.stats.setText(_translate("MainWindow", "Stats"))
        self.cpm.setText(_translate("MainWindow", "CPM: "))
        self.generated.setText(_translate("MainWindow", "Generated:"))
        self.to_generate.setText(_translate("MainWindow", "To Generate: "))
        self.settings.setText(_translate("MainWindow", "Settings"))
        self.threads_label.setText(_translate("MainWindow", "Threads:"))
        self.output_file_label.setText(_translate("MainWindow", "Output File:"))
        self.links.setText(_translate("MainWindow", "Links"))
        self.youtube.setText(_translate("MainWindow", "YouTube"))
        self.github.setText(_translate("MainWindow", "GitHub"))
        self.instagram.setText(_translate("MainWindow", "Instagram"))
        self.twitter.setText(_translate("MainWindow", "Twitter"))
        self.lawliet_host.setText(_translate("MainWindow", "Lawliet Host"))
        self.discord.setText(_translate("MainWindow", "Discord"))
        self.threads.setText(_translate("MainWindow", "Threads"))
        self.extra_fast.setText(_translate("MainWindow", "Extra Fast"))
        self.codes_to_generate.setText(_translate("MainWindow", "Codes To Generate:"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.debuggingMode.setText(_translate("MainWindow", "Debugging Mode"))
        self.saveCodesAs.setText(_translate("MainWindow", "Save Codes As:"))
        self.saveAs1.setText(_translate("MainWindow", "discord.gift/code_here"))
        self.saveAs2.setText(_translate("MainWindow", "code_here"))
        self.pushButton.clicked.connect(self.start)
        self.youtube.clicked.connect(self.yt)
        self.github.clicked.connect(self.git)
        self.instagram.clicked.connect(self.ig)
        self.twitter.clicked.connect(self.twit)
        self.lawliet_host.clicked.connect(self.lh)
        self.discord.clicked.connect(self.dc)
    def yt(self):
        webbrowser.open("https://youtube.com/c/MysteriousK69")
    def git(self):
        webbrowser.open('https://github.com/MysteriousK69')
    def ig(self):
        webbrowser.open('https://instagram.com/@mysteriousk8116')
    def twit(self):
        webbrowser.open("https://twitter.com/MysteriousK17")
    def lh(self):
        webbrowser.open("https://panel.lawliethost.com")
    def dc(self):
        webbrowser.open("https://discord.gg/cDmSw63wE8")
    def update_stats(self):
        self.current_cpm = randint(self.current_cpm,self.current_cpm+20)
        self.cpm_ = self.current_cpm
        self.cpm.setText("CPM: {}".format(self.cpm_*60))
        self.generated.setText("Generated: {}".format(self.generated_codes))
        self.to_generate.setText("To Generate: {}".format(self.to_generate_codes))
        self.current_cpm = 0
    def start(self):
        if self.extra_fast.isChecked() and self.threads.isChecked():
            threadamt = int(self.threads_input.text())
            to_generate_codes = self.codes_to_generate_input.text()
            threads_to_use = threadamt+100
            uwu = Pool(threads_to_use)
            uwu.map(self.generator,to_generate_codes)
        elif self.extra_fast.isChecked():
            to_generate_codes = self.codes_to_generate_input.text()
            uwu = Pool(100)
            uwu.map(self.generator,to_generate_codes)
        elif self.threads.isChecked():
            threadamt = self.threads_input.text()
            to_generate_codes = self.codes_to_generate_input.text()
            uwu = Pool(int(threadamt))
            uwu.map(self.generator,to_generate_codes)
        else:
            to_generate_codes = self.codes_to_generate_input.text()
            self.generator(to_generate_codes)
            
    def generator(self,togen:int):
        togen = self.codes_to_generate_input.text()
        output_file_name = self.output_file_input.text()
        debug = self.debuggingMode.isChecked()
        if debug:
            try:
                with open(output_file_name,'a') as f:
                    while True:
                        if int(self.genned) <= int(togen):
                            code = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(16))
                            if self.saveAs1.isChecked():
                                f.write('discord.gift/'+code+'\n')
                            elif self.saveAs2.isChecked():
                                f.write(code+'\n')
                            else:
                                f.write('discord.gift/'+code+'\n')
                            self.current_cpm += 1
                            self.generated_codes += 1
                            self.to_generate_codes -= 1
                            self.genned += 1
                            self.update_stats()
                        elif int(self.genned) >= int(togen):
                            self.current_cpm = randint(self.current_cpm,self.current_cpm+20)
                            self.cpm_ = self.current_cpm
                            self.cpm.setText("CPM: {}".format(self.cpm_*60))
                            self.generated.setText("Generated: {}".format(self.generated_codes))
                            self.to_generate.setText("To Generate: 0")
                            self.current_cpm = 0
                            break
            except:
                bawks = QMessageBox()
                bawks.setWindowTitle("Error!")
                bawks.setText('BRUH u probs just entered a string instead of integer or something smh')
                bawks.setIcon(QMessageBox.Critical)
                bawks.exec_()
        else:
            try:
                with open(output_file_name,'a') as f:
                    while True:
                        if int(self.genned) <= int(togen):
                            code = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(16))
                            f.write(code+'\n')

                            self.current_cpm += 1
                            self.generated_codes += 1
                            self.to_generate_codes -= 1
                            self.genned += 1
                            self.update_stats()
                        elif int(self.genned) >= int(togen):
                            self.current_cpm = randint(self.current_cpm,self.current_cpm+20)
                            self.cpm_ = self.current_cpm
                            self.cpm.setText("CPM: {}".format(self.cpm_*60))
                            self.generated.setText("Generated: {}".format(self.generated_codes))
                            self.to_generate.setText("To Generate: 0")
                            self.current_cpm = 0
                            break
            except:
                pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())