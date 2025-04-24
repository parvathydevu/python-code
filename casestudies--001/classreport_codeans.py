#step 1
# Read the content
path = r"C:\Users\237237\Desktop\anacondacode\casestudies--001\student_report\students.csv"
f = open(path)
content = f.readlines()
f.close()

print("INFO -> step 1", content)

# Step 2
# Process the content and store in a data structure
# What data structure will be good here?-> Dictionary
# student_dict -> class_dict

class_dict = {}
columns = [item.strip() for item in content[0].split(',')] # Keys of the student dictionary
for dataitem in content[1:]:
    values = [item.strip() for item in dataitem.split(',')] # Values for the student dictionary
    student_dict = dict(zip(columns, values)) # Zipping keys and values to form the student dictionary
    class_dict[student_dict['regid']] = student_dict # Adding student dictionery to class dictionary


print("\n" + "-"*100)
print("INFO -> step 2 Registeration ID KEY \n", class_dict)
 
# Step 3
# Calculate the average
 
for key, value in class_dict.items():
    marks = [int(v) for k, v in value.items() if k not in ['name', 'age', 'regid', 'avg', 'rank']]
    average = sum(marks) / len(marks)  #sum(marks)/4.0
    class_dict[key]['avg'] = str(average) #average is added to the student dictionary under the key 'avg
 
print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)
 
# Step 4
# Calculate the rank
for k, v in class_dict.items(): # key is the registration ID of the student, and value is the student dictionary containing their details.
    rank = 1
    for k1, v1 in class_dict.items():
        if k != k1 and float(v1['avg']) > float(v['avg']):
            rank += 1
    class_dict[k]['rank'] = rank

# Sort students by rank in ascending order (highest average gets rank 1)
students_sorted = sorted(class_dict.values(), key=lambda x: x['rank'])

# Update ranks to be consecutive integers starting from 1
rank = 1
for student in students_sorted:
    student['rank'] = rank
    rank += 1

print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)

#Display the report
template = "{0:8} | {1:15} | {2:5} | {3:5} | {4:5} | {5:5} | {6:5} | {7:5} | {8:5}"

print("\nCLASS REPORT")
print('-'*90)
print(template.format('REGID', 'NAME', 'AGE', 'PHY', 'CHEM', 'MATH', 'BIO', 'AVG', 'RANK'))
print('-'*90)

# This iterates over each student dictionary in the sorted list students_sorted.
for student in students_sorted:
    regid = student['regid']
    name = student['name']
    age = student['age']
    phy = student['phy']
    chem = student['chem']
    math = student['math']
    bio = student['bio']
    avg = student['avg']
    rank = student['rank']
    print(template.format(regid, name, age, phy, chem, math, bio, avg, rank))


print('-'*90)

# Assuming students_sorted is defined and contains the sorted list of student dictionaries

# Task 2: Print the formatted report into a file - studentreport.txt
#FORMATED REPORT TO TXT file
with open('studentrep.txt', 'w') as txt_file:
    template = "{0:8} | {1:15} | {2:5} | {3:5} | {4:5} | {5:5} | {6:5} | {7:5} | {8:5}"
    txt_file.write("\nCLASS REPORT\n")
    txt_file.write('-'*90 + '\n')
    txt_file.write(template.format('REGID', 'NAME', 'AGE', 'PHY', 'CHEM', 'MATH', 'BIO', 'AVG', 'RANK') + '\n')
    txt_file.write('-'*90 + '\n')
    
    for student in students_sorted:
        regid = student['regid']
        name = student['name']
        age = student['age']
        phy = student['phy']
        chem = student['chem']
        math = student['math']
        bio = student['bio']
        avg = student['avg']
        rank = student['rank']
        txt_file.write(template.format(regid, name, age, phy, chem, math, bio, avg, rank) + '\n')
    
        txt_file.write('-'*90 + '\n')
#Txt to CSV file conversion
csv_content="regid, name, age, phy, chem, math, bio, avg, rank\n"
for student in students_sorted:
    csv_content += f"{student['name']},{student['age']},{student['regid']},{student['phy']},{student['chem']},{student['math']},{student['bio']},{student['avg']},{student['rank']}\n"

with open('studentrep.csv', 'w') as csv_file:
    csv_file.write(csv_content)




