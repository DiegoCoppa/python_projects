
import mysql.connector
import csv

dataBaseName = "dccDummy"
thehost="localhost"
theuser="diego"
thepass="rojo6667"


table1 = "dccdepts"
table2 = "dccusers"
table3 = "dccprocs"
table3 = "dcccerts"

archivoDepts = 'dccDepts.new.csv'
archivoUsers = 'dccUsers.new.csv'
archivoProcs = 'dccProcs.new.csv'
archivoCert = 'dccCerts.new.csv'

sqlCreateDepts = "CREATE TABLE DccDepts ( \
            DeptoId INT NOT NULL PRIMARY KEY AUTO_INCREMENT, \
            DccDept VARCHAR(20) NOT NULL UNIQUE, \
            DccCentro VARCHAR(20) NOT NULL, \
            PermisosDept INT(2), \
            centro_costo INT(3), \
            pubdate datetime(6) NOT NULL \
            );"

sqlCreateUsers = "CREATE TABLE DccUsers ( \
            %s INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            DccUser VARCHAR(150) NOT NULL UNIQUE,\
            DccPermisosUser INT(20),\
            DccIdBelongDept INT, \
            FOREIGN KEY (DccIdBelongDept) REFERENCES DccDepts(DeptoID),\
            DccNombreFull VARCHAR(150) NOT NULL, \
            DCCEmail  VARCHAR(150) NOT NULL, \
            DccPassFull VARCHAR(8) NOT NULL, \
            pubdate datetime(6) NOT NULL \
            ); ","UserId"

sqlCreateProcs = "CREATE TABLE DccProcs ( \
            ProcId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            DccProcNominacion VARCHAR(20) NOT NULL UNIQUE,\
            DccIdDeptLinked INT),\
            FOREIGN KEY (DccIdDeptLinked) REFERENCES DccDepts(DeptoID),\
            DccRootFolder char(100),\
            );"

sqlCreateCerts = "CREATE TABLE DccCerts ( \
            CertID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            Tipo INT NOT NULL UNIQUE,\
            NúmeroDeCertificado INT(20),\
            NúmeroDeParcial INT,\
            UserResponsable INT, \
            FOREIGN KEY (UserResponsable) REFERENCES DccUsers(UserId),\
            ProcId INT, \
            FOREIGN KEY (ProcId) REFERENCES DccProcs(ProcId),\
            pubdate datetime(6) NOT NULL \
            );"
    

sqlInsertDccDepts = "INSERT INTO DccDepts(DeptoId, DccDept, DccCentro,PermisosDept,pubdate, centro_costo ) VALUES(%s,%s,%s,%s,%s,%s);"
sqlInsertDccUsers = "INSERT INTO DccUsers(%s, DccUser, DccPermisosUser,DccIdBelongDept,DccNombreFull,DccPassFull, DccEmail,pubdate)" , "UserId" + "VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
sqlInsertDccProcs = "INSERT INTO DccProcs(ProcId, DccProcNominacion, DccIdDeptLinked,DccRootFolder) VALUES(%s,%s,%s,%s);"
sqlInsertDccCerts = "INSERT INTO DccCerts(CertId, DccDept, DccCentro,PermisosDept,pubdate, centro_costo ) VALUES(%s,%s,%s,%s,%s,%s);"

def dataBaseConnection():
    try:
        mydb = mysql.connector.connect(
        host=thehost,
        user=theuser,
        password=thepass,
        database = dataBaseName
        )
        
        cursor = mydb.cursor()
        sql = "DROP DATABASE %s" %dataBaseName
        cursor.execute(sql)
        print("Existe base")
    
    except:       
        mydb = mysql.connector.connect(
        host=thehost,
        user=theuser,
        password=thepass
        )
        print ("no database %s " % dataBaseName )
    
    #creo la db
    cursor = mydb.cursor()
    sql = "CREATE DATABASE %s " % dataBaseName
    cursor.execute(sql)
    
    #Uso la db
    cursor = mydb.cursor()
    sql = "USE %s;" %dataBaseName
    cursor.execute(sql)
    
    return(mydb)
    
def insertDcc(mydb,archivo,sqlCreateForm):
    cursor = mydb.cursor()
    #creo la tabla    
    cursor.execute(sqlCreateForm)

    #leo el archivo    
    with open(archivo, 'r') as f:
        file_read = csv.DictReader(f)
        ordered_dict=list(file_read)
        #print(ordered_dict)
        #print(ordered_dict[1].keys())
        #print(ordered_dict[1].value())
    return(ordered_dict)

def guardar_db_depts(ordered_dict,mydb,sqlInfo):
    cursor = mydb.cursor()
    try:
        for row in ordered_dict:
            args = str(row['id']) , str(row['dcc_dept']) , str(row['dcc_centro']) , str(row['dcc_PermisosDept']) , str(row['pub_date'])
            print(sqlInfo,args)
            cursor.execute(sqlInfo,args)
        mydb.commit()
    except: print("error depts")

def guardar_db_users(ordered_dict,mydb,sqlInfo):
    cursor = mydb.cursor()
    try:
        for row in ordered_dict:
            #sqlInsertDccUsers = "INSERT INTO DccUsers(UserID, DccUser, DccPermisosUser,DccBelongDept,DccNombreFull,DccPassFull, DccEmail,pubdate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
            args = str(row['id']) , str(row['dcc_user']), str(row['dcc_PermisosUser'])  , str(row['dcc_belong_Dept_id']) , str(row['dcc_nombre_full']) , str(row['dcc_pass_full']) , str(row['Email']) , str(row['pub_date'])
            #print(sqlInfo,args)
            cursor.execute(sqlInfo,args)
        mydb.commit()
    except: print("error users")

def guardar_db_certs(ordered_dict,mydb,sqlInfo):
    cursor = mydb.cursor()
    try:
        for row in ordered_dict:
            #sqlInsertDccUsers = "INSERT INTO DccUsers(UserID, DccUser, DccPermisosUser,DccBelongDept,DccNombreFull,DccPassFull, DccEmail,pubdate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
            args = str(row['id']) , str(row['dcc_user']), str(row['dcc_PermisosUser'])  , str(row['dcc_belong_Dept_id']) , str(row['dcc_nombre_full']) , str(row['dcc_pass_full']) , str(row['Email']) , str(row['pub_date'])
            #print(sqlInfo,args)
            cursor.execute(sqlInfo,args)
        mydb.commit()
    except: print("error users")





"""
def verifica_escritura (table,mydb):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM " +table
    cursor.execute(sql)
    #rows = cursor.fetchall()
    #print(rows)
"""
    
def main():
    mydb=dataBaseConnection()
    guardar_db_depts(insertDcc(mydb,archivoDepts,sqlCreateDepts),mydb,sqlInsertDccDepts)
    guardar_db_users(insertDcc(mydb,archivoUsers,sqlCreateUsers),mydb,sqlInsertDccUsers)

if __name__ == "__main__":
    main()