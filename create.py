import psycopg2
def createtable():
    conn = None
    try:
        # connect to postgresql database
        conn = psycopg2.connect(database='test',user='postgres',password='Sidhu237@',host='127.0.0.1',port='5432')
        cur=conn.cursor() # create a new cursor
        cur.execute('''create table employee( emp_num int primary key,
                    emp_name varchar(40) not null,
                    department varchar(40))''')
        conn.commit() #commit the changes to the database
        print("Table created successfully")
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection 

createtable()