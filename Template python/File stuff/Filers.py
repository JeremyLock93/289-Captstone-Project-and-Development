#Import Module
import sys
import os

  
# Folder Path
user_input = input("Enter Folder/File Path:")
  
# Verify the path if it's valid
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

#Dictionary Storage ##how to implement for usage?
Storage = {}

# Read File
def read_file(file_path):
    #index
    index1 = -1
    index2 = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            print(line)
        #     for word in line.split(): Figuring how to split and append it to an empty dictionary
        #         index1 += 1
        #         keys = word[index1]
        #     for word in line.split():
        #         index2 += 1
        #         values = word[index2]
        # Storage[keys] = values#Dictionary append        
        # print(Storage)#for verification  
         
# iterate through all file
for filename in os.listdir(user_input):
    f = os.path.join(user_input, filename)
    if os.path.isfile(f) and filename.endswith(".txt"): # Check whether file is in text format or not
        # call read file function
        print(f)
        read_file(f)
    elif os.path.isfile(f) and filename.endswith(".docx"): # Check whether file is in docx format or not
        # call read file function
        print(f)
        read_file(f)  
    elif os.path.isfile(f) and filename.endswith(".csv"): # Check whether file is in csv format or not
        # call read file function
        print(f)
        read_file(f)
    # elif file.endswith(file):
    #     file_path = f"{path}\{file}"
  
    #     # call read file function
    #     read_file(file_path)
    else:
        pass
    
#f = open(user_input,'r+')
#print("Hooray we found your file!")