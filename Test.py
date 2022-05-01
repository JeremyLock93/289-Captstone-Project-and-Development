"""
    Taylor J. Brown
    30APR22
    
    This is a tester file for user data to be returned to the calling function for displaying 
    the users information on the profile page of the website.    
"""

def main():
    userRecord = Test()
    
    for value in userRecord:
        print(value)


def Test():
    USID = 1
    UserName = 'Admin'
    lastname = 'Templiholics'
    firstname = 'Pythonese'
    email = 'admin@Pythonese.com'
    password = 'We_Are_A_Team$50'
    affiliation = 'A'
    datecreated = '2022-04-28 02:59:24'
    return(USID,UserName,lastname,firstname,email,password,affiliation,datecreated)


if __name__ == '__main__':
    main()