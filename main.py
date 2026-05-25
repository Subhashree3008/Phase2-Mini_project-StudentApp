import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="subbu*05"
)
mycursor=mydb.cursor()

class Student:
    def __init__(self,name,roll_no,branch,cgpa,email):
        self.name=name
        self.roll_no=roll_no
        self.branch=branch
        self.cgpa=cgpa
        self.email=email


    def create_db(self):

        try:
            sql=""" create database srmdb"""
            mycursor.execute(sql)
            print('DB created successfully')
        except Exception as err:
            print("Issue while creating db")

    def use_db(self):
        try:
            sql=""" use srmdb"""
            mycursor.execute(sql)
            print("DB selected")
        except Exception as err:
            print("Issue while select db")

    
    def create_table(self):
        try:
            self.use_db()
            sql="""create table student(
              name varchar(20), roll_no int primary key,
              branch varchar(10),cgpa decimal(3,2),email varchar(30)) """
            mycursor.execute(sql)
            print("Table Created successfully")
        
        except Exception as err:
            print("Issue while creating table")

    def insert_table(self,name,roll_no,branch,cgpa,email):
        try:
            self.use_db()
            sql="""insert into student(name,roll_no,branch,cgpa,email) 
            values(%s,%s,%s,%s,%s)
   """
            values = (name, roll_no, branch, cgpa, email)
            mycursor.execute(sql,values)
            mydb.commit()
            print("data inserted successfully")
        
        except Exception as err:
            print("Issue while inserting table")

    
    def view_students(self):
        try:
            self.use_db()
            sql="""select * from student"""
            mycursor.execute(sql)
            rows=mycursor.fetchall()

            print("\n-----------Student Details-----------\n")
            for row in rows:
                print(row)
        except Exception as err:
            print("Issue while fetching details")


            
    def view_student_by_roll(self,roll_no):
        try:
            self.use_db()
            sql="""select * from student where roll_no=%s"""
            values=(roll_no,)
            mycursor.execute(sql,values)
            row=mycursor.fetchone()

            print(f"\n-----------Student Detail By Roll {roll_no}-----------\n")
            print(row)
        except Exception as err:
            print("Issue while fetching detail")

    
    def update_students(self,cgpa):
        try:
            self.use_db()
            sql="""select * from student where cgpa=%s"""
            values=(cgpa,)
            mycursor.execute(sql,values)
        except: 
            









s1=Student("",0,"",0.0,"")
s1.create_db()
s1.create_table()
s1.insert_table()
s1.view_students()
s1.view_student_by_roll(622)