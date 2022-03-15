import pandas as pd



studentdict = {'studentname':[],'studentpass':[],'studentmajor':[]}

df = pd.Dataframe(studentdict)


studentinput1 = input("studentname: ")
studentinput2 = input("studentpass: ")
studentinput3 = input("studentmajor: ")

df.to_csv('student.csv')

