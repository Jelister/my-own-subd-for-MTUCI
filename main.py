from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import psycopg2

class Login(QWidget):
	auth = QtCore.pyqtSignal(str, str, str, str)
	reg = QtCore.pyqtSignal(str, str, str, str)
	err = QtCore.pyqtSignal(str)
	cl = QtCore.pyqtSignal()
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle('Authorization')
		self.setMaximumSize(QtCore.QSize(360, 640))
		self.setMinimumSize(QtCore.QSize(360, 640))
		self.setStyleSheet("""background-color: rgb(75, 105, 240) """)
		
		self.main_label = QLabel('Authorization.', self)
		self.frame =QFrame(self)
		self.dbname_label = QLabel('Database name:', self)
		self.dbname_line = QLineEdit(self)
		self.userlogin_label = QLabel('User login:', self)
		self.userlogin_line = QLineEdit(self)
		self.pass_label = QLabel('User passcode:', self)
		self.pass_line = QLineEdit(self)
		self.port_label = QLabel('Database port:', self)
		self.port_line = QLineEdit('5432', self)
		self.connect_button = QPushButton('Connect!', self)
		self.connect_button.clicked.connect(self.connect)
		self.reg_button = QPushButton('Cancel', self)
		self.reg_button.clicked.connect(self.registration)
		x1 = 55
		x2 = 155
		self.main_label.move(95, 0)
		self.frame.move(x1-10, 35)
		self.dbname_label.move(x1, 50)
		self.dbname_line.move(x2, 48)
		self.userlogin_label.move(x1, 150)
		self.userlogin_line.move(x2, 148)
		self.pass_label.move(x1, 250)
		self.pass_line.move(x2, 248)
		self.port_label.move(x1, 350)
		self.port_line.move(x2, 348)
		self.connect_button.move(130, 450)
		self.reg_button.move(150, 550)

		self.main_label.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 24px; color: rgb(255, 255, 255); font: bold "Times New Roman"; border-radius: 5px; min-width: 170; min-height: 30; max-width: 170; max-height: 30""")
		self.frame.setStyleSheet("""background-color: rgb(255, 255, 255); min-height: 480; min-width: 270; border-radius: 8px """)
		self.dbname_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.dbname_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24""")
		self.userlogin_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24""")
		self.userlogin_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.pass_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24""")
		self.pass_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.port_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24""")
		self.port_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.connect_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 20px; color: rgb(255, 255, 255); font: "Times New Roman"; border-radius: 5px; min-width: 100; min-height: 24; max-width: 100; max-height: 24""")
		self.reg_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 14px; color: white; font: bold "Times New Roman"; border-radius: 0px; min-width: 60; min-height: 24; max-width: 60; max-height: 24""")
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
		self.cl.emit()
	"""
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
	"""
class Auth(QWidget):
	back = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	conn1 = QtCore.pyqtSignal(str, str, str, str, str)
	def __init__(self, t1, t2, t3, t4):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setWindowTitle(str(t1))
		self.setMaximumSize(QtCore.QSize(800, 600))
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.setLayout(layout)
		self.selecter = QLineEdit()
		layout.addWidget(self.selecter, 0, 0)
		#label = QLabel('Database name: '+str(t1)+'; User login: '+str(t2)+'; User password: '+str(t3)+'; Database port: '+str(t4))
		#layout.addWidget(label, 1, 0)
		self.back_button = QPushButton('Back')
		self.back_button.clicked.connect(self.back)
		layout.addWidget(self.back_button, 1, 1)
		self.conn_button = QPushButton('Connect')
		self.conn_button.clicked.connect(lambda: self.conn(t1, t2, t3, t4))
		layout.addWidget(self.conn_button, 1, 0)
	def backb(self):
		self.back.emit()

	def conn(self, t1, t2, t3, t4):
		s = 'SELECT * FROM '+self.selecter.text()
		print(s)
		self.conn1.emit(s, t1, t2, t3, t4)

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

class DataBaseEditor(QWidget):
	back = QtCore.pyqtSignal()
	comm = QtCore.pyqtSignal()#add smtn
	def __init__(self, s, t1, t2, t3, t4):
		conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
		cur_sql = conn.cursor()
		cur_sql.execute(str(s))
		db = cur_sql.fetchall()
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setWindowTitle(s[13:-1]+s[-1])
		self.setMaximumSize(QtCore.QSize(800, 600))
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.label = QLabel(str(db))
		layout.addWidget(self.label)
		self.setLayout(layout)


class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.auth.connect(self.show_auth)
        self.login.reg.connect(self.show_reg)
        self.login.err.connect(self.show_err)
        self.login.cl.connect(self.hide_login)
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
    	try:
    		conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
    		self.auth = Auth(t1, t2, t3, t4)
    		self.login.close()
    		self.auth.back.connect(self.show_login)
    		self.auth.err.connect(self.show_err)
    		self.auth.conn1.connect(self.show_db)
    		self.auth.show()
    	except Exception as t:
    		self.show_err(str(t))
        
    def show_db(self, s, t1, t2, t3, t4):
    	self.db = DataBaseEditor(s, t1, t2, t3, t4)
    	self.auth.close()
    	self.db.show()
    def show_reg(self):
    	self.login.close()
    def hide_err(self):
    	self.erroring.close()
    def hide_login(self):
    	self.login.close()

    def show_err(self, t):
    	print(t)
    	self.erroring = LoginError(t)
    	self.erroring.cl.connect(self.hide_err)
    	self.erroring.show()
app = QApplication(sys.argv)
screen = Controller()
screen.show_login()
sys.exit(app.exec_())