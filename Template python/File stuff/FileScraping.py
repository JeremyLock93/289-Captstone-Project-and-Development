# import urllib2  # the lib that handles the url stuff
# data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
## VSCODE not recognized
### NOT TESTED YET
import urllib.request  # the lib that handles the url stuff

target_url = input("Enter the url file:")
data = urllib.request.urlopen(target_url)
data = data.split("\n") # then split it into lines
for line in data:
    print(line.decode('utf-8')) #utf-8 or iso8859-1 or whatever the page encoding scheme is

# file = open(data, "r")
with open('words.txt','r') as f:
    for line in f:
        for word in line.split():
           print(word)  
           

  
