#Lord Jenar Adolph C Allan
# 07MAR2022
#CSC-289-0B01

#Import Module
import os
import csv

##File imports
import File_Parser
import File_Writing



def DisplayMenu():
    print("Filers")
    print("______________")
    print("1)	Create .csv file")
    print("2)	Create .docs file")
    print("3)   Parse your files in dictionary.")
    print("4)	Exit")
    print()
def main():
    ''' This menu function is formatted to prevent error '''
    # Folder Path
    user_input = "E:\\Jenar's FTCC Book and Homework\\FTCCSpring2022\\Programming Capstone Project (CSC-289-0B01)\\Template python\\filefolder"
    # Verify the path if it's valid
    assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)
        
    loop = '1'
    while loop == '1':
        DisplayMenu()
        selection = input("Choose one of the menu options: ")
        if selection == '1':
            for filename in os.listdir(user_input):
                f = os.path.join(user_input, filename)
                if os.path.isfile(f) and filename.endswith(".csv"): # Check whether file is in csv format or not
                    CLASS_NAME, DATA_FORMATTED = File_Parser.ParseCSV(f)
                    num1 = 1
                    file = File_Writing.files(num1)
                    File_Writing.CreateCSV(user_input,file, CLASS_NAME, DATA_FORMATTED)
        elif selection == '2':
            for filename in os.listdir(user_input):
                f = os.path.join(user_input, filename)
                if os.path.isfile(f) and filename.endswith("ocx"): # Check whether file is in docx format or not
                    CLASS_NAME, DATA_FORMATTED = File_Parser.ParseDOCX(f)
                    num1 = 2
                    file = File_Writing.files(num1)
                    File_Writing.CreateDOCX(user_input,file, CLASS_NAME, DATA_FORMATTED)
        elif selection == '3':
            # Folder Path
            user_input = input("Enter Folder/File Path:")
            # Verify the path if it's valid
            assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)
            Parsers(user_input)
        elif selection == '4':
            loop = '0'
            print()
            print("Bye!")
            exit
            ##raise SystemExit(0)#exit feature for spyder#REMOVED
        else:
            print("Invalid input/choice. Choose within 1-4")
        print()
        
def Parsers(user_input):
    for filename in os.listdir(user_input):
        f = os.path.join(user_input, filename)
        if os.path.isfile(f) and filename.endswith(".csv"): # Check whether file is in csv format or not
            # call read file function
            #print(f)#Test print path
            Print(f)
        elif os.path.isfile(f) and filename.endswith(".docx"): # Check whether file is in docx format or not
            # call read file function
            #print(f)#Test print path
            Print(f)

def Print(f):
    CLASS_NAME, DATA_FORMATTED = File_Parser.ParseCSV(f)
    print(CLASS_NAME)     
    for item in DATA_FORMATTED:
        print(item , "\n")
        
    
#return CLASS_NAME, DATA_FORMATTED
if __name__ == ("__main__"):
    main()
