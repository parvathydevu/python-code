#name, phone , email, job id

import os
import re

#to get the list of files to process
path= r"C:\Users\237237\Desktop\anacondacode\day-09\words1.txt"
os.chdir(path)

files=[file for file in os.lisdir() if os.splittext()[1:]=='txt']

#function to extract the data
email_pattern ="\w*@\w*"
def extract(file):
    fhandler=open(file)
    content=fhandler.read()
    #extract
    fhandler.search(email_pattern,content).group()