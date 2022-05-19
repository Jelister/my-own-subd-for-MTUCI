#Dude, this program sucks. I'm f%$#ing hate this code. - Tony
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys
import psycopg2
class Login(QMainWindow):
	auth = QtCore.pyqtSignal(str, str, str, str, str)
	err = QtCore.pyqtSignal(str)
	cl = QtCore.pyqtSignal()

	def __init__(self):
		QWidget.__init__(self)

		self.showUI()
		self.setWindowTitle('Authorization')
		self.setMaximumSize(QtCore.QSize(360, 640))
		self.setMinimumSize(QtCore.QSize(360, 640))
		self.setStyleSheet("""background-color: rgb(75, 105, 240) """)
		self.setWindowIcon(QIcon('ico/python.ico'))
		
		self.main_label = QLabel('<p align="center">Authorization.</p>', self)
		self.frame =QFrame(self)

		self.dbname_label = QLabel('Database name:', self)
		self.dbname_line = QLineEdit('', self)

		self.userlogin_label = QLabel('User login:', self)
		self.userlogin_line = QLineEdit('', self)

		self.pass_label = QLabel('User passcode:', self)
		self.pass_line = QLineEdit('', self)
		self.pass_line.setEchoMode(QLineEdit.Password)

		self.host_label = QLabel('Database host:', self)
		self.host_line = QLineEdit('localhost', self)

		self.port_label = QLabel('Database port:', self)
		self.port_line = QLineEdit('5432', self)

		self.connect_button = QPushButton('Connect!', self)
		self.connect_button.clicked.connect(self.connect)

		self.back_button = QPushButton('Cancel', self)
		self.back_button.clicked.connect(lambda: self.cl.emit())
		x1 = 55
		x2 = 175
		self.main_label.move(0, 0)
		self.frame.move(x1-10, 35)
		self.dbname_label.move(x1, 50)
		self.dbname_line.move(x2, 52)
		self.userlogin_label.move(x1, 150)
		self.userlogin_line.move(x2, 152)
		self.pass_label.move(x1, 250)
		self.pass_line.move(x2, 252)
		self.host_label.move(x1, 350)
		self.host_line.move(x2, 352)
		self.port_label.move(x1, 400)
		self.port_line.move(x2, 402)
		self.connect_button.move(130, 450)
		self.back_button.move(150, 550)

		self.main_label.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 24px; color: rgb(255, 255, 255); font: bold "Times New Roman"; border-radius: 5px; min-width: 360; min-height: 30; max-width: 360; max-height: 30""")
		self.frame.setStyleSheet("""background-color: rgb(255, 255, 255); min-height: 480; min-width: 270; border-radius: 8px """)
		self.dbname_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.dbname_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 125; max-width: 125; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.userlogin_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 125; max-width: 125; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.userlogin_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.pass_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 125; max-width: 125; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.pass_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.host_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 125; max-width: 125; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.host_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.port_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 125; max-width: 125; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.port_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.connect_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 20px; color: rgb(255, 255, 255); font: "Times New Roman"; border-radius: 5px; min-width: 100; min-height: 24; max-width: 100; max-height: 24""")
		self.back_button.setStyleSheet("""text-decoration: underline; background-color: rgb(75, 105, 240); font-size: 14px; color: white; font: bold "Times New Roman"; border-radius: 0px; min-width: 60; min-height: 24; max-width: 60; max-height: 24""")
		
	def showUI(self):

		self.statusBar()

		menubar = self.menuBar()

		exitAction = QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(qApp.quit)
		terminalAction = QAction('$Terminal',self)
		terminalAction.setShortcut('Ctrl+`')
		terminalAction.triggered.connect(lambda: print('Terminal update! Soon...'))

		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)
		fileMenu.addAction(terminalAction)
	def connect(self):
		if len(str(self.dbname_line.text())) > 0:
			if len(str(self.userlogin_line.text())) > 0:
				if len(str(self.pass_line.text())) > 0:
					if len(str(self.host_line.text())) > 0:
						if len(str(self.port_line.text())) > 0:
							self.auth.emit(self.dbname_line.text(), self.userlogin_line.text(), self.pass_line.text(), self.port_line.text(), self.host_line.text())
						else:
							self.err.emit('Port line error: port line can\'t be emty!')
					else:
						self.err.emit('Host line error: port line can\'t be emty!')
				else:
					self.err.emit('Password line error: password line can\'t be emty!')
			else:
				self.err.emit('Login line error: login line can\'t be empty!')
		else:
			self.err.emit('Database name error: Database name line can\'t be empty!')

class Auth(QMainWindow):
	back = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	conn1 = QtCore.pyqtSignal(str, str, str, str, str, str)
	def __init__(self, t1, t2, t3, t4,t5):
		QWidget.__init__(self)
		self.showUI()
		self.setWindowTitle('Table selection.')
		self.setMaximumSize(QtCore.QSize(360, 640))
		self.setMinimumSize(QtCore.QSize(360, 640))
		self.setStyleSheet("""background-color: rgb(75, 105, 240) """)
		self.setWindowIcon(QIcon('ico/python.ico'))

		self.frame =QFrame(self)

		self.main_label = QLabel('<p align="center">Table selection.</p>', self)

		self.selecter_label = QLabel('Table name:', self)

		self.selecter_line = QLineEdit(self)

		self.back_button = QPushButton('Back', self)
		self.back_button.clicked.connect(lambda: self.back.emit())

		self.conn_button = QPushButton('Connect!', self)
		self.conn_button.clicked.connect(lambda: self.conn(t1, t2, t3, t4,t5))
		
		self.main_label.move(0, 0)
		self.frame.move(45, 35)
		self.selecter_label.move(55, 50)
		self.selecter_line.move(155, 49)
		self.conn_button.move(130, 450)
		self.back_button.move(150, 550)

		self.main_label.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 24px; color: rgb(255, 255, 255); font: bold "Times New Roman"; border-radius: 5px; min-width: 360; min-height: 30; max-width: 360; max-height: 30""")
		self.frame.setStyleSheet("""background-color: rgb(255, 255, 255); min-height: 480; min-width: 270; border-radius: 8px """)
		self.selecter_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.selecter_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.conn_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 20px; color: rgb(255, 255, 255); font: "Times New Roman"; border-radius: 5px; min-width: 100; min-height: 24; max-width: 100; max-height: 24""")
		self.back_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 14px; color: white; font: bold "Times New Roman"; border-radius: 0px; min-width: 60; min-height: 24; max-width: 60; max-height: 24""")

		exitAction = QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(qApp.quit)
		backAction = QAction('&Back', self)
		backAction.setShortcut('Ctrl+B')
		backAction.triggered.connect(lambda: self.back.emit())

	def showUI(self):

		self.statusBar()

		menubar = self.menuBar()

		exitAction = QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(qApp.quit)
		terminalAction = QAction('$Terminal',self)
		terminalAction.setShortcut('Ctrl+`')
		terminalAction.triggered.connect(lambda: print('Terminal update! Soon...'))

		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)
		fileMenu.addAction(terminalAction)
	def conn(self, t1, t2, t3, t4,t5):
		s = self.selecter_line.text()
		try:
			conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4,host=t5)
			cur_sql = conn.cursor()
			cur_sql.execute('SELECT * FROM '+str(s))
			self.conn1.emit(s, t1, t2, t3, t4,t5)
		except Exception as e:
			self.err.emit(str(e))

class DataBaseEditor(QMainWindow):
	back = QtCore.pyqtSignal(str,str,str,str,str)
	comm = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	def __init__(self, s, t1, t2, t3, t4,t5):
		super().__init__()

		self.showUI(s, t1, t2, t3, t4,t5)

	def showUI(self, s, t1, t2, t3, t4,t5):

		conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4,host=t5)
		cur_sql = conn.cursor()
		cur_sql.execute('SELECT * FROM '+str(s))
		db = cur_sql.fetchall()

		self.setWindowTitle(str(s)+' database Editor')
		self.setMaximumSize(QtCore.QSize(800, 600))
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.setStyleSheet("""background-color: rgb(255,255,255) """)
		self.setWindowIcon(QIcon('python.ico'))
		self.main_frame = QFrame(self)
		self.main_frame.setStyleSheet("""background-color: rgb(75, 105, 240); min-height: 600; min-width: 800; max-height: 600; max-width: 800; border-radius: 8px """)

		self.statusBar()
		self.statusBar().setStyleSheet("""background-color: rgb(75, 105, 240)""")
		self.table_frame =QFrame(self)
		self.table_frame.move(20, 40)
		self.table_frame.setStyleSheet("""background-color: rgb(255, 255, 255); min-height: 540; min-width: 760; max-height: 540; max-width: 760; border-radius: 8px """)
		
		a = 0
		b = 0
		for hor in db:
			a+=1
			if a == 1:
				for ver in hor:
					b+=1

		self.table = QTableWidget(self)
		self.table.setColumnCount(b)
		self.table.setRowCount(a)
		self.table.setMinimumWidth(740)
		self.table.setMinimumHeight(500)
		self.table.move(30, 50)

		column_names = [t[0] for t in cur_sql.description]

		self.table.setHorizontalHeaderLabels(column_names) 
		self.table.setStyleSheet("""border-radius: 0px; background-color: rgb(255, 255, 255); background: rgb(255, 255, 255); border-color: rgb(255,255,255); outline-color: rgb(255,255,255); color: rgb(0, 0, 0)""")

		a = 0
		for hor in db:
			b = 0
			for ver in hor:
				self.table.setItem(a, b, QTableWidgetItem(str(ver)))
				b+=1
			a+=1
		self.table.resizeColumnsToContents()

		exitAction = QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(qApp.quit)
		backAction = QAction('&Back', self)
		backAction.setShortcut('Ctrl+B')
		backAction.setStatusTip('Change table')
		backAction.triggered.connect(lambda: self.back.emit(t1, t2, t3, t4,t5))
		saveAction = QAction('&Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save changes')
		saveAction.triggered.connect(lambda: self.save_commiting_changes(s, t1, t2,t3,t4,t5))

		menubar = self.menuBar()
		menubar.setStyleSheet("""background: rgb(255, 255, 255); selection-background-color: rgb(145,201,247)""")

		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(saveAction)
		fileMenu.addAction(backAction)
		fileMenu.addAction(exitAction)
		fileMenu.setStyleSheet("""color: rgb(0,0,0); background-color: rgb(255,255,255)""")
		
		rowAction = QAction('&Add row', self)
		rowAction.setShortcut('Ctrl+Alt+R')
		rowAction.setStatusTip('Add a new row')
		rowAction.triggered.connect(lambda: self.add_row())
		
		colAction = QAction('&Add column', self)
		colAction.setShortcut('Ctrl+Alt+C')
		colAction.setStatusTip('Add a new column')
		colAction.triggered.connect(lambda: self.add_col(s,t1,t2,t3,t4,t5))

		delrowAction = QAction('&Delete row', self)
		delrowAction.setShortcut('Ctrl+Shift+r')
		delrowAction.setStatusTip('Delete last row')
		delrowAction.triggered.connect(lambda: self.del_row())

		delcolAction = QAction('&Delete column', self)
		delcolAction.setShortcut('Ctrl+Shift+C')
		delcolAction.setStatusTip('Delete last column')
		delcolAction.triggered.connect(lambda: self.del_col(s,t1,t2,t3,t4,t5))

		editMenu = menubar.addMenu('&Edit')
		editMenu.addAction(rowAction)
		editMenu.addAction(colAction)
		editMenu.addAction(delrowAction)
		editMenu.addAction(delcolAction)
		editMenu.setStyleSheet("""color: rgb(0,0,0); background-color: rgb(255,255,255)""")

	def add_row(self):
		self.adding_row = RowWindow(1)
		self.adding_row.ok.connect(self.ds_func)
		self.adding_row.ko.connect(lambda: self.adding_row.close())
		self.adding_row.exec_()

	def ds_func(self):
		self.table.setRowCount(int(self.table.rowCount()+1))
		self.adding_row.close()

	def del_row(self):
		self.deling_row = RowWindow(0)
		self.deling_row.ok.connect(self.sd_func)
		self.deling_row.ko.connect(lambda: self.deling_row.close())
		self.deling_row.exec_()

	def sd_func(self):
		self.table.setRowCount(int(self.table.rowCount()-1))
		self.deling_row.close()

	def add_col(self,s,t1,t2,t3,t4,t5):
		try:
			self.adding_col = ColumnWindow(1,s,t1,t2,t3,t4,t5)
			self.adding_col.ok.connect(self.adding_colum)
			self.adding_col.ko.connect(lambda: self.adding_col.close())
			self.adding_col.err.connect(self.show_err)
			self.adding_col.exec_()
		except Exception as e:
			self.show_err('Add_col error')
			print(e)

	def adding_colum(self, col_name, t1, t2, t3,t4,t5,s,default):
		try:
			self.table.setColumnCount(int(self.table.columnCount()+1))
			conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4,host=t5)
			cur_sql = conn.cursor()
			cur_sql.execute('SELECT * FROM '+str(s))
			db = cur_sql.fetchall()

			a = 0
			b = 0
			for hor in db:
				a+=1
				if a == 1:
					for ver in hor:
						b+=1

			self.table.setHorizontalHeaderLabels([t[0] for t in cur_sql.description])

			for i in range(b+2):
				self.table.setItem(i,b-1, QTableWidgetItem(str(default)))

			self.table.resizeColumnsToContents()

		except Exception:
			self.show_err('Adding column error')

	def deling_colum(self, col_name, t1, t2, t3,t4,t5,s,default):
		try:
			conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4,host=t5)
			cur_sql = conn.cursor()
			cur_sql.execute('SELECT * FROM '+str(s))
			db = cur_sql.fetchall()
			a = 0
			b = 0
			for hor in db:
				a+=1
				if a == 1:
					for ver in hor:
						b+=1

			self.table.setColumnCount(b)
			self.table.setRowCount(a)
			self.table.setMinimumWidth(740)
			self.table.setMinimumHeight(500)
			self.table.move(30, 50)
			column_names = [t[0] for t in cur_sql.description]
			self.table.setHorizontalHeaderLabels(column_names)
			a = 0
			for hor in db:
				b = 0
				for ver in hor:
					self.table.setItem(a, b, QTableWidgetItem(str(ver)))
					b+=1
				a+=1
			self.table.resizeColumnsToContents()
		except Exception:
			self.show_err('Deling column error')

	def del_col(self,s,t1,t2,t3,t4,t5):
		self.deling_col = ColumnWindow(0,s,t1,t2,t3,t4,t5)
		self.deling_col.ok.connect(self.deling_colum)
		self.deling_col.ko.connect(lambda: self.deling_col.close())
		self.deling_col.err.connect(self.show_err)
		self.deling_col.exec_()

	def save_commiting_changes(self,s,t1,t2,t3,t4,t5):
		try:
			mas = []
			a, b = self.table.rowCount(), self.table.columnCount()
			for i in range(a):
				st = ''
				for j in range(b):
					st+='\''+str(self.table.item(i, j).text())+'\', '
				mas+=[st[0:-2]]
			conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4,host=t5)
			cur_sql = conn.cursor()
			cur_sql.execute('DELETE FROM '+str(s))
			for i in range(len(mas)):
				cur_sql.execute('INSERT INTO '+str(s)+' VALUES ('+str(mas[i])+')')
			conn.commit()
			self.statusBar().showMessage("Saved!", 2000)
		except Exception as e:
			self.err.emit(str(e))

	def show_err(self, t):
		try:
			self.erroring = LoginError(t)
			self.erroring.cl.connect(lambda: self.erroring.close())
			self.erroring.exec_()
		except Exception as e:
			print('show_err error: '+str(e))

class RowWindow(QDialog):
	ok=QtCore.pyqtSignal()
	ko=QtCore.pyqtSignal()
	def __init__(self, a):
		QWidget.__init__(self)
		self.setMaximumSize(QtCore.QSize(352, 123))
		self.setMinimumSize(QtCore.QSize(352, 123))

		if a == 1:
			self.setWindowTitle('Adding a row')
		else:
			self.setWindowTitle('Deleting a row')

		self.framerow = QFrame(self)
		self.framerow.setStyleSheet("""max-width:352; min-width:352; max-height:82; min-height:82; background-color: rgb(255,255,255)""")

		self.label = QLabel('Are you sure?',self)
		self.label.setStyleSheet("""font-size: 15px; color: rgb(0,51,188); font: 'Arial'""")

		self.but1=QPushButton('Continue',self)
		self.but1.setStyleSheet("""max-width:110; min-width:110; max-height:21; min-height:21""")
		self.but2=QPushButton('Cancel',self)
		self.but2.setStyleSheet("""max-width:78; min-width:78; max-height:21; min-height:21""")
		self.but1.clicked.connect(lambda: self.ok.emit())
		self.but2.clicked.connect(lambda: self.ko.emit())
		self.framerow.move(0,0)
		self.label.move(11,12)
		self.but1.move(142, 91)
		self.but2.move(260, 91)


class ColumnWindow(QDialog):
    ok = QtCore.pyqtSignal(str, str, str, str, str, str, str, str)
    ko = QtCore.pyqtSignal()
    err = QtCore.pyqtSignal(str)
    def __init__(self,a,s,t1,t2,t3,t4,t5):
        QDialog.__init__(self)
        self.setMaximumSize(QtCore.QSize(370, 120))
        self.setMinimumSize(QtCore.QSize(370, 120))
        if a == 1:
        	self.setWindowTitle('Adding a new column')

        	self.col_line = QLineEdit('', self)
        	self.col_line_label = QLabel('Name:',self)

        	self.col_type_label = QLabel('Type:',self)
        	self.col_type = QComboBox(self)
        	self.col_type.addItem('text')
        	self.col_type.addItem('integer')
        	self.col_type.addItem('char')
        	self.col_type.addItem('bool')
        	self.col_type.setFrame(True)
        	self.col_type.setEditable(True)

        	self.n_null = QCheckBox("Not null?", self)
        	self.n_null.setChecked(True)
        	self.p_k = QCheckBox("Primary key?", self)

        	self.def_line_label = QLabel('Default value of column',self)
        	self.def_line = QLineEdit('Default value', self)

        	self.col_line_label.move(5, 12)
        	self.col_line.move(43, 10)
        	self.col_type_label.move(5, 42)
        	self.col_type.move(43, 40)
        	self.n_null.move(5, 75)
        	self.p_k.move(5, 100)
        	self.def_line_label.move(160,75)
        	self.def_line.move(160, 95)

        else:
        	self.setWindowTitle('Deleting column')
        	self.col_line_label = QLabel('Name:',self)
        	self.col_line = QLineEdit('', self)
        	self.col_line_label.move(5, 10)
        	self.col_line.move(43, 10)

        self.ok_button = QPushButton('Continue', self)
        self.ko_button = QPushButton('Cancel', self)
        self.ok_button.move(281, 8)
        self.ko_button.move(281, 36)
        self.ok_button.setStyleSheet("""min-width: 77; min-height: 20; max-width: 77; max-height: 20""")
        self.ko_button.setStyleSheet("""min-width: 77; min-height: 20; max-width: 77; max-height: 20""")
        
        if a == 1:
        	if self.n_null.isChecked():
        		self.n_null = 'Yes'
        	else:
        		self.n_null = 'No'
        	if self.p_k.isChecked():
        		self.p_k = 'Yes'
        	else:
        		self.p_k = 'No'
        	self.ok_button.clicked.connect(lambda: self.do_do(self.col_line.text(),self.col_type.currentText(),t1,t2,t3,t4,t5,s,self.n_null,self.p_k,self.def_line.text()))
        elif a == 0:
        	self.ok_button.clicked.connect(lambda: self.do_do(self.col_line.text(),0,t1,t2,t3,t4,t5,s,'','',''))
        self.ko_button.clicked.connect(lambda: self.ko.emit())

    def do_do(self, col_name, col_type, t1, t2, t3, t4,t5,table_name,nn,pk,def_value):
        if col_type == 0:
            try:
                conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4,host=t5)
                cur_sql = conn.cursor()
                s = 'ALTER TABLE '+table_name+' DROP COLUMN '+col_name
                cur_sql.execute(s)
                conn.commit()
                self.ok.emit(col_name, t1, t2, t3,t4,t5,table_name,def_value)
                self.ko.emit()
            except Exception as e:
                self.err.emit(str(e))

        else:
            try:
            	if pk == 'Yes':
            		pk = 'PRIMARY KEY'
            	else:
            		pk = ''
            	if nn == 'Yes':
            		nn = 'NOT NULL'
            	else:
            		nn = ''
            	if def_value == 'Default value' or def_value == '':
            		if col_type == 'bool':
            			def_value = 'False'
            		else:
            			def_value = '0'
            	if def_value == 'true':
            		def_value = 'True'
            	if def_value == 'false':
            		def_value = 'False'
            	conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4,host=t5)
            	cur_sql = conn.cursor()
            	s = 'ALTER TABLE '+table_name+' ADD COLUMN '+col_name+' '+col_type+' default \''+def_value+'\' '+nn+' '+pk
            	cur_sql.execute(s)
            	conn.commit()
            	self.ok.emit(col_name, t1, t2, t3,t4,t5,table_name, def_value)
            	self.ko.emit()
            except Exception as e:
            	self.err.emit(str(e))


class LoginError(QDialog):
	cl = QtCore.pyqtSignal()
	def __init__(self, t):
		QWidget.__init__(self)
		self.setWindowIcon(QIcon('python.ico'))
		layout = QGridLayout()
		self.setWindowTitle('Error')
		self.label = QLabel(t)
		layout.addWidget(self.label)
		self.button = QPushButton('Ok')
		self.button.clicked.connect(self.clact)
		layout.addWidget(self.button)
		self.setLayout(layout)
		exitAction = QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(qApp.quit)
		exitAction = QAction('&Back', self)
		exitAction.setShortcut('Ctrl+B')
		exitAction.triggered.connect(qApp.quit)
	def clact(self):
		self.cl.emit()


class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.auth.connect(self.show_auth)
        self.login.err.connect(self.show_err)
        self.login.cl.connect(lambda: self.login.close())
        try:
        	self.auth.close()
        except AttributeError:
        	pass
        try:
        	self.reg.close()	
        except AttributeError:
        	pass
        self.login.show()
    def show_auth(self, t1, t2, t3, t4, t5):
    	try:
    		self.db.close()
    	except AttributeError:
    		pass
    	try:
    		conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4, host=t5)
    		self.auth = Auth(t1, t2, t3, t4, t5)
    		self.login.close()
    		self.auth.back.connect(self.show_login)
    		self.auth.err.connect(self.show_err)
    		self.auth.conn1.connect(self.show_db)
    		self.auth.show()
    	except Exception as t:
    		self.show_err(str(t))
        
    def show_db(self, s, t1, t2, t3, t4,t5):
    	self.db = DataBaseEditor(s, t1, t2, t3, t4,t5)
    	self.auth.close()
    	self.db.show()
    	self.db.back.connect(self.show_auth)
    	self.db.err.connect(self.show_err)

    def show_err(self, t):
    	self.erroring = LoginError(t)
    	self.erroring.cl.connect(lambda: self.erroring.close())
    	self.erroring.exec_()

app = QApplication(sys.argv)
screen = Controller()
screen.show_login()
sys.exit(app.exec_())