"""
    Opens a file and returns the parsed contents in a sorted dictionary
"""


import csv
def main():
    # File path (will be changed when intergrated with flask app)
    file_P = "CSC_289_CAP.csv"
    
    # Strips the file extention and assigns it as the Class_name
    size = len(file_P)
    CLASS_NAME = file_P[:size - 4]
    print(CLASS_NAME , "\n")
    
    # Parses the rows and makes the first row read the header and the subsequent rows
    #   the values for each header.
    with open(file_P, "r") as file:
        csvreader = csv.DictReader(file)
        ASSIGNMENTS = []
        for row in csvreader:
            ASSIGNMENTS.append(row)
        
    # Prints each assignments value in the CSV file       
    for item in ASSIGNMENTS:
        print(item , "\n")


if __name__ == ("__main__"):
    main()
    