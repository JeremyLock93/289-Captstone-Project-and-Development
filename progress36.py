# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:34:15 2022

@author: pinka
"""


#demo connect to student/teacher database
import mysql.connector

cnx = mysql.connector.connect(user='', password='',
host='',
database='')

#demo menu placeholder
print("1) Access Student Assignments")
print("2) Add assignments")
print("3) Access Assignments(Teacher)")
print("4) Add assignments(Teacher)")
print("5) Exit")

#teacher list for students
teacher_list = []
student_list = []
#input for menu
student_input = input("")

if student_input == "1":
  display.teacherlist()
elif student_input == "2":
  with open('student.txt', 'w') as f:
    f.write('Add assignments here')
    #create function add student assignments from student change later
elif student_input == "3":
  display.student_list()
elif student_input == "4":
    with open('teacher.txt', 'w') as f:
    f.write('Add assignments here')
        #create function add student assignments from teache change later

cnx.close()
