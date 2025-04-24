import uuid
 
class students:
   
    def __init__(self,name:str,age:int,grade:str,id=None):
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.age = age
        self.grade = grade
       
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'age':self.age,
            'grade':self.grade
        }
       
    @staticmethod
    def from_dict(data):
        return students(
            name = data['name'],
            age = data['age'],
            grade = data['grade'],
            id = data['id']
        )
       
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"