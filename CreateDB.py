from datetime import date
import tools
import sys, os



path_date = 'date/'

if not os.path.exists(path_date):
    os.mkdir(path_date)
    
tools.WriteInFile()
data = tools.ReadInFile()
tools.FindUrl(data)
tools.AllWorkInSecondPage()
tools.WriteInDB()