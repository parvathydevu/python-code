# Step 1
# Read the content
import json

path = r"C:\Users\237237\Desktop\anacondacode\day-13\classassignment\students.json"
with open(path, 'r') as f:
    content = json.load(f)


print("INFO -> step 1", content)

# Step 2
# Step 2: Process the content and store in a data structure
class_dict = {}
for student_dict in content:
    class_dict[student_dict['regid']] = student_dict  # Adding student dictionary to class dictionary

print("\n" + "-"*100)
print("INFO -> step 2 \n", class_dict)

# Step 3
# Calculate the average

for regid in class_dict.keys():
    sum_of_subjects = float(class_dict[regid]['phy']) + float(class_dict[regid]['chem']) + \
                      float(class_dict[regid]['math']) + float(class_dict[regid]['bio'])
    class_dict[regid]['avg'] = sum_of_subjects / 4


print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank

avgs = [class_dict[regid]['avg'] for regid in class_dict.keys()]
avgs.sort(reverse=True)

for regid in class_dict.keys():
    class_dict[regid]['rank'] = avgs.index(class_dict[regid]['avg']) + 1

print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)

# Step 5
# Display the report

template = "{0:8} | {1:15} | {2:5} | {3:5} | {4:5} | {5:5} | {6:5} | {7:5} | {8:5}"
line = '-'*90

print("\nCLASS REPORT")
print(line)
print(template.format('REGID', 'NAME', 'AGE', 'PHY', 'CHEM', 'MATH', 'BIO', 'AVG', 'RANK'))
print(line)
for regid in class_dict.keys():
    name = class_dict[regid]['name']
    id = class_dict[regid]['regid']
    age = class_dict[regid]['age']
    phy = class_dict[regid]['phy']
    chem = class_dict[regid]['chem']
    math = class_dict[regid]['math']
    bio = class_dict[regid]['bio']
    avg = class_dict[regid]['avg']
    rank = class_dict[regid]['rank']
    print(template.format(id, name, age, phy, chem, math, bio, avg, rank))
  
print(line)
# Write student_report.json file
#prepare the data
report_data = {
    "header": ["REGID", "NAME", "AGE", "PHY", "CHEM", "MATH", "BIO", "AVG", "RANK"],
    "report": []
}
for regid, student in class_dict.items():  #append data in dictionary format-report
    report_data["report"].append({
        "REGID": student['regid'],
        "NAME": student['name'],
        "AGE": student['age'],
        "PHY": student['phy'],
        "CHEM": student['chem'],
        "MATH": student['math'],
        "BIO": student['bio'],
        "AVG": student['avg'],
        "RANK": student['rank']
    })

with open('student_report.json', 'w') as json_file:
    json.dump(report_data, json_file, indent=4)

print("Class report written to 'student_report.json'")

print("\nINFO -> step 6 -> Report written to student-report.json")