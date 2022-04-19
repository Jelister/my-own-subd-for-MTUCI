from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys

class Login(QWidget):
	auth = QtCore.pyqtSignal(str, str, str, str)
	reg = QtCore.pyqtSignal(str, str, str, str)
	err = QtCore.pyqtSignal(str)
	def __init__(self):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setWindowTitle('Authorization')
		self.dbname_label = QLabel('Database name:')
		layout.addWidget(self.dbname_label)
		self.dbname_line = QLineEdit()
		layout.addWidget(self.dbname_line)
		self.setLayout(layout)
		self.userlogin_label = QLabel('User login:')
		layout.addWidget(self.userlogin_label)
		self.userlogin_line = QLineEdit()
		layout.addWidget(self.userlogin_line)
		self.setLayout(layout)
		self.pass_label = QLabel('User passcode:')
		layout.addWidget(self.pass_label)
		self.pass_line = QLineEdit()
		layout.addWidget(self.pass_line)
		self.setLayout(layout)
		self.port_label = QLabel('Database port:')
		layout.addWidget(self.port_label)
		self.port_line = QLineEdit('5432')
		layout.addWidget(self.port_line)
		self.setLayout(layout)
		self.connect_button = QPushButton('Connect')
		self.connect_button.clicked.connect(self.connect)
		layout.addWidget(self.connect_button, 8, 1)
		self.reg_button = QPushButton('Registration')
		self.reg_button.clicked.connect(self.registration)
		layout.addWidget(self.reg_button, 8, 2)
		self
	def connect(self):
		if len(str(self.dbname_line.text())) > 0:
			if len(str(self.userlogin_line.text())) > 0:
				if len(str(self.pass_line.text())) > 0:
					if len(str(self.port_line.text())) > 0:
						self.auth.emit(self.dbname_line.text(), self.userlogin_line.text(), self.pass_line.text(), self.port_line.text())
					else:
						self.err.emit('Port line error: port line can\'t be emty!')
				else:
					self.err.emit('Password line error: password line can\'t be emty!')
			else:
				self.err.emit('Login line error: login line can\'t be empty!')
		else:
			self.err.emit('Database name error: Database name line can\'t be empty!')
	def registration(self):
		if len(str(self.dbname_line.text())) > 0:
			if len(str(self.userlogin_line.text())) > 0:
				if len(str(self.pass_line.text())) > 0:
					if len(str(self.port_line.text())) > 0:
						self.reg.emit(self.dbname_line.text(), self.userlogin_line.text(), self.pass_line.text(), self.port_line.text())
					else:
						self.err.emit('Port line error: port line can\'t be emty!')
				else:
					self.err.emit('Password error: password line can\'t be emty!')
			else:
				self.err.emit('Login error: login line can\'t be empty!')
		else:
			self.err.emit('Database name error: Database name line can\'t be empty!')

class Auth(QWidget):
	back = QtCore.pyqtSignal()
	def __init__(self, t1, t2, t3, t4):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setWindowTitle(str(t1))
		self.setLayout(layout)
		label = QLabel('Database name: '+str(t1)+'; User login: '+str(t2)+'; User password: '+str(t3)+'; Database port: '+str(t4))
		layout.addWidget(label, 1, 0)
		self.back_button = QPushButton('Back')
		self.back_button.clicked.connect(self.backb)
		layout.addWidget(self.back_button, 0, 0)
	def backb(self):
		self.back.emit()

class LoginError(QWidget):
	cl = QtCore.pyqtSignal()
	def __init__(self, t):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setWindowTitle('Error')
		self.label = QLabel(t)
		layout.addWidget(self.label)
		self.button = QPushButton('Ok')
		self.button.clicked.connect(self.clact)
		layout.addWidget(self.button)
		self.setLayout(layout)
	def clact(self):
		self.cl.emit()

class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.auth.connect(self.show_auth)
        self.login.reg.connect(self.show_reg)
        self.login.err.connect(self.show_err)
        try:
        	self.auth.close()
        except AttributeError:
        	pass
        try:
        	self.reg.close()
        except AttributeError:
        	pass
        self.login.show()

    def show_auth(self, t1, t2, t3, t4):
        self.auth = Auth(t1, t2, t3, t4)
        self.login.close()
        self.auth.back.connect(self.show_login)
        self.auth.show()

    def show_reg(self):
    	self.login.close()
    def hide_err(self):
    	self.erroring.close()

    def show_err(self, t):
    	self.erroring = LoginError(t)
    	self.erroring.cl.connect(self.hide_err)
    	self.erroring.show()
app = QApplication(sys.argv)
screen = Controller()
screen.show_login()
sys.exit(app.exec_())