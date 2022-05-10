from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import sys
import psycopg2
#private one, dude#
class Login(QWidget):
	auth = QtCore.pyqtSignal(str, str, str, str)
	err = QtCore.pyqtSignal(str)
	cl = QtCore.pyqtSignal()
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle('Authorization')
		self.setMaximumSize(QtCore.QSize(360, 640))
		self.setMinimumSize(QtCore.QSize(360, 640))
		self.setStyleSheet("""background-color: rgb(75, 105, 240) """)
		self.setWindowIcon(QIcon('python.ico'))
		
		self.main_label = QLabel('<p align="center">Authorization.</p>', self)
		self.frame =QFrame(self)

		self.dbname_label = QLabel('Database name:', self)
		self.dbname_line = QLineEdit('', self)

		self.userlogin_label = QLabel('User login:', self)
		self.userlogin_line = QLineEdit('', self)

		self.pass_label = QLabel('User passcode:', self)
		self.pass_line = QLineEdit('', self)
		self.pass_line.setEchoMode(QLineEdit.Password)

		self.port_label = QLabel('Database port:', self)
		self.port_line = QLineEdit('5432', self)

		self.connect_button = QPushButton('Connect!', self)
		self.connect_button.clicked.connect(self.connect)

		self.back_button = QPushButton('Cancel', self)
		self.back_button.clicked.connect(lambda: self.cl.emit())
		x1 = 55
		x2 = 155
		self.main_label.move(0, 0)
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
		self.back_button.move(150, 550)

		self.main_label.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 24px; color: rgb(255, 255, 255); font: bold "Times New Roman"; border-radius: 5px; min-width: 360; min-height: 30; max-width: 360; max-height: 30""")
		self.frame.setStyleSheet("""background-color: rgb(255, 255, 255); min-height: 480; min-width: 270; border-radius: 8px """)
		self.dbname_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.dbname_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.userlogin_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.userlogin_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.pass_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.pass_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.port_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.port_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.connect_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 20px; color: rgb(255, 255, 255); font: "Times New Roman"; border-radius: 5px; min-width: 100; min-height: 24; max-width: 100; max-height: 24""")
		self.back_button.setStyleSheet("""text-decoration: underline; background-color: rgb(75, 105, 240); font-size: 14px; color: white; font: bold "Times New Roman"; border-radius: 0px; min-width: 60; min-height: 24; max-width: 60; max-height: 24""")
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

class Auth(QWidget):
	back = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	conn1 = QtCore.pyqtSignal(str, str, str, str, str)
	def __init__(self, t1, t2, t3, t4):
		QWidget.__init__(self)
		self.setWindowTitle('Table selection.')
		self.setMaximumSize(QtCore.QSize(360, 640))
		self.setMinimumSize(QtCore.QSize(360, 640))
		self.setStyleSheet("""background-color: rgb(75, 105, 240) """)
		self.setWindowIcon(QIcon('python.ico'))

		self.frame =QFrame(self)

		self.main_label = QLabel('<p align="center">Table selection.</p>', self)

		self.selecter_label = QLabel('Table name:', self)

		self.selecter_line = QLineEdit(self)

		self.back_button = QPushButton('Back', self)
		self.back_button.clicked.connect(lambda: self.back.emit())

		self.conn_button = QPushButton('Connect!', self)
		self.conn_button.clicked.connect(lambda: self.conn(t1, t2, t3, t4))

		
		x1 = 55
		x2 = 155
		self.main_label.move(0, 0)
		self.frame.move(x1-10, 35)
		self.selecter_label.move(x1, 50)
		self.selecter_line.move(x2, 50)
		self.conn_button.move(130, 450)
		self.back_button.move(150, 550)


		self.main_label.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 24px; color: rgb(255, 255, 255); font: bold "Times New Roman"; border-radius: 5px; min-width: 360; min-height: 30; max-width: 360; max-height: 30""")
		self.frame.setStyleSheet("""background-color: rgb(255, 255, 255); min-height: 480; min-width: 270; border-radius: 8px """)
		self.selecter_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
		self.selecter_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
		self.conn_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 20px; color: rgb(255, 255, 255); font: "Times New Roman"; border-radius: 5px; min-width: 100; min-height: 24; max-width: 100; max-height: 24""")
		self.back_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 14px; color: white; font: bold "Times New Roman"; border-radius: 0px; min-width: 60; min-height: 24; max-width: 60; max-height: 24""")

	def conn(self, t1, t2, t3, t4):
		s = self.selecter_line.text()
		try:
			conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
			cur_sql = conn.cursor()
			cur_sql.execute('SELECT * FROM '+str(s))
			self.conn1.emit(s, t1, t2, t3, t4)
		except Exception as e:
			self.err.emit(str(e))

class LoginError(QWidget):
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
	def clact(self):
		self.cl.emit()

class DataBaseEditor(QMainWindow):
	back = QtCore.pyqtSignal(str,str,str,str)
	comm = QtCore.pyqtSignal()
	err = QtCore.pyqtSignal(str)
	def __init__(self, s, t1, t2, t3, t4):
		super().__init__()

		self.showUI(s, t1, t2, t3, t4)

	def showUI(self, s, t1, t2, t3, t4):
		

		conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
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
		backAction.triggered.connect(lambda: self.back.emit(t1, t2, t3, t4))

		saveAction = QAction('&Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.setStatusTip('Save changes')
		saveAction.triggered.connect(lambda: self.save_commiting_changes(s, t1, t2,t3,t4))

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
		rowAction.triggered.connect(lambda: self.table.setRowCount(int(self.table.rowCount()+1)))
		
		colAction = QAction('&Add column', self)
		colAction.setShortcut('Ctrl+Alt+C')
		colAction.setStatusTip('Add a new column')
		colAction.triggered.connect(lambda: self.add_col(s,t1,t2,t3,t4))

		delrowAction = QAction('&Delete row', self)
		delrowAction.setShortcut('Ctrl+Shift+r')
		delrowAction.setStatusTip('Delete last row')
		delrowAction.triggered.connect(lambda: self.table.setRowCount(int(self.table.rowCount()-1)))

		delcolAction = QAction('&Delete column', self)
		delcolAction.setShortcut('Ctrl+Shift+C')
		delcolAction.setStatusTip('Delete last column')
		delcolAction.triggered.connect(lambda: self.del_col(s,t1,t2,t3,t4))

		editMenu = menubar.addMenu('&Edit')
		editMenu.addAction(rowAction)
		editMenu.addAction(colAction)
		editMenu.addAction(delrowAction)
		editMenu.addAction(delcolAction)
		editMenu.setStyleSheet("""color: rgb(0,0,0); background-color: rgb(255,255,255)""")

	def save_commiting_changes(self,s,t1,t2,t3,t4):
		try:
			mas = []
			a, b = self.table.rowCount(), self.table.columnCount()
			for i in range(a):
				st = ''
				for j in range(b):
					st+='\''+str(self.table.item(i, j).text())+'\', '
				mas+=[st[0:-2]]
			conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
			cur_sql = conn.cursor()
			cur_sql.execute('DELETE FROM '+str(s))
			for i in range(len(mas)):
				cur_sql.execute('INSERT INTO '+str(s)+' VALUES ('+str(mas[i])+')')
			conn.commit()
			self.statusBar().showMessage("Saved!", 2000)
		except Exception as e:
			self.err.emit(str(e))


	def add_col(self,s,t1,t2,t3,t4):
		self.adding_col = ColumnWindow(1,s,t1,t2,t3,t4)
		#self.adding_col.ok.connect(lambda: self.table.setColumnCount(int(self.table.columnCount()+1)))
		self.adding_col.ok.connect(self.adding_colum)
		self.adding_col.ko.connect(lambda: self.adding_col.close())
		self.adding_col.show()

	def adding_colum(self, col_name, t1, t2, t3,t4,s):
		self.table.setColumnCount(int(self.table.columnCount()+1))
		conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
		cur_sql = conn.cursor()
		cur_sql.execute('SELECT * FROM '+str(s))
		self.table.setHorizontalHeaderLabels([t[0] for t in cur_sql.description])


	def del_col(self,s,t1,t2,t3,t4):
		self.deling_col = ColumnWindow(0,s,t1,t2,t3,t4)
		self.deling_col.ok.connect(lambda: self.table.setColumnCount(int(self.table.columnCount()-1)))
		self.deling_col.ko.connect(lambda: self.deling_col.close())
		self.deling_col.show()
			
class ColumnWindow(QDialog):
    ok = QtCore.pyqtSignal(str, str, str, str, str, str)
    ko = QtCore.pyqtSignal()
    err = QtCore.pyqtSignal(str)
    def __init__(self,a,s,t1,t2,t3,t4):
        QDialog.__init__(self)
        self.setMaximumSize(QtCore.QSize(480, 640))
        self.setMinimumSize(QtCore.QSize(480, 640))
        self.setStyleSheet("""background: rgb(75, 105, 240)""")
        self.frame =QFrame(self)
        self.frame.move(45, 35)

        if a == 1:
        	self.setWindowTitle('Adding a new column')
        	self.main_label = QLabel('<p align="center">Adding column.</p>', self)

        	self.col_line = QLineEdit('', self)
        	self.col_line_label = QLabel('Name of the new column:',self)

        	self.col_type_label = QLabel('Type of the new column:',self)
        	self.col_type = QComboBox(self)
        	self.col_type.addItem('text')
        	self.col_type.addItem('integer')
        	self.col_type.addItem('char')

        	self.n_null_label = QLabel('Not null? ',self)
        	self.n_null = QComboBox(self)
        	self.n_null.addItem('Yes')
        	self.n_null.addItem('No')

        	self.p_k_label = QLabel('Primary key? ',self)
        	self.p_k = QComboBox(self)
        	self.p_k.addItem('No')
        	self.p_k.addItem('Yes')

        	self.def_line_label = QLabel('Default value of column',self)
        	self.def_line = QLineEdit('Default value', self)

        	x1 = 55
        	x2 = 285
        	x3 = 72+x2
        	self.main_label.move(0, 0)
        	self.col_line_label.move(x1, 50)
        	self.col_line.move(x2, 48)
        	self.col_type_label.move(x1, 150)
        	self.col_type.move(x3, 148)
        	self.n_null_label.move(x1, 250)
        	self.n_null.move(x3, 248)
        	self.p_k_label.move(x1, 350)
        	self.p_k.move(x3, 348)
        	self.def_line_label.move(x1,400)
        	self.def_line.move(x2, 398)

        	self.col_type.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
        	self.col_type_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
        	self.n_null.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
        	self.n_null_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
        	self.p_k.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
        	self.p_k_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
        	self.def_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
        	self.def_line_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)

        else:
        	self.setWindowTitle('Deleting column')
        	self.col_line_label = QLabel('Name of the column to delete:',self)
        	self.col_line = QLineEdit('', self)
        	self.main_label = QLabel('<p align="center">Deleting column.</p>', self)

        	x1 = 55
        	x2 = 285
        	self.main_label.move(0, 0)
        	self.frame.move(x1-10, 35)
        	self.col_line_label.move(x1, 50)
        	self.col_line.move(x2, 48)

        self.ok_button = QPushButton('Ok', self)
        self.ko_button = QPushButton('Cancel', self)
        self.ok_button.move(80, 450)
        self.ko_button.move(300, 450)
        self.col_line_label.setStyleSheet("""background-color: rgb(255, 255, 255); font-size: 14px; font: "Times New Roman" """)
        self.col_line.setStyleSheet("""font-size: 14px; border-radius: 4px; background-color: rgb(240, 240, 240); min-width: 50; min-height: 24; border: 1px solid rgb(100,100,100)""")
        self.main_label.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 24px; color: rgb(255, 255, 255); font: bold "Times New Roman"; border-radius: 5px; min-width: 480; min-height: 30; max-width: 480; max-height: 30""")
        self.frame.setStyleSheet("""background-color: rgb(255, 255, 255); min-height: 480; min-width: 390; border-radius: 8px """)
        self.ok_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 20px; color: rgb(255, 255, 255); font: "Times New Roman"; border-radius: 5px; min-width: 100; min-height: 24; max-width: 100; max-height: 24""")
        self.ko_button.setStyleSheet("""background-color: rgb(75, 105, 240); font-size: 20px; color: rgb(255, 255, 255); font: "Times New Roman"; border-radius: 5px; min-width: 100; min-height: 24; max-width: 100; max-height: 24""")
        
        if a == 1:
        	self.ok_button.clicked.connect(lambda: self.do_do(self.col_line.text(),self.col_type.currentText(),t1,t2,t3,t4,s,self.n_null.currentText(),self.p_k.currentText(),self.def_line.text()))
        elif a == 0:
        	self.ok_button.clicked.connect(lambda: self.do_do(self.col_line.text(),0,t1,t2,t3,t4,s,'','',''))
        self.ko_button.clicked.connect(lambda: self.ko.emit())
        


    def do_do(self, col_name, col_type, t1, t2, t3, t4,table_name,nn,pk,def_value):
        if col_type == 0:
            try:
                conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
                cur_sql = conn.cursor()
                s = 'ALTER TABLE '+table_name+' DROP COLUMN '+col_name
                cur_sql.execute(s)
                conn.commit()
                self.ok.emit(col_name, t1, t2, t3,t4,table_name)
                self.ko.emit()
            except Exception as e:
                print(e)

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
            		def_value = '0'
            		pass
            	conn = psycopg2.connect(dbname=t1, user=t2, password=t3, port=t4)
            	cur_sql = conn.cursor()
            	s = 'ALTER TABLE '+table_name+' ADD COLUMN '+col_name+' '+col_type+' default '+def_value+' '+nn+' '+pk
            	cur_sql.execute(s)
            	conn.commit()
            	self.ok.emit(col_name, t1, t2, t3,t4,table_name)
            	self.ko.emit()
            except Exception as e:
            	print(e)

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
    def show_auth(self, t1, t2, t3, t4):
    	try:
    		self.db.close()
    	except AttributeError:
    		pass
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
    	self.db.back.connect(self.show_auth)
    	self.db.err.connect(self.show_err)

    def show_err(self, t):
    	self.erroring = LoginError(t)
    	self.erroring.cl.connect(lambda: self.erroring.close())
    	self.erroring.show()

app = QApplication(sys.argv)
screen = Controller()
screen.show_login()
sys.exit(app.exec_())