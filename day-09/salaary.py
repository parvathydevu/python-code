class Employee:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company
        self.gross_salary = 0
        self.tax_rate = 0
        self.net_salary = 0

    def calculate_net_salary(self):
        self.net_salary = self.gross_salary * (1 - self.tax_rate / 100)
        return self.net_salary

    def set_gross_salary(self, gross_salary):
        self.gross_salary = gross_salary
        self.calculate_net_salary()

    def set_tax_rate(self, tax_rate):
        self.tax_rate = tax_rate
        self.calculate_net_salary()

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Company: {self.company}")
        print(f"Gross Salary: {self.gross_salary}")
        print(f"Tax Rate: {self.tax_rate}%")
        print(f"Net Salary: {self.net_salary}")

# Example usage:
employee = Employee("John Doe", 30, "TechCorp")
employee.set_gross_salary(50000)
employee.set_tax_rate(20)
employee.print_information()