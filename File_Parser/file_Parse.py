"""
    Opens a file and returns the parsed contents in a sorted dictionary
"""

from docx import Document
import csv

def main():
    # File path (will be changed when intergrated with flask app)
    file_P_CSV = "CSC_289_CAP.csv"
    file_P_DOCX = "CSC_289_CAP.docx"
    
    ParseCSV(file_P_CSV)
    print()
    ParseDOCX(file_P_DOCX)


def ParseCSV(file_P_CSV):
    # Strips the file extention and assigns it as the Class_name
    size = len(file_P_CSV)
    CLASS_NAME = file_P_CSV[:size - 4]
    print(CLASS_NAME , "\n")
    
    # Parses the rows and makes the first row read the header and the subsequent rows the values for each header.
    with open(file_P_CSV, "r") as file:
        csvreader = csv.DictReader(file)
        ASSIGNMENTS = []
        for row in csvreader:
            ASSIGNMENTS.append(row)
        
    # Prints each assignments value in the CSV file       
    for item in ASSIGNMENTS:
        print(item , "\n")   


def ParseDOCX(file_P_DOCX):
    # Passes the file through the docx method
    document = Document(file_P_DOCX)
    
    # Chops off the file extention and assigns it to the class name
    size = len(file_P_DOCX)
    CLASS_NAME = file_P_DOCX[:size - 5]
    print(CLASS_NAME , "\n")
    
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
    
    # Iterates through the list and appends the dictionary sets to the data_formatted list 
    data_formatted = []
    count = int((len(data) / 3) - 1)
    index = 3
    for _ in range(count):
        tmp = {}
        tmp[data_keys[0]] = data[index]
        tmp[data_keys[1]] = data[index + 1]
        tmp[data_keys[2]] = data[index + 2]
        index += 3
        data_formatted.append(tmp)
        
    # Prints the objects in the list
    for item in data_formatted:
        print(item , "\n") 
        

if __name__ == ("__main__"):
    main()
    