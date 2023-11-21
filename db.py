import os
import psycopg2

conn = psycopg2.connect(database="flask_db",  
                        user="postgres", 
                        password="root",  
                        host="localhost", port="5432") 
  
cur = conn.cursor() 
  
conn.commit() 
  
cur.close() 
conn.close() 