# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from dialogue import Ui_Dialog
import subprocess


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.wrapper = 'cpp'
        self.cores = int(subprocess.getoutput("nproc"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 331, 71))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inputWrapperField = QtWidgets.QLineEdit(self.centralwidget)
        self.inputWrapperField.setGeometry(QtCore.QRect(40, 290, 511, 25))
        self.inputWrapperField.setReadOnly(True)
        self.inputWrapperField.setObjectName("inputWrapperField")
        self.inputVerilogButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputVerilogButton.setGeometry(QtCore.QRect(610, 200, 91, 25))
        self.inputVerilogButton.setObjectName("inputVerilogButton")
        self.outputField = QtWidgets.QLineEdit(self.centralwidget)
        self.outputField.setGeometry(QtCore.QRect(40, 340, 511, 25))
        self.outputField.setReadOnly(True)
        self.outputField.setObjectName("outputField")
        self.outputButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputButton.setGeometry(QtCore.QRect(610, 340, 91, 25))
        self.outputButton.setObjectName("outputButton")
        self.coreCount = QtWidgets.QSpinBox(self.centralwidget)
        self.coreCount.setGeometry(QtCore.QRect(500, 400, 51, 26))
        self.coreCount.setMinimum(1)
        self.coreCount.setMaximum(self.cores)
        self.coreCount.setValue(self.cores)
        self.coreCount.setObjectName("coreCount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 400, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.buildButton = QtWidgets.QPushButton(self.centralwidget)
        self.buildButton.setGeometry(QtCore.QRect(610, 500, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.buildButton.setFont(font)
        self.buildButton.setObjectName("buildButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(460, 500, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setItalic(True)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.inputVerilogField = QtWidgets.QLineEdit(self.centralwidget)
        self.inputVerilogField.setGeometry(QtCore.QRect(40, 200, 511, 25))
        self.inputVerilogField.setReadOnly(True)
        self.inputVerilogField.setObjectName("inputVerilogField")
        self.inputWrapperButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputWrapperButton.setGeometry(QtCore.QRect(610, 290, 91, 25))
        self.inputWrapperButton.setObjectName("inputWrapperButton")
        self.cppRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.cppRadioButton.setGeometry(QtCore.QRect(500, 250, 51, 23))
        self.cppRadioButton.setChecked(True)
        self.cppRadioButton.setObjectName("cppRadioButton")
        self.systemCRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.systemCRadioButton.setGeometry(QtCore.QRect(380, 250, 81, 23))
        self.systemCRadioButton.setObjectName("systemCRadioButton")
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
        MainWindow.setTabOrder(self.inputVerilogButton, self.inputWrapperButton)
        MainWindow.setTabOrder(self.inputWrapperButton, self.outputButton)
        MainWindow.setTabOrder(self.outputButton, self.coreCount)
        MainWindow.setTabOrder(self.coreCount, self.clearButton)
        MainWindow.setTabOrder(self.clearButton, self.buildButton)
        MainWindow.setTabOrder(self.buildButton, self.inputVerilogField)
        MainWindow.setTabOrder(self.inputVerilogField, self.inputWrapperField)
        MainWindow.setTabOrder(self.inputWrapperField, self.outputField)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Verilator GUI"))
        self.label.setText(_translate("MainWindow", "Verilator GUI"))
        self.inputWrapperField.setPlaceholderText(_translate("MainWindow", "Input C++ Wrapper"))
        self.inputVerilogButton.setText(_translate("MainWindow", "Input"))
        self.outputField.setPlaceholderText(_translate("MainWindow", "Output Directory"))
        self.outputButton.setText(_translate("MainWindow", "Output"))
        self.label_2.setText(_translate("MainWindow", "No. of cores"))
        self.buildButton.setText(_translate("MainWindow", "Build"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.inputVerilogField.setPlaceholderText(_translate("MainWindow", "Input Verilog file"))
        self.inputWrapperButton.setText(_translate("MainWindow", "Input"))
        self.cppRadioButton.setText(_translate("MainWindow", "C++"))
        self.systemCRadioButton.setText(_translate("MainWindow", "SystemC"))

        self.cppRadioButton.toggled.connect(lambda: self.cppRadioButtonClicked())
        self.systemCRadioButton.toggled.connect(lambda: self.systemCRadioButtonClicked())
        self.buildButton.clicked.connect(lambda: self.build())
        self.clearButton.clicked.connect(lambda: self.clearAll())
        self.inputVerilogButton.clicked.connect(lambda: self.getVerilogInputFile())
        self.inputWrapperButton.clicked.connect(lambda: self.getWrapperInputFile())
        self.outputButton.clicked.connect(lambda: self.setOutputDir())

    def cppRadioButtonClicked(self):
        self.inputWrapperField.setPlaceholderText("Input C++ Wrapper")
        self.wrapper = "cpp"

    def systemCRadioButtonClicked(self):
        self.inputWrapperField.setPlaceholderText("Input SystemC Wrapper")
        self.wrapper = "systemc"

    def getVerilogInputFile(self):
        fileTuple = QtWidgets.QFileDialog.getOpenFileName() # Returns a tuple with ('filename', 'Allfiles(*)')
        filename = fileTuple[0]
        self.inputVerilogField.setText(f"{filename}")

    def getWrapperInputFile(self):
        fileTuple = QtWidgets.QFileDialog.getOpenFileName()
        filename = fileTuple[0]
        self.inputWrapperField.setText(f"{filename}")

    def setOutputDir(self):
        dirName = QtWidgets.QFileDialog.getExistingDirectory()
        self.outputField.setText(f"{dirName}")

    def clearAll(self):
        self.inputVerilogField.setText("")
        self.inputWrapperField.setText("")
        self.outputField.setText("")
        self.coreCount.setValue(self.cores)
        self.cppRadioButton.setChecked(True)

    def openDialogueBox(self, text):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog(text)
        self.ui.setupUi(self.window)
        self.window.show()

    def build(self):
        inputFilename = self.inputVerilogField.text()
        outputDirName = self.outputField.text() + '/obj_dir'
        simFilename = self.inputWrapperField.text()
        wrapper = "cc" if self.wrapper == "cpp" else "sc"
        cores = self.coreCount.value()
        command = f"verilator --{wrapper} --exe --build -j {cores} -Wall {simFilename} {inputFilename} --Mdir {outputDirName}"

        commandExecOutput = subprocess.getoutput(command)
        self.openDialogueBox(commandExecOutput)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
