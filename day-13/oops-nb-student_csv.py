from students import Student
import csv
from operator import methodcaller, attrgetter

#main code 2nd 
# Read the contents 


student_data = []
path=r"C:\Users\237237\Desktop\anacondacode\day-13\students.csv"
with open(path, "r") as csvdata:  # context manager-
    content = csv.DictReader(csvdata)
#The csv.DictReader is a class in Python's csv module that reads CSV files and maps the information in each row to a dictionary. Each row read from the CSV file is returned as a dictionary,
#  where the keys are the column names and the values are the data from that row.
    for row in content:
        student_data.append(row)
    

# Create a list of student objects
students = []
for data in student_data:
    temp = Student(data['name'], data['regid'], data['age'])
    temp.set_marks(phy=data['phy'], chem=data['chem'], bio=data['bio'], math=data['math'])
    students.append(temp)

print(type(students[0])) # output if __repr__ not defined-> <class 'students.Student'>
print(students[0]) # output if __str__ not defined -> <students.Student object at 0x000002076AE82F30>

# Calculate average and rank

avgs = list(map(methodcaller('calculate_average'), students))
avgs = sorted(list(set(avgs)), reverse=True) #got unique average 
#ranks-> updated based on average marks.
ranks = [student.set_rank(avgs.index(getattr(student, 'average')) + 1) for student in students] 
#take ranks based on index values[[0][1][2][3]]--from sorted avg-highest marks got rank first

print(avgs, ranks)

'''
# alternative to getattr()
a = attrgetter('average')(students[0])
print("INFO ", a)
'''


# Write data to the report
with open('studentreport-oop.csv', 'w', newline='') as csvfile:  #automatically develop a csv file name with mentioned here
    reportwriter = csv.writer(csvfile, delimiter=',')
    for student in students:                       
        reportwriter.writerow(student.__str__().split(','))  #gives list --writed .
    