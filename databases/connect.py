from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# engine = create_engine("mysql:///?User=root&Password=root&Database=db_pengolahan_nilai&Server=localhost&Port=3306")
# factory = sessionmaker(bind=engine)
# session = factory()

sqlEngine       = create_engine('mysql+pymysql://root:root@127.0.0.1/db_pengolahan_nilai', pool_recycle=3600, pool_size=50, max_overflow=50)
dbConnection    = sqlEngine.connect()


def Sql_Get_Table(sql_query):    
  result_dataFrame = pd.read_sql(sql_query,dbConnection)
  return result_dataFrame

# Set up and end date of the employee
def SQL_FN_Employee_IsActive(employeeID):
  result = dbConnection.execute("select Employee_IsActive(" + str(employeeID) + ") ")
  for row in result:
    # Take note that in order to read the value this way, you must specify the name of the column
    # print(row["Employee_IsActive(" + str(employeeID) + ")"])
    if str(row["Employee_IsActive(" + str(employeeID) + ")"]) == "0":
      print("Employee is not longer active :S")
    else:
      print("Employee is still working with us :D")

def SQL_SP_Employee_EndDate(employeeID, endDate):
  dbConnection.execute("call Employee_ENDS(" + str(employeeID) + ", '" + endDate +"') ")

def SQL_Run_Query(query):
  dbConnection.execute(query)
  # dbConnection.execute("commit")

Table('mytable', metadata,
      Column('data', String(32)),
      mysql_engine='InnoDB',
      mysql_charset='utf8mb4',
      mysql_key_block_size="1024"
     )

# sql_Query_View = '''SELECT * FROM login'''
# SQL_Run_Query(sql_Query_View)