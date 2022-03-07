"""
    Taylor J. Brown
    07MAR22
    file_Parse.py

    Opens a file and returns the parsed contents in a sorted dictionary
"""

from docx import Document
import csv

def main():
    # File path (will be changed when intergrated with flask app)
    file_P_CSV = "CSC_289_CAP.csv"
    file_P_DOCX = "CSC_289_CAP.docx"
    DATA_FORMATTED_CSV = []
    DATA_FORMATTED_DOCX = []
    CLASS_NAME = ""
    
    
    CLASS_NAME, DATA_FORMATTED_CSV = ParseCSV(file_P_CSV)
    # Prints each DATA_FORMATTED_CSV value in the CSV file  
    print(CLASS_NAME)     
    for item in DATA_FORMATTED_CSV:
        print(item , "\n")
        
    print()
    
    CLASS_NAME, DATA_FORMATTED_DOCX = ParseDOCX(file_P_DOCX)
    # Prints the objects in the list
    print(CLASS_NAME) 
    for item in DATA_FORMATTED_DOCX:
        print(item , "\n") 


def ParseCSV(file_P_CSV):
    # Strips the file extention and assigns it as the Class_name
    size = len(file_P_CSV)
    CLASS_NAME = file_P_CSV[:size - 4]
    
    # Parses the rows and makes the first row read the header and the subsequent rows the values for each header.
    with open(file_P_CSV, "r") as file:
        csvreader = csv.DictReader(file)
        DATA_FORMATTED_CSV = []
        for row in csvreader:
            DATA_FORMATTED_CSV.append(row)
            
    return CLASS_NAME, DATA_FORMATTED_CSV
        

def ParseDOCX(file_P_DOCX):
    # Passes the file through the docx method
    document = Document(file_P_DOCX)
    
    # Chops off the file extention and assigns it to the class name
    size = len(file_P_DOCX)
    CLASS_NAME = file_P_DOCX[:size - 5]
    
    # Rips the data from the table and appends each item to the list
    data = []
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                data.append(cell.text)

    # Assigns the row headers as keys for the following records
    data_keys = []
    data_keys.append(data[0])
    data_keys.append(data[1])
    data_keys.append(data[2])
    
    # Iterates through the list and appends the dictionary key value pairs to the DATA_FORMATTED list 
    DATA_FORMATTED_DOCX = []
    count = int((len(data) / 3) - 1)
    index = 3
    for _ in range(count):
        tmp = {}
        tmp[data_keys[0]] = data[index]
        tmp[data_keys[1]] = data[index + 1]
        tmp[data_keys[2]] = data[index + 2]
        index += 3
        DATA_FORMATTED_DOCX.append(tmp)

    return CLASS_NAME, DATA_FORMATTED_DOCX
                 

if __name__ == ("__main__"):
    main()
    