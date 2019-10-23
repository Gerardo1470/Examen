import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtSql
import sqlite3
from example import Ui_MainWindow

class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.create_DB()
        self.model = None
        self.ui.pushButton_viewdata.clicked.connect(self.sql_tableview_model)
        self.ui.pushButton_addRow.clicked.connect(self.sql_add_row)
        self.ui.pushButton_deleteRow.clicked.connect(self.sql_delete_row)
       

        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
        else:
            self.sql_tableview_model()       
                
    #----------------------------------------------------------
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    #----------------------------------------------------------
    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('COURSE.db')
        
        tableview = self.ui.tableView
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        
        self.model.setTable('CURSO')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Cod_curso")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Nom_Curso")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Modalidad")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Lugar")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Jornada")


    #----------------------------------------------------------
    def print_data(self):
        sqlite_file = 'COURSE.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'CURSO' ORDER BY ID")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       # not needed when only selecting data
        conn.close()        
        
    #----------------------------------------------------------
    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('COURSE.db')
        db.open()
        
        query = QtSql.QSqlQuery()
          
        query.exec_("create table CURSO(ID int primary key, "
                    "Nom_curso varchar(35), Modalidad varchar(25),  Lugar varchar(30),  Jornada int(15))")
        query.exec_("insert into CURSOvalues(1444, 'Introduccion a derecho', 'Vespertino', 'Edificio A', '8 am)")
        query.exec_("insert into CURSO values(3333, 'Dibujo tecnico', 'Matutino', 'Edificio D', '9 am')")
        query.exec_("insert into CURSO values(1470, 'Princpios de IoT', 'Matutino', ''Edificio F', '11 am')")
        query.exec_("insert into CURSO values(2220, 'Optativa I, 'Vespertino', 'Edificio F', '4 pm')")


if __name__ == "__main__":
    MainWindow_EXEC()



