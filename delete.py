import psycopg2
conn = None
def deleterecord(num):
    try:
        conn = psycopg2.connect(database='test',user='postgres',password='Sidhu237@',host='127.0.0.1',port='5432')
        cur = conn.cursor() # create a new cursor
        cur.execute('''delete from employee where emp_num= %s ''',(num,))
        conn.commit() # commit the changes to the database
        print('record is deleted')
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

deleterecord(113)