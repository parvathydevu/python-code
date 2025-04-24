import random
list1 = ['dinesh', 'vijaya', 'gomathi', 'priyanka',
         'gagana', 'abhijith', 'yashwanth', 'shwetha', 'sadhana',
         'mahesh', 'pranav', 'aleena', 'nithin', 'prathiksha', 'lakith', 'tamil', 'afif',
         'srinandan', 'akshay', 'parvathi', 'bincy', 'ponnulakshmi', 'ganga', 'krishnapriya', 'sanju', 'sourabh',
         'nimra', 'ramji', 'ananthan']
 
print(len(list1))
random.shuffle(list1)
 
group1 = list1[:3]
group2 = list1[3:6]
group3 = list1[6:9]
group4 = list1[9:12]
group5 = list1[12:15]
group6 = list1[15:18]
group7 = list1[18:21]
group8 = list1[21:24]
group9 = list1[24:27]
group10 = list1[27:30]
 
print("Group 1:", group1)
print("Group 2:", group2)
print("Group 3:", group3)
print("Group 4:", group4)
print("Group 5:", group5)
print("Group 6:", group6)
print("Group 7:", group7)
print("Group 8:", group8)
print("Group 9:", group9)