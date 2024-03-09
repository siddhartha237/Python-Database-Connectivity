import psycopg2
conn = None
def insertrecord(num,name,dept):
    try:
        #Connect to the postgresql database
        conn = psycopg2.connect(database='test',user='postgres',password='Sidhu237@',host='127.0.0.1',port='5432')
        cur=conn.cursor() # create a new cursor
        cur.execute('''insert into employee values(%s,%s,%s)''',(num,name,dept))
        conn.commit() #commit the changes 
        print('record is inserted successfully')
        cur.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection


insertrecord(112,'Siddhartha','IT')
insertrecord(113,'Dev','IT')
insertrecord(114,'Shraddha','IT')
insertrecord(115,'Roshani','IT')
insertrecord(116,'Ravi','IT')
insertrecord(117,'Archana','IT')