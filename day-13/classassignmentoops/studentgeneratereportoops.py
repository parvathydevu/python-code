from students import Student
import json
from operator import methodcaller, attrgetter
 
 
# Read the contents
 
 
student_data = []
 
# with open("students.csv", "r") as csvdata:  # context manager
#     content = csv.DictReader(csvdata)
#     for row in content:
#         student_data.append(row)
 
#read from json file
path = r'C:\Users\237237\Desktop\anacondacode\day-13\classassignmentoops\students.json'
with open(path,'r') as content:
    student_data = json.load(content)  #json load
 
 
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
avgs = sorted(list(set(avgs)), reverse=True)
ranks = [student.set_rank(avgs.index(getattr(student, 'average')) + 1) for student in students]
 
print(avgs, ranks)
 
'''
# alternative to getattr()
a = attrgetter('average')(students[0])
print("INFO ", a)
'''
 
 
# Write data to the report
 
#with open('studentreport-oop.json', 'w', newline='') as jsonfile:
    #reportwriter = csv.writer(csvfile, delimiter=',')
    #for student in students:                      
    #reportwriter.writerow(student.__str__().split(','))
    #json.dump(students,jsonfile)
    #Ensures the file is ready for writing and will be closed properly.

#Converts each student object to a dictionary.--__dict__ constructor
#Saves the list of student dictionaries to the file with readable formatting.

with open("student_report1.json", 'w') as jsonfile:
    json.dump([student.__dict__ for student in students], jsonfile, indent=4)
   
 