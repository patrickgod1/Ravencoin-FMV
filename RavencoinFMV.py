import datetime
import os.path
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QMessageBox
import sys


class Ui_mainWindow(object):
    def __init__(self):
        self.cwd = os.path.dirname(os.path.abspath(__file__))
        self.exportPath = ''
        self.savePath = ''
        self.forceDL = False
        self.today = datetime.datetime.utcnow().strftime('%Y%m%d')

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.setEnabled(True)
        mainWindow.resize(490, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(490, 200))
        mainWindow.setBaseSize(QtCore.QSize(490, 400))
        self.mainWindowLayout = QtWidgets.QVBoxLayout(mainWindow)
        self.mainWindowLayout.setObjectName("mainWindowLayout")
        self.userInputLayout = QtWidgets.QWidget(mainWindow)
        self.userInputLayout.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userInputLayout.sizePolicy().hasHeightForWidth())
        self.userInputLayout.setSizePolicy(sizePolicy)
        self.userInputLayout.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.userInputLayout.setFont(font)
        self.userInputLayout.setObjectName("userInputLayout")
        self.createSignsBoxLayout = QtWidgets.QVBoxLayout(self.userInputLayout)
        self.createSignsBoxLayout.setObjectName("createSignsBoxLayout")
        self.exportLayout = QtWidgets.QHBoxLayout()
        self.exportLayout.setObjectName("exportLayout")
        self.exportLabel = QtWidgets.QLabel(self.userInputLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportLabel.sizePolicy().hasHeightForWidth())
        self.exportLabel.setSizePolicy(sizePolicy)
        self.exportLabel.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.exportLabel.setFont(font)
        self.exportLabel.setObjectName("exportLabel")
        self.exportLayout.addWidget(self.exportLabel)
        self.selectExport = QtWidgets.QLineEdit(self.userInputLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectExport.sizePolicy().hasHeightForWidth())
        self.selectExport.setSizePolicy(sizePolicy)
        self.selectExport.setMinimumSize(QtCore.QSize(179, 29))
        self.selectExport.setDragEnabled(False)
        self.selectExport.setReadOnly(True)
        self.selectExport.setObjectName("selectExport")
        self.exportLayout.addWidget(self.selectExport)
        self.browseExportButton = QtWidgets.QPushButton(self.userInputLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseExportButton.sizePolicy().hasHeightForWidth())
        self.browseExportButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.browseExportButton.setFont(font)
        self.browseExportButton.setObjectName("browseExportButton")
        self.exportLayout.addWidget(self.browseExportButton)
        self.createSignsBoxLayout.addLayout(self.exportLayout)
        self.saveReportPathLayout = QtWidgets.QHBoxLayout()
        self.saveReportPathLayout.setObjectName("saveReportPathLayout")
        self.saveReportPathLabel = QtWidgets.QLabel(self.userInputLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveReportPathLabel.sizePolicy().hasHeightForWidth())
        self.saveReportPathLabel.setSizePolicy(sizePolicy)
        self.saveReportPathLabel.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.saveReportPathLabel.setFont(font)
        self.saveReportPathLabel.setObjectName("saveReportPathLabel")
        self.saveReportPathLayout.addWidget(self.saveReportPathLabel)
        self.selectSaveReportPath = QtWidgets.QLineEdit(self.userInputLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectSaveReportPath.sizePolicy().hasHeightForWidth())
        self.selectSaveReportPath.setSizePolicy(sizePolicy)
        self.selectSaveReportPath.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.selectSaveReportPath.setFont(font)
        self.selectSaveReportPath.setText("")
        self.selectSaveReportPath.setReadOnly(True)
        self.selectSaveReportPath.setObjectName("selectSaveReportPath")
        self.saveReportPathLayout.addWidget(self.selectSaveReportPath)
        self.browseSaveReportButton = QtWidgets.QToolButton(self.userInputLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseSaveReportButton.sizePolicy().hasHeightForWidth())
        self.browseSaveReportButton.setSizePolicy(sizePolicy)
        self.browseSaveReportButton.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.browseSaveReportButton.setFont(font)
        self.browseSaveReportButton.setCheckable(False)
        self.browseSaveReportButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.browseSaveReportButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.browseSaveReportButton.setObjectName("browseSaveReportButton")
        self.saveReportPathLayout.addWidget(self.browseSaveReportButton)
        self.createSignsBoxLayout.addLayout(self.saveReportPathLayout)
        self.downloadLayout = QtWidgets.QHBoxLayout()
        self.downloadLayout.setContentsMargins(8, 0, -1, 0)
        self.downloadLayout.setSpacing(12)
        self.downloadLayout.setObjectName("downloadLayout")
        self.downloadCheckbox = QtWidgets.QCheckBox(self.userInputLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadCheckbox.sizePolicy().hasHeightForWidth())
        self.downloadCheckbox.setSizePolicy(sizePolicy)
        self.downloadCheckbox.setMinimumSize(QtCore.QSize(180, 20))
        self.downloadCheckbox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.downloadCheckbox.setFont(font)
        self.downloadCheckbox.setChecked(False)
        self.downloadCheckbox.setObjectName("downloadCheckbox")
        self.downloadLayout.addWidget(self.downloadCheckbox)
        self.createSignsBoxLayout.addLayout(self.downloadLayout)
        self.mainWindowLayout.addWidget(self.userInputLayout)
        self.startExitLayout = QtWidgets.QHBoxLayout()
        self.startExitLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.startExitLayout.setObjectName("startExitLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.startExitLayout.addItem(spacerItem)
        self.StartButton = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setMinimumSize(QtCore.QSize(175, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.startExitLayout.addWidget(self.StartButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.startExitLayout.addItem(spacerItem1)
        self.exitButton = QtWidgets.QPushButton(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QtCore.QSize(175, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.startExitLayout.addWidget(self.exitButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.startExitLayout.addItem(spacerItem2)
        self.mainWindowLayout.addLayout(self.startExitLayout)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "RavencoinFMV"))
        self.exportLabel.setText(_translate("mainWindow", "Wallet Export File:"))
        self.browseExportButton.setText(_translate("mainWindow", "Browse"))
        self.saveReportPathLabel.setText(_translate("mainWindow", "Save Path:"))
        self.browseSaveReportButton.setText(_translate("mainWindow", "Browse"))
        self.downloadCheckbox.setText(_translate("mainWindow", "Force Download Historical Data"))
        self.StartButton.setText(_translate("mainWindow", "Start"))
        self.exitButton.setText(_translate("mainWindow", "Exit"))

        self.browseExportButton.clicked.connect(self.setExportPath)
        self.browseSaveReportButton.clicked.connect(self.setSavePath)
        self.downloadCheckbox.toggled.connect(self.downloadState)
        self.exitButton.clicked.connect(self.exitApp)
        self.StartButton.clicked.connect(self.startApp)

    def setExportPath(self):
        self.exportPath, _ = QFileDialog.getOpenFileName(None, "Select Wallet Transactions Export File", "", "Comma-separated Value (*.csv)")
        self.selectExport.setText(self.exportPath)

    def setSavePath(self):
        self.savePath = QFileDialog.getExistingDirectory(None, 'Save Report to')
        self.selectSaveReportPath.setText(self.savePath)

    def downloadState(self):
        if self.downloadCheckbox.isChecked():
            self.forceDL = True
        else:
            self.forceDL = False

    def exitApp(self):
        reply = QMessageBox.question(None, 'Exit', "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def startApp(self):
        if self.exportPath == '':
            QMessageBox.warning(None, 'No wallet transactons export file found!!!', "Please export you wallet transactions first. Then select the (.csv) file.")
            return
        elif self.savePath == '':
            QMessageBox.warning(None, 'No save path selected.', "Please select where to save the results.")
            return
        if self.forceDL == True:
            self.updateHistoricalData()
        if self.calcAssets():
            QMessageBox.information(None, 'Done', f'Done. Please review capitalAsset.csv and yearlySummary.csv in {self.savePath}')
        else:
            QMessageBox.critical(None, 'Error', f'Error!!! Something went wrong. Please contact developer(s) with specific instructions on how to reproduce error state. Thanks.')

    def updateHistoricalData(self):
        url = f"https://coinmarketcap.com/currencies/ravencoin/historical-data/?start=20130428&end={self.today}"
        historical = pd.read_html(url, parse_dates=['Date'])[0]
        historical.to_csv(f'{self.cwd}\\historicalData.csv')

    def calcAssets(self):
        if os.path.isfile(f'{self.cwd}\\historicalData.csv'):
            historical = pd.read_csv(f'{self.cwd}\\historicalData.csv', parse_dates=['Date'])
            if(historical.iloc[0]['Date'] < datetime.datetime.strptime(self.today, '%Y%m%d')):
                self.updateHistoricalData()
        else:
            self.updateHistoricalData()

        export = pd.read_csv(self.exportPath, usecols=['Date', 'Type', 'Label', 'Amount (RVN)'], parse_dates=['Date'])
        export['Date'] = pd.to_datetime(export['Date'].dt.strftime('%Y-%m-%d'), format='%Y-%m-%d')

        export = pd.merge(left=export, right=historical[['Date', 'Close**']], how='left', on=['Date'])
        export['Capital Asset (USD)'] = export['Amount (RVN)'] * export['Close**']
        export.rename(columns={'Close**': 'FMV (USD)'}, inplace=True)
        export = export.iloc[::-1].reset_index(drop=True)
        export.to_csv(f'{self.savePath}\\capitalAsset.csv')

        yearlySummary = export[['Date', 'Type', 'Label', 'Amount (RVN)', 'Capital Asset (USD)']].groupby(export['Date'].dt.strftime('%Y')).sum()
        yearlySummary.index.names = ['Year']
        yearlySummary.to_csv(f'{self.savePath}\\yearlySummary.csv')
        # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        #     print(yearlySummary)
        return 1


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QWidget()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
