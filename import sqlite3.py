import sqlite3
connection = sqlite3.connect('test4ForOrderingSystem.db')

cursor = connection.cursor()
""":param create_table_sql: a CREATE TABLE statement
:return:"""
cursor.execute("""CREATE TABLE IF NOT EXISTS SAUSAGES (
                                    name TEXT
                                    
                                );""")
               

cursor.execute("INSERT INTO SAUSAGES VALUES(:sausages)",

                {

                'sausages':"Sausages",


                })

connection.commit()


connection.close()
