def DisplayMenu():
    print("File Creation")
    print("______________")
    print("1)	Create .txt file")
    print("2)	Create .docx file")
    print("3)	Create .csv file")
    print("4)	Exit")
    print()
def main():
    ''' This menu function is formatted to prevent error '''
    arr = []
    loop = '1'
    while loop == '1':
        DisplayMenu()
        selection = input("Choose one of the menu options: ")
        if selection == '1':
            num1 = 1
            file = files(num1)
            Create(file)
        elif selection == '2':
            num1 = 2
            file = files(num1)
            Create(file)
        elif selection == '3':
            num1 = 3
            file = files(num1)
            Create(file)       
        elif selection == '4':
            loop = '2'
            print()
            print("Bye!")
            ##raise SystemExit(0)#exit feature for spyder#REMOVED
        else:
            print("Invalid input/choice. Choose within 1-5")
        print()

def files(num):
    if num == 1:
        file = "guru99.txt"
        return file
    elif num == 2:
        file = "guru99.docx"
        return file
    elif num == 3:
        file = "guru99.csv"
        return file
    
def Create(file):
     with open(file,"w+") as f:
        for i in range(10):
            f.write("This is line %d\r\n" % (i+1))
     #read file for verification
     with open(file,"r") as f:       
        for line in f.readlines():
            print(line)
            """ for word in line.split():
               print(word)  """  
if __name__== "__main__":
  main()