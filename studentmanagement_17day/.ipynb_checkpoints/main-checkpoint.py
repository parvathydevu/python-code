from student_manager import studentManager
from storage import Storage
 
def display_std(details: list) -> None:
    if not details:
        print("No data to display")
    else:
        for i in details:
            print(f"{i.id},{i.name},{i.age},{i.grade}")
 
def main():
 
    manager = studentManager()
    store = Storage()
 
    saved_stds = store.load()
    manager.load_std(saved_stds)
 
    while True:
 
        print("TODO Application: ")
        print("\n1. Add student\n2. View all student\n3.Search student by ID\n4. Delete student\n5. Exit\n")
        choice = input("Choice -> ")
 
        if choice == '1':
            name = input("Enter a name: ")
            age = input("Enter the age: ")
            grade = input("Enter the grade: ")
            students = manager.add_std(name,age,grade)
            store.save(manager.to_dict_list())
            print(f"Student added with ID: {students.id}")
 
        elif choice == '2':
            display_std(manager.get_all_std())
        elif choice == '3':
            tid = input("Enter the ID to search: ")
            result = manager.search_ID(tid)
            if (result):
                print(result)
                store.save(manager.to_dict_list())
                print("Search data")
            else:
                print("Student ID not found")
               
        elif choice == '4':
            tid = input("Enter the ID to delete: ")
            if manager.delete_std(tid):
                store.save(manager.to_dict_list())
                print("std details Deleted")
            else:
                print("std ID not found")
        elif choice == '5':
            print("Goodbye !")
            break
        else:
            print("Invalid Choice")
 
if __name__ == "__main__":
 
    main()