#Lord Jenar Adolph C Allan
# 07MAR2022
#CSC-289-0B01

#Import Module
import os
import csv
import json
##File imports
import File_Parser as fp



def DisplayMenu():
    print("Filers")
    print("______________")
    print("1)	Create .csv file")
    print("2)	Create .docs file")
    print("3)   Parse your files in dictionary.")
    print("4)	Create json file")
    print("5)	Exit")
    print()
def main():
    ''' This menu function is formatted to prevent error '''
    # Folder Path
    ### THIS FILE PATH MUST BE CHANGED BEFORE BEING USED
    basepath = "C:\\Users\\lord_\\289-Captstone-Project-and-Development(tmp)\\File_Parser\\TemplateFolder"
    #### WEB PATH
    #basepath = os.path.abspath("/home/Pythonese/mysite/TemplateFolder")
    # Verify the path if it's valid
    assert os.path.exists(basepath), "I did not find the directory at, "+str(basepath)
        
    loop = '1'
    while loop == '1':
        DisplayMenu()
        selection = input("Choose one of the menu options: ")
        if selection == '1':
            for filename in os.listdir(basepath):
                f = os.path.join(basepath, filename)
                if os.path.isfile(f) and filename.endswith(".csv"): # Check whether file is in csv format or not
                    CLASS_NAME, DATA_FORMATTED = fp.ParseCSV(f)
                    ##FileName
                    num1 = 1
                    ##Student Name
                    #student = ""
                    file = fp.files(num1)
                    fp.CreateCSV(basepath,file, CLASS_NAME, DATA_FORMATTED)
        elif selection == '2':
            for filename in os.listdir(basepath):
                f = os.path.join(basepath, filename)
                if os.path.isfile(f) and filename.endswith("ocx"): # Check whether file is in docx format or not
                    CLASS_NAME, DATA_FORMATTED = fp.ParseDOCX(f)
                    ##FileName
                    num1 = 2
                    #StudentName
                    file = fp.files(num1)
                    fp.CreateDOCX(basepath,file, CLASS_NAME, DATA_FORMATTED)
        elif selection == '3':
            # Folder Path
            basepath = input("Enter Folder/File Path:")
            # Verify the path if it's valid
            assert os.path.exists(basepath), "I did not find the directory at, "+str(basepath)
            Parsers(basepath)
        elif selection == '4':
            #JSON CREATION
            for filename in os.listdir(basepath):
                f = os.path.join(basepath, filename)
                if os.path.isfile(f) and filename.endswith(".csv"): # Check whether file is in csv format or not
                    CLASS_NAME, DATA_FORMATTED = fp.ParseCSV(f)
                    num1 = 4
                    file = fp.files(num1)
                    fp.Create_JSON(basepath,file, CLASS_NAME, DATA_FORMATTED)
        elif selection == '5':
            loop = '0'
            print()
            print("Bye!")
            exit
            ##raise SystemExit(0)#exit feature for spyder#REMOVED
        else:
            print("Invalid input/choice. Choose within 1-4")
        print()

def PrintCSV(f):
    CLASS_NAME, DATA_FORMATTED = fp.ParseCSV(f)
    print(CLASS_NAME)     
    for item in DATA_FORMATTED:
        print(item , "\n")
        
def PrintDOCX(f):
    CLASS_NAME, DATA_FORMATTED = fp.ParseDOCX(f)
    print(CLASS_NAME)     
    for item in DATA_FORMATTED:
        print(item , "\n")
        
def Parsers(basepath):
    for filename in os.listdir(basepath):
        f = os.path.join(basepath, filename)
        if os.path.isfile(f) and filename.endswith(".csv"): # Check whether file is in csv format or not
            # call read file function
            #print(f)#Test print path
            PrintCSV(f)
        elif os.path.isfile(f) and filename.endswith(".docx"): # Check whether file is in docx format or not
            # call read file function
            #print(f)#Test print path
            PrintDOCX(f)
    
    
#return CLASS_NAME, DATA_FORMATTED
if __name__ == ("__main__"):
    main()
