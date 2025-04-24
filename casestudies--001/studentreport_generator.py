#Step 1
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
for k, v in class_dict.items(): #key is the registration ID of the student, and value is the student dictionary containing their details.
    rank = 1  
    for k1, v1 in class_dict.items():
        if k != k1 and float(v1['avg']) > float(v['avg']):
            rank += 1
    class_dict[k]['rank'] = rank
print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)

# Sort students by rank-in descending order
#This sorts the list of student dictionaries based on the value of the 'rank' key.
students_sorted = sorted(class_dict.values(), key=lambda x: x['rank'])
# print("\n", students_sorted)

# Display the report
print("\n" + "-"*100)
print("INFO -> step 5 -> Class Report\n")
print("-"*100)

#This iterates over each student dictionary in the sorted list students_sorted.
for student in students_sorted:
    print(f"RegID: {student['regid']},|, Name: {student['name']}, |,Average Marks: {student['avg']},| Rank: {student['rank']}")
