[x] CSV files read and assigned to correct variables
[x] DOCX files read and assigned to correct variables

[ ] Create CSV files with imported values
[ ] Create DOCX files with imported values

[ ] Integrate with flask app to get and post information to the templates


To use this file firstly

'import file_Parser as fp'

Then call the internal methods as such

'fp.ParseCSV(file.csv)'

--or--

'fp.ParseDOCX(file.docx)'


The return values types are (String, List(nested dictionaries))


Example: 

File sent to ParseCSV: "CSC_289_CAP.csv"

--Returned values--

CLASS_NAME:
CSC_289_CAP 

DATA_FORMATTED_CSV:
[{'Assignment': 'M1HW1', 'Due-Date': '21-Jan-22', 'Comment': 'Upload a picture of your Github activity.'},   

{'Assignment': 'M1HW2', 'Due-Date': '30-Jan-22', 'Comment': 'Upload your groups power point presentation.'},

{'Assignment': 'M2HW1', 'Due-Date': '5-Feb-22', 'Comment': 'Upload a word document about your sprint.'}]
