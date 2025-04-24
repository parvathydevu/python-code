from student import students
 
class studentManager(object):
   
    def __init__(self):
        self.stds =[]
       
    #add a student
    def add_std(self,name,age,grade):
        student = students(name,age,grade)
        self.stds.append(student)
        return student
   
    #View all student
    def get_all_std(self):
        return self.stds
   
   
    #search by ID
    def search_ID(self,id):
        for students in self.stds:
            if students.id == id:
                return students
            return  None
   
   
    #Delete student
    def delete_std(self,id):
        for students in self.stds:
            if students.id == id:
                self.stds.remove(students)
                return True
            return False
   
    #load tasks
    def load_std(self,std_dicts):
        self.stds = [students.from_dict(td) for td in std_dicts]
       
    #list of tasks in dictionary format
    def to_dict_list(self):
        return [students.to_dict() for students in self.stds]