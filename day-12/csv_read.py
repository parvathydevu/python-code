import csv
path=r"C:\Users\237237\Desktop\anacondacode\day-12\casestudies002\data.csv"
with open(path,'r') as f:
  data = csv.reader(f)
  print('DATA TYPE: ', type(data))
  for row in data:
        print(row)


reader = csv.DictReader(open("data.csv"))
for raw in reader:
    print(dict(raw))