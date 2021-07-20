
from PyQt5 import QtCore, QtGui, QtWidgets
import converter
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
    	#adding objects and setting their widgets↓↓↓
        MainWindow.setObjectName("python currency converter")
        MainWindow.setFixedSize(736, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.arrow_label = QtWidgets.QLabel(self.centralwidget)
        self.arrow_label.setGeometry(QtCore.QRect(330, 30, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(43)
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        font3 = QtGui.QFont()
        font3.setPointSize(15)
        self.arrow_label.setFont(font)
        self.arrow_label.setObjectName("arrow_label")
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(300, 150, 101, 61))
        self.convert_button.setFont(font3)
        self.convert_button.setObjectName("convert_button")
        self.amount_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.amount_textedit.setGeometry(QtCore.QRect(310, 100, 81, 41))
        self.amount_textedit.setObjectName("amount_textedit")
        self.answer_label = QtWidgets.QLabel(self.centralwidget)
        self.answer_label.setGeometry(QtCore.QRect(10, 240, 691, 51))
        self.answer_label.setFont(font3)
        self.answer_label.setText("")
        self.answer_label.setObjectName("answer_label")
        self.from_currency_box = QtWidgets.QComboBox(self.centralwidget)
        self.from_currency_box.setGeometry(QtCore.QRect(50, 50, 191, 51))
        self.from_currency_box.setObjectName("from_currency_box")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.from_currency_box.addItem("")
        self.to_currency_box = QtWidgets.QComboBox(self.centralwidget)
        self.to_currency_box.setGeometry(QtCore.QRect(450, 50, 191, 51))
        self.to_currency_box.setObjectName("to_currency_box")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.to_currency_box.addItem("")
        self.from_currency_box.setFont(font2)
        self.to_currency_box.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.convert_button.clicked.connect(self.press)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.arrow_label.setText(_translate("MainWindow", "→"))
        self.convert_button.setText(_translate("MainWindow", "convert"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.jpeg"))
        self.convert_button.setStyleSheet("background-color: darkgray")
        #setting texts and background colors of combo boxes↓↓↓
        self.from_currency_box.setStyleSheet("background-color: gray")
        self.from_currency_box.setItemText(0, _translate("MainWindow", "United States Dollar"))
        self.from_currency_box.setItemText(1, _translate("MainWindow", "Afghan Afghani"))
        self.from_currency_box.setItemText(2, _translate("MainWindow", "Albanian Lek"))
        self.from_currency_box.setItemText(3, _translate("MainWindow", "Algerian Dinar"))
        self.from_currency_box.setItemText(4, _translate("MainWindow", "Angolan Kwanza"))
        self.from_currency_box.setItemText(5, _translate("MainWindow", "Argentine Peso"))
        self.from_currency_box.setItemText(6, _translate("MainWindow", "Armenian Dram"))
        self.from_currency_box.setItemText(7, _translate("MainWindow", "Aruban Florin"))
        self.from_currency_box.setItemText(8, _translate("MainWindow", "Australian Dollar"))
        self.from_currency_box.setItemText(9, _translate("MainWindow", "Azerbaijani Manat"))
        self.from_currency_box.setItemText(10, _translate("MainWindow", "Bahamian Dollar"))
        self.from_currency_box.setItemText(11, _translate("MainWindow", "Bahraini Dinar"))
        self.from_currency_box.setItemText(12, _translate("MainWindow", "Bajan dollar"))
        self.from_currency_box.setItemText(13, _translate("MainWindow", "Bangladeshi Taka"))
        self.from_currency_box.setItemText(14, _translate("MainWindow", "Belarusian Ruble"))
        self.from_currency_box.setItemText(15, _translate("MainWindow", "Belize Dollar"))
        self.from_currency_box.setItemText(16, _translate("MainWindow", "Bermudan Dollar"))
        self.from_currency_box.setItemText(17, _translate("MainWindow", "Bhutan currency"))
        self.from_currency_box.setItemText(18, _translate("MainWindow", "Bitcoin"))
        self.from_currency_box.setItemText(19, _translate("MainWindow", "Bitcoin Cash"))
        self.from_currency_box.setItemText(20, _translate("MainWindow", "Bolivian Boliviano"))
        self.from_currency_box.setItemText(21, _translate("MainWindow", "Bosnia-Herzegovina Convertible Mark"))
        self.from_currency_box.setItemText(22, _translate("MainWindow", "Botswanan Pula"))
        self.from_currency_box.setItemText(23, _translate("MainWindow", "Brazilian Real"))
        self.from_currency_box.setItemText(24, _translate("MainWindow", "Brunei Dollar"))
        self.from_currency_box.setItemText(25, _translate("MainWindow", "Bulgarian Lev"))
        self.from_currency_box.setItemText(26, _translate("MainWindow", "Burundian Franc"))
        self.from_currency_box.setItemText(27, _translate("MainWindow", "CFP Franc"))
        self.from_currency_box.setItemText(28, _translate("MainWindow", "Cambodian riel"))
        self.from_currency_box.setItemText(29, _translate("MainWindow", "Canadian Dollar"))
        self.from_currency_box.setItemText(30, _translate("MainWindow", "Cape Verdean Escudo"))
        self.from_currency_box.setItemText(31, _translate("MainWindow", "Cayman Islands Dollar"))
        self.from_currency_box.setItemText(32, _translate("MainWindow", "Central African CFA franc"))
        self.from_currency_box.setItemText(33, _translate("MainWindow", "Chilean Peso"))
        self.from_currency_box.setItemText(34, _translate("MainWindow", "Chilean Unit of Account (UF)"))
        self.from_currency_box.setItemText(35, _translate("MainWindow", "Chinese Yuan"))
        self.from_currency_box.setItemText(36, _translate("MainWindow", "Chinese Yuan (offshore)"))
        self.from_currency_box.setItemText(37, _translate("MainWindow", "Colombian Peso"))
        self.from_currency_box.setItemText(38, _translate("MainWindow", "Comorian franc"))
        self.from_currency_box.setItemText(39, _translate("MainWindow", "Congolese Franc"))
        self.from_currency_box.setItemText(40, _translate("MainWindow", "Costa Rican Colón"))
        self.from_currency_box.setItemText(41, _translate("MainWindow", "Croatian Kuna"))
        self.from_currency_box.setItemText(42, _translate("MainWindow", "Cuban Peso"))
        self.from_currency_box.setItemText(43, _translate("MainWindow", "Czech Koruna"))
        self.from_currency_box.setItemText(44, _translate("MainWindow", "Danish Krone"))
        self.from_currency_box.setItemText(45, _translate("MainWindow", "Djiboutian Franc"))
        self.from_currency_box.setItemText(46, _translate("MainWindow", "Dominican Peso"))
        self.from_currency_box.setItemText(47, _translate("MainWindow", "East Caribbean Dollar"))
        self.from_currency_box.setItemText(48, _translate("MainWindow", "Egyptian Pound"))
        self.from_currency_box.setItemText(49, _translate("MainWindow", "Ether"))
        self.from_currency_box.setItemText(50, _translate("MainWindow", "Ethiopian Birr"))
        self.from_currency_box.setItemText(51, _translate("MainWindow", "Euro"))
        self.from_currency_box.setItemText(52, _translate("MainWindow", "Fijian Dollar"))
        self.from_currency_box.setItemText(53, _translate("MainWindow", "Gambian dalasi"))
        self.from_currency_box.setItemText(54, _translate("MainWindow", "Georgian Lari"))
        self.from_currency_box.setItemText(55, _translate("MainWindow", "Ghanaian Cedi"))
        self.from_currency_box.setItemText(56, _translate("MainWindow", "Gibraltar Pound"))
        self.from_currency_box.setItemText(57, _translate("MainWindow", "Guatemalan Quetzal"))
        self.from_currency_box.setItemText(58, _translate("MainWindow", "Guinean Franc"))
        self.from_currency_box.setItemText(59, _translate("MainWindow", "Guyanaese Dollar"))
        self.from_currency_box.setItemText(60, _translate("MainWindow", "Haitian Gourde"))
        self.from_currency_box.setItemText(61, _translate("MainWindow", "Honduran Lempira"))
        self.from_currency_box.setItemText(62, _translate("MainWindow", "Hong Kong Dollar"))
        self.from_currency_box.setItemText(63, _translate("MainWindow", "Hungarian Forint"))
        self.from_currency_box.setItemText(64, _translate("MainWindow", "Icelandic Króna"))
        self.from_currency_box.setItemText(65, _translate("MainWindow", "Indian Rupee"))
        self.from_currency_box.setItemText(66, _translate("MainWindow", "Indonesian Rupiah"))
        self.from_currency_box.setItemText(67, _translate("MainWindow", "Iranian Rial"))
        self.from_currency_box.setItemText(68, _translate("MainWindow", "Iraqi Dinar"))
        self.from_currency_box.setItemText(69, _translate("MainWindow", "Israeli New Shekel"))
        self.from_currency_box.setItemText(70, _translate("MainWindow", "Jamaican Dollar"))
        self.from_currency_box.setItemText(71, _translate("MainWindow", "Japanese Yen"))
        self.from_currency_box.setItemText(72, _translate("MainWindow", "Jordanian Dinar"))
        self.from_currency_box.setItemText(73, _translate("MainWindow", "Kazakhstani Tenge"))
        self.from_currency_box.setItemText(74, _translate("MainWindow", "Kenyan Shilling"))
        self.from_currency_box.setItemText(75, _translate("MainWindow", "Kuwaiti Dinar"))
        self.from_currency_box.setItemText(76, _translate("MainWindow", "Kyrgystani Som"))
        self.from_currency_box.setItemText(77, _translate("MainWindow", "Laotian Kip"))
        self.from_currency_box.setItemText(78, _translate("MainWindow", "Lebanese pound"))
        self.from_currency_box.setItemText(79, _translate("MainWindow", "Lesotho loti"))
        self.from_currency_box.setItemText(80, _translate("MainWindow", "Liberian Dollar"))
        self.from_currency_box.setItemText(81, _translate("MainWindow", "Libyan Dinar"))
        self.from_currency_box.setItemText(82, _translate("MainWindow", "Litecoin"))
        self.from_currency_box.setItemText(83, _translate("MainWindow", "Macanese Pataca"))
        self.from_currency_box.setItemText(84, _translate("MainWindow", "Macedonian Denar"))
        self.from_currency_box.setItemText(85, _translate("MainWindow", "Malagasy Ariary"))
        self.from_currency_box.setItemText(86, _translate("MainWindow", "Malawian Kwacha"))
        self.from_currency_box.setItemText(87, _translate("MainWindow", "Malaysian Ringgit"))
        self.from_currency_box.setItemText(88, _translate("MainWindow", "Maldivian Rufiyaa"))
        self.from_currency_box.setItemText(89, _translate("MainWindow", "Mauritanian Ouguiya (1973–2017)"))
        self.from_currency_box.setItemText(90, _translate("MainWindow", "Mauritian Rupee"))
        self.from_currency_box.setItemText(91, _translate("MainWindow", "Mexican Peso"))
        self.from_currency_box.setItemText(92, _translate("MainWindow", "Moldovan Leu"))
        self.from_currency_box.setItemText(93, _translate("MainWindow", "Moroccan Dirham"))
        self.from_currency_box.setItemText(94, _translate("MainWindow", "Mozambican metical"))
        self.from_currency_box.setItemText(95, _translate("MainWindow", "Myanmar Kyat"))
        self.from_currency_box.setItemText(96, _translate("MainWindow", "NT$"))
        self.from_currency_box.setItemText(97, _translate("MainWindow", "Namibian dollar"))
        self.from_currency_box.setItemText(98, _translate("MainWindow", "Nepalese Rupee"))
        self.from_currency_box.setItemText(99, _translate("MainWindow", "Netherlands Antillean Guilder"))
        self.from_currency_box.setItemText(100, _translate("MainWindow", "New Zealand Dollar"))
        self.from_currency_box.setItemText(101, _translate("MainWindow", "Nicaraguan Córdoba"))
        self.from_currency_box.setItemText(102, _translate("MainWindow", "Nigerian Naira"))
        self.from_currency_box.setItemText(103, _translate("MainWindow", "Norwegian Krone"))
        self.from_currency_box.setItemText(104, _translate("MainWindow", "Omani Rial"))
        self.from_currency_box.setItemText(105, _translate("MainWindow", "Pakistani Rupee"))
        self.from_currency_box.setItemText(106, _translate("MainWindow", "Panamanian Balboa"))
        self.from_currency_box.setItemText(107, _translate("MainWindow", "Papua New Guinean Kina"))
        self.from_currency_box.setItemText(108, _translate("MainWindow", "Paraguayan Guarani"))
        self.from_currency_box.setItemText(109, _translate("MainWindow", "Philippine Piso"))
        self.from_currency_box.setItemText(110, _translate("MainWindow", "Poland złoty"))
        self.from_currency_box.setItemText(111, _translate("MainWindow", "Pound sterling"))
        self.from_currency_box.setItemText(112, _translate("MainWindow", "Qatari Rial"))
        self.from_currency_box.setItemText(113, _translate("MainWindow", "Romanian Leu"))
        self.from_currency_box.setItemText(114, _translate("MainWindow", "Russian Ruble"))
        self.from_currency_box.setItemText(115, _translate("MainWindow", "Rwandan franc"))
        self.from_currency_box.setItemText(116, _translate("MainWindow", "Salvadoran Colón"))
        self.from_currency_box.setItemText(117, _translate("MainWindow", "Saudi Riyal"))
        self.from_currency_box.setItemText(118, _translate("MainWindow", "Serbian Dinar"))
        self.from_currency_box.setItemText(119, _translate("MainWindow", "Seychellois Rupee"))
        self.from_currency_box.setItemText(120, _translate("MainWindow", "Sierra Leonean Leone"))
        self.from_currency_box.setItemText(121, _translate("MainWindow", "Singapore Dollar"))
        self.from_currency_box.setItemText(122, _translate("MainWindow", "Sol"))
        self.from_currency_box.setItemText(123, _translate("MainWindow", "Solomon Islands Dollar"))
        self.from_currency_box.setItemText(124, _translate("MainWindow", "Somali Shilling"))
        self.from_currency_box.setItemText(125, _translate("MainWindow", "South African Rand"))
        self.from_currency_box.setItemText(126, _translate("MainWindow", "South Korean won"))
        self.from_currency_box.setItemText(127, _translate("MainWindow", "Sovereign Bolivar"))
        self.from_currency_box.setItemText(128, _translate("MainWindow", "Special Drawing Rights"))
        self.from_currency_box.setItemText(129, _translate("MainWindow", "Sri Lankan Rupee"))
        self.from_currency_box.setItemText(130, _translate("MainWindow", "Sudanese pound"))
        self.from_currency_box.setItemText(131, _translate("MainWindow", "Surinamese Dollar"))
        self.from_currency_box.setItemText(132, _translate("MainWindow", "Swazi Lilangeni"))
        self.from_currency_box.setItemText(133, _translate("MainWindow", "Swedish Krona"))
        self.from_currency_box.setItemText(134, _translate("MainWindow", "Swiss Franc"))
        self.from_currency_box.setItemText(135, _translate("MainWindow", "Tajikistani Somoni"))
        self.from_currency_box.setItemText(136, _translate("MainWindow", "Tanzanian Shilling"))
        self.from_currency_box.setItemText(137, _translate("MainWindow", "Thai Baht"))
        self.from_currency_box.setItemText(138, _translate("MainWindow", "Tongan Paʻanga"))
        self.from_currency_box.setItemText(139, _translate("MainWindow", "Trinidad & Tobago Dollar"))
        self.from_currency_box.setItemText(140, _translate("MainWindow", "Tunisian Dinar"))
        self.from_currency_box.setItemText(141, _translate("MainWindow", "Turkish lira"))
        self.from_currency_box.setItemText(142, _translate("MainWindow", "Turkmenistan manat"))
        self.from_currency_box.setItemText(143, _translate("MainWindow", "Ugandan Shilling"))
        self.from_currency_box.setItemText(144, _translate("MainWindow", "Ukrainian hryvnia"))
        self.from_currency_box.setItemText(145, _translate("MainWindow", "United Arab Emirates Dirham"))
        self.from_currency_box.setItemText(146, _translate("MainWindow", "Uruguayan Peso"))
        self.from_currency_box.setItemText(147, _translate("MainWindow", "Uzbekistani Som"))
        self.from_currency_box.setItemText(148, _translate("MainWindow", "Vietnamese dong"))
        self.from_currency_box.setItemText(149, _translate("MainWindow", "West African CFA franc"))
        self.from_currency_box.setItemText(150, _translate("MainWindow", "Yemeni Rial"))
        self.from_currency_box.setItemText(151, _translate("MainWindow", "Zambian Kwacha"))
        self.to_currency_box.setStyleSheet("background-color: gray")
        self.to_currency_box.setItemText(0, _translate("MainWindow", "United States Dollar"))
        self.to_currency_box.setItemText(1, _translate("MainWindow", "Afghan Afghani"))
        self.to_currency_box.setItemText(2, _translate("MainWindow", "Albanian Lek"))
        self.to_currency_box.setItemText(3, _translate("MainWindow", "Algerian Dinar"))
        self.to_currency_box.setItemText(4, _translate("MainWindow", "Angolan Kwanza"))
        self.to_currency_box.setItemText(5, _translate("MainWindow", "Argentine Peso"))
        self.to_currency_box.setItemText(6, _translate("MainWindow", "Armenian Dram"))
        self.to_currency_box.setItemText(7, _translate("MainWindow", "Aruban Florin"))
        self.to_currency_box.setItemText(8, _translate("MainWindow", "Australian Dollar"))
        self.to_currency_box.setItemText(9, _translate("MainWindow", "Azerbaijani Manat"))
        self.to_currency_box.setItemText(10, _translate("MainWindow", "Bahamian Dollar"))
        self.to_currency_box.setItemText(11, _translate("MainWindow", "Bahraini Dinar"))
        self.to_currency_box.setItemText(12, _translate("MainWindow", "Bajan dollar"))
        self.to_currency_box.setItemText(13, _translate("MainWindow", "Bangladeshi Taka"))
        self.to_currency_box.setItemText(14, _translate("MainWindow", "Belarusian Ruble"))
        self.to_currency_box.setItemText(15, _translate("MainWindow", "Belize Dollar"))
        self.to_currency_box.setItemText(16, _translate("MainWindow", "Bermudan Dollar"))
        self.to_currency_box.setItemText(17, _translate("MainWindow", "Bhutan currency"))
        self.to_currency_box.setItemText(18, _translate("MainWindow", "Bitcoin"))
        self.to_currency_box.setItemText(19, _translate("MainWindow", "Bitcoin Cash"))
        self.to_currency_box.setItemText(20, _translate("MainWindow", "Bolivian Boliviano"))
        self.to_currency_box.setItemText(21, _translate("MainWindow", "Bosnia-Herzegovina Convertible Mark"))
        self.to_currency_box.setItemText(22, _translate("MainWindow", "Botswanan Pula"))
        self.to_currency_box.setItemText(23, _translate("MainWindow", "Brazilian Real"))
        self.to_currency_box.setItemText(24, _translate("MainWindow", "Brunei Dollar"))
        self.to_currency_box.setItemText(25, _translate("MainWindow", "Bulgarian Lev"))
        self.to_currency_box.setItemText(26, _translate("MainWindow", "Burundian Franc"))
        self.to_currency_box.setItemText(27, _translate("MainWindow", "CFP Franc"))
        self.to_currency_box.setItemText(28, _translate("MainWindow", "Cambodian riel"))
        self.to_currency_box.setItemText(29, _translate("MainWindow", "Canadian Dollar"))
        self.to_currency_box.setItemText(30, _translate("MainWindow", "Cape Verdean Escudo"))
        self.to_currency_box.setItemText(31, _translate("MainWindow", "Cayman Islands Dollar"))
        self.to_currency_box.setItemText(32, _translate("MainWindow", "Central African CFA franc"))
        self.to_currency_box.setItemText(33, _translate("MainWindow", "Chilean Peso"))
        self.to_currency_box.setItemText(34, _translate("MainWindow", "Chilean Unit of Account (UF)"))
        self.to_currency_box.setItemText(35, _translate("MainWindow", "Chinese Yuan"))
        self.to_currency_box.setItemText(36, _translate("MainWindow", "Chinese Yuan (offshore)"))
        self.to_currency_box.setItemText(37, _translate("MainWindow", "Colombian Peso"))
        self.to_currency_box.setItemText(38, _translate("MainWindow", "Comorian franc"))
        self.to_currency_box.setItemText(39, _translate("MainWindow", "Congolese Franc"))
        self.to_currency_box.setItemText(40, _translate("MainWindow", "Costa Rican Colón"))
        self.to_currency_box.setItemText(41, _translate("MainWindow", "Croatian Kuna"))
        self.to_currency_box.setItemText(42, _translate("MainWindow", "Cuban Peso"))
        self.to_currency_box.setItemText(43, _translate("MainWindow", "Czech Koruna"))
        self.to_currency_box.setItemText(44, _translate("MainWindow", "Danish Krone"))
        self.to_currency_box.setItemText(45, _translate("MainWindow", "Djiboutian Franc"))
        self.to_currency_box.setItemText(46, _translate("MainWindow", "Dominican Peso"))
        self.to_currency_box.setItemText(47, _translate("MainWindow", "East Caribbean Dollar"))
        self.to_currency_box.setItemText(48, _translate("MainWindow", "Egyptian Pound"))
        self.to_currency_box.setItemText(49, _translate("MainWindow", "Ether"))
        self.to_currency_box.setItemText(50, _translate("MainWindow", "Ethiopian Birr"))
        self.to_currency_box.setItemText(51, _translate("MainWindow", "Euro"))
        self.to_currency_box.setItemText(52, _translate("MainWindow", "Fijian Dollar"))
        self.to_currency_box.setItemText(53, _translate("MainWindow", "Gambian dalasi"))
        self.to_currency_box.setItemText(54, _translate("MainWindow", "Georgian Lari"))
        self.to_currency_box.setItemText(55, _translate("MainWindow", "Ghanaian Cedi"))
        self.to_currency_box.setItemText(56, _translate("MainWindow", "Gibraltar Pound"))
        self.to_currency_box.setItemText(57, _translate("MainWindow", "Guatemalan Quetzal"))
        self.to_currency_box.setItemText(58, _translate("MainWindow", "Guinean Franc"))
        self.to_currency_box.setItemText(59, _translate("MainWindow", "Guyanaese Dollar"))
        self.to_currency_box.setItemText(60, _translate("MainWindow", "Haitian Gourde"))
        self.to_currency_box.setItemText(61, _translate("MainWindow", "Honduran Lempira"))
        self.to_currency_box.setItemText(62, _translate("MainWindow", "Hong Kong Dollar"))
        self.to_currency_box.setItemText(63, _translate("MainWindow", "Hungarian Forint"))
        self.to_currency_box.setItemText(64, _translate("MainWindow", "Icelandic Króna"))
        self.to_currency_box.setItemText(65, _translate("MainWindow", "Indian Rupee"))
        self.to_currency_box.setItemText(66, _translate("MainWindow", "Indonesian Rupiah"))
        self.to_currency_box.setItemText(67, _translate("MainWindow", "Iranian Rial"))
        self.to_currency_box.setItemText(68, _translate("MainWindow", "Iraqi Dinar"))
        self.to_currency_box.setItemText(69, _translate("MainWindow", "Israeli New Shekel"))
        self.to_currency_box.setItemText(70, _translate("MainWindow", "Jamaican Dollar"))
        self.to_currency_box.setItemText(71, _translate("MainWindow", "Japanese Yen"))
        self.to_currency_box.setItemText(72, _translate("MainWindow", "Jordanian Dinar"))
        self.to_currency_box.setItemText(73, _translate("MainWindow", "Kazakhstani Tenge"))
        self.to_currency_box.setItemText(74, _translate("MainWindow", "Kenyan Shilling"))
        self.to_currency_box.setItemText(75, _translate("MainWindow", "Kuwaiti Dinar"))
        self.to_currency_box.setItemText(76, _translate("MainWindow", "Kyrgystani Som"))
        self.to_currency_box.setItemText(77, _translate("MainWindow", "Laotian Kip"))
        self.to_currency_box.setItemText(78, _translate("MainWindow", "Lebanese pound"))
        self.to_currency_box.setItemText(79, _translate("MainWindow", "Lesotho loti"))
        self.to_currency_box.setItemText(80, _translate("MainWindow", "Liberian Dollar"))
        self.to_currency_box.setItemText(81, _translate("MainWindow", "Libyan Dinar"))
        self.to_currency_box.setItemText(82, _translate("MainWindow", "Litecoin"))
        self.to_currency_box.setItemText(83, _translate("MainWindow", "Macanese Pataca"))
        self.to_currency_box.setItemText(84, _translate("MainWindow", "Macedonian Denar"))
        self.to_currency_box.setItemText(85, _translate("MainWindow", "Malagasy Ariary"))
        self.to_currency_box.setItemText(86, _translate("MainWindow", "Malawian Kwacha"))
        self.to_currency_box.setItemText(87, _translate("MainWindow", "Malaysian Ringgit"))
        self.to_currency_box.setItemText(88, _translate("MainWindow", "Maldivian Rufiyaa"))
        self.to_currency_box.setItemText(89, _translate("MainWindow", "Mauritanian Ouguiya (1973–2017)"))
        self.to_currency_box.setItemText(90, _translate("MainWindow", "Mauritian Rupee"))
        self.to_currency_box.setItemText(91, _translate("MainWindow", "Mexican Peso"))
        self.to_currency_box.setItemText(92, _translate("MainWindow", "Moldovan Leu"))
        self.to_currency_box.setItemText(93, _translate("MainWindow", "Moroccan Dirham"))
        self.to_currency_box.setItemText(94, _translate("MainWindow", "Mozambican metical"))
        self.to_currency_box.setItemText(95, _translate("MainWindow", "Myanmar Kyat"))
        self.to_currency_box.setItemText(96, _translate("MainWindow", "NT$"))
        self.to_currency_box.setItemText(97, _translate("MainWindow", "Namibian dollar"))
        self.to_currency_box.setItemText(98, _translate("MainWindow", "Nepalese Rupee"))
        self.to_currency_box.setItemText(99, _translate("MainWindow", "Netherlands Antillean Guilder"))
        self.to_currency_box.setItemText(100, _translate("MainWindow", "New Zealand Dollar"))
        self.to_currency_box.setItemText(101, _translate("MainWindow", "Nicaraguan Córdoba"))
        self.to_currency_box.setItemText(102, _translate("MainWindow", "Nigerian Naira"))
        self.to_currency_box.setItemText(103, _translate("MainWindow", "Norwegian Krone"))
        self.to_currency_box.setItemText(104, _translate("MainWindow", "Omani Rial"))
        self.to_currency_box.setItemText(105, _translate("MainWindow", "Pakistani Rupee"))
        self.to_currency_box.setItemText(106, _translate("MainWindow", "Panamanian Balboa"))
        self.to_currency_box.setItemText(107, _translate("MainWindow", "Papua New Guinean Kina"))
        self.to_currency_box.setItemText(108, _translate("MainWindow", "Paraguayan Guarani"))
        self.to_currency_box.setItemText(109, _translate("MainWindow", "Philippine Piso"))
        self.to_currency_box.setItemText(110, _translate("MainWindow", "Poland złoty"))
        self.to_currency_box.setItemText(111, _translate("MainWindow", "Pound sterling"))
        self.to_currency_box.setItemText(112, _translate("MainWindow", "Qatari Rial"))
        self.to_currency_box.setItemText(113, _translate("MainWindow", "Romanian Leu"))
        self.to_currency_box.setItemText(114, _translate("MainWindow", "Russian Ruble"))
        self.to_currency_box.setItemText(115, _translate("MainWindow", "Rwandan franc"))
        self.to_currency_box.setItemText(116, _translate("MainWindow", "Salvadoran Colón"))
        self.to_currency_box.setItemText(117, _translate("MainWindow", "Saudi Riyal"))
        self.to_currency_box.setItemText(118, _translate("MainWindow", "Serbian Dinar"))
        self.to_currency_box.setItemText(119, _translate("MainWindow", "Seychellois Rupee"))
        self.to_currency_box.setItemText(120, _translate("MainWindow", "Sierra Leonean Leone"))
        self.to_currency_box.setItemText(121, _translate("MainWindow", "Singapore Dollar"))
        self.to_currency_box.setItemText(122, _translate("MainWindow", "Sol"))
        self.to_currency_box.setItemText(123, _translate("MainWindow", "Solomon Islands Dollar"))
        self.to_currency_box.setItemText(124, _translate("MainWindow", "Somali Shilling"))
        self.to_currency_box.setItemText(125, _translate("MainWindow", "South African Rand"))
        self.to_currency_box.setItemText(126, _translate("MainWindow", "South Korean won"))
        self.to_currency_box.setItemText(127, _translate("MainWindow", "Sovereign Bolivar"))
        self.to_currency_box.setItemText(128, _translate("MainWindow", "Special Drawing Rights"))
        self.to_currency_box.setItemText(129, _translate("MainWindow", "Sri Lankan Rupee"))
        self.to_currency_box.setItemText(130, _translate("MainWindow", "Sudanese pound"))
        self.to_currency_box.setItemText(131, _translate("MainWindow", "Surinamese Dollar"))
        self.to_currency_box.setItemText(132, _translate("MainWindow", "Swazi Lilangeni"))
        self.to_currency_box.setItemText(133, _translate("MainWindow", "Swedish Krona"))
        self.to_currency_box.setItemText(134, _translate("MainWindow", "Swiss Franc"))
        self.to_currency_box.setItemText(135, _translate("MainWindow", "Tajikistani Somoni"))
        self.to_currency_box.setItemText(136, _translate("MainWindow", "Tanzanian Shilling"))
        self.to_currency_box.setItemText(137, _translate("MainWindow", "Thai Baht"))
        self.to_currency_box.setItemText(138, _translate("MainWindow", "Tongan Paʻanga"))
        self.to_currency_box.setItemText(139, _translate("MainWindow", "Trinidad & Tobago Dollar"))
        self.to_currency_box.setItemText(140, _translate("MainWindow", "Tunisian Dinar"))
        self.to_currency_box.setItemText(141, _translate("MainWindow", "Turkish lira"))
        self.to_currency_box.setItemText(142, _translate("MainWindow", "Turkmenistan manat"))
        self.to_currency_box.setItemText(143, _translate("MainWindow", "Ugandan Shilling"))
        self.to_currency_box.setItemText(144, _translate("MainWindow", "Ukrainian hryvnia"))
        self.to_currency_box.setItemText(145, _translate("MainWindow", "United Arab Emirates Dirham"))
        self.to_currency_box.setItemText(146, _translate("MainWindow", "Uruguayan Peso"))
        self.to_currency_box.setItemText(147, _translate("MainWindow", "Uzbekistani Som"))
        self.to_currency_box.setItemText(148, _translate("MainWindow", "Vietnamese dong"))
        self.to_currency_box.setItemText(149, _translate("MainWindow", "West African CFA franc"))
        self.to_currency_box.setItemText(150, _translate("MainWindow", "Yemeni Rial"))
        self.to_currency_box.setItemText(151, _translate("MainWindow", "Zambian Kwacha"))

    def press(self):
        def replace(x):
            CURRENCY_CODES = {'Afghan Afghani': 'AFN',
                              'Albanian Lek': 'ALL',
                              'Algerian Dinar': 'DZD',
                              'Angolan Kwanza': 'AOA',
                              'Argentine Peso': 'ARS',
                              'Armenian Dram': 'AMD',
                              'Aruban Florin': 'AWG',
                              'Australian Dollar': 'AUD',
                              'Azerbaijani Manat': 'AZN',
                              'Bahamian Dollar': 'BSD',
                              'Bahraini Dinar': 'BHD',
                              'Bajan dollar': 'BBD',
                              'Bangladeshi Taka': 'BDT',
                              'Belarusian Ruble': 'BYR',
                              'Belize Dollar': 'BZD',
                              'Bermudan Dollar': 'BMD',
                              'Bhutan currency': 'BTN',
                              'Bitcoin': 'BTC',
                              'Bitcoin Cash': 'BCH',
                              'Bolivian Boliviano': 'BOB',
                              'Bosnia-Herzegovina Convertible Mark': 'BAM',
                              'Botswanan Pula': 'BWP',
                              'Brazilian Real': 'BRL',
                              'Brunei Dollar': 'BND',
                              'Bulgarian Lev': 'BGN',
                              'Burundian Franc': 'BIF',
                              'CFP Franc': 'XPF',
                              'Cambodian riel': 'KHR',
                              'Canadian Dollar': 'CAD',
                              'Cape Verdean Escudo': 'CVE',
                              'Cayman Islands Dollar': 'KYD',
                              'Central African CFA franc': 'XAF',
                              'Chilean Peso': 'CLP',
                              'Chilean Unit of Account (UF)': 'CLF',
                              'Chinese Yuan': 'CNY',
                              'Chinese Yuan (offshore)': 'CNH',
                              'Colombian Peso': 'COP',
                              'Comorian franc': 'KMF',
                              'Congolese Franc': 'CDF',
                              'Costa Rican Colón': 'CRC',
                              'Croatian Kuna': 'HRK',
                              'Cuban Peso': 'CUP',
                              'Czech Koruna': 'CZK',
                              'Danish Krone': 'DKK',
                              'Djiboutian Franc': 'DJF',
                              'Dominican Peso': 'DOP',
                              'East Caribbean Dollar': 'XCD',
                              'Egyptian Pound': 'EGP',
                              'Ether': 'ETH',
                              'Ethiopian Birr': 'ETB',
                              'Euro': 'EUR',
                              'Fijian Dollar': 'FJD',
                              'Gambian dalasi': 'GMD',
                              'Georgian Lari': 'GEL',
                              'Ghanaian Cedi': 'GHC',
                              'Gibraltar Pound': 'GIP',
                              'Guatemalan Quetzal': 'GTQ',
                              'Guinean Franc': 'GNF',
                              'Guyanaese Dollar': 'GYD',
                              'Haitian Gourde': 'HTG',
                              'Honduran Lempira': 'HNL',
                              'Hong Kong Dollar': 'HKD',
                              'Hungarian Forint': 'HUF',
                              'Icelandic Króna': 'ISK',
                              'Indian Rupee': 'INR',
                              'Indonesian Rupiah': 'IDR',
                              'Iranian Rial': 'IRR',
                              'Iraqi Dinar': 'IQD',
                              'Israeli New Shekel': 'ILS',
                              'Jamaican Dollar': 'JMD',
                              'Japanese Yen': 'JPY',
                              'Jordanian Dinar': 'JOD',
                              'Kazakhstani Tenge': 'KZT',
                              'Kenyan Shilling': 'KES',
                              'Kuwaiti Dinar': 'KWD',
                              'Kyrgystani Som': 'KGS',
                              'Laotian Kip': 'LAK',
                              'Lebanese pound': 'LBP',
                              'Lesotho loti': 'LSL',
                              'Liberian Dollar': 'LRD',
                              'Libyan Dinar': 'LYD',
                              'Litecoin': 'LTC',
                              'Macanese Pataca': 'MOP',
                              'Macedonian Denar': 'MKD',
                              'Malagasy Ariary': 'MGA',
                              'Malawian Kwacha': 'MWK',
                              'Malaysian Ringgit': 'MYR',
                              'Maldivian Rufiyaa': 'MVR',
                              'Mauritanian Ouguiya (1973–2017)': 'MRO',
                              'Mauritian Rupee': 'MUR',
                              'Mexican Peso': 'MXN',
                              'Moldovan Leu': 'MDL',
                              'Moroccan Dirham': 'MAD',
                              'Mozambican metical': 'MZM',
                              'Myanmar Kyat': 'MMK',
                              'NT$': 'TWD',
                              'Namibian dollar': 'NAD',
                              'Nepalese Rupee': 'NPR',
                              'Netherlands Antillean Guilder': 'ANG',
                              'New Zealand Dollar': 'NZD',
                              'Nicaraguan Córdoba': 'NIO',
                              'Nigerian Naira': 'NGN',
                              'Norwegian Krone': 'NOK',
                              'Omani Rial': 'OMR',
                              'Pakistani Rupee': 'PKR',
                              'Panamanian Balboa': 'PAB',
                              'Papua New Guinean Kina': 'PGK',
                              'Paraguayan Guarani': 'PYG',
                              'Philippine Piso': 'PHP',
                              'Poland złoty': 'PLN',
                              'Pound sterling': 'GBP',
                              'Qatari Rial': 'QAR',
                              'Romanian Leu': 'ROL',
                              'Russian Ruble': 'RUR',
                              'Rwandan franc': 'RWF',
                              'Salvadoran Colón': 'SVC',
                              'Saudi Riyal': 'SAR',
                              'Serbian Dinar': 'CSD',
                              'Seychellois Rupee': 'SCR',
                              'Sierra Leonean Leone': 'SLL',
                              'Singapore Dollar': 'SGD',
                              'Sol': 'PEN',
                              'Solomon Islands Dollar': 'SBD',
                              'Somali Shilling': 'SOS',
                              'South African Rand': 'ZAR',
                              'South Korean won': 'KRW',
                              'Sovereign Bolivar': 'VEF',
                              'Special Drawing Rights': 'XDR',
                              'Sri Lankan Rupee': 'LKR',
                              'Sudanese pound': 'SSP',
                              'Surinamese Dollar': 'SRD',
                              'Swazi Lilangeni': 'SZL',
                              'Swedish Krona': 'SEK',
                              'Swiss Franc': 'CHF',
                              'Tajikistani Somoni': 'TJS',
                              'Tanzanian Shilling': 'TZS',
                              'Thai Baht': 'THB',
                              'Tongan Paʻanga': 'TOP',
                              'Trinidad & Tobago Dollar': 'TTD',
                              'Tunisian Dinar': 'TND',
                              'Turkish lira': 'TRY',
                              'Turkmenistan manat': 'TMM',
                              'Ugandan Shilling': 'UGX',
                              'Ukrainian hryvnia': 'UAH',
                              'United Arab Emirates Dirham': 'AED',
                              'United States Dollar': 'USD',
                              'Uruguayan Peso': 'UYU',
                              'Uzbekistani Som': 'UZS',
                              'Vietnamese dong': 'VND',
                              'West African CFA franc': 'XOF',
                              'Yemeni Rial': 'YER',
                              'Zambian Kwacha': 'ZMW'}



            return CURRENCY_CODES[x]

        try:
            fromtext = str(self.from_currency_box.currentText())
            fromtextr = replace(fromtext)#replaced from text
            totext = str(self.to_currency_box.currentText())
            totextr = replace(totext)#replaced to text
            amnt = int(self.amount_textedit.toPlainText())

            jjson = converter.convert(fromtextr, totextr, amnt)
            jjson = json.loads(jjson)
            amounttxt = jjson['amount']
            amounttxt = str(amounttxt)
            
            self.answer_label.setStyleSheet("background-color: white")
            self.answer_label.setText(f'{amnt} {fromtext} is equal to {amounttxt} {totext}')
        except:
            self.answer_label.setStyleSheet("background-color: red")
            self.answer_label.setText("please try again!(you should type integer)")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

