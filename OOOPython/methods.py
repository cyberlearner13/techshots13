class Employee:
    def __init__(self,name):
        self.name = name
    def displayEmployeeDetails(self):
        print(self.name)
    @staticmethod
    def welcomeMessage():
        print('Welcome to our organization')

employee1 = Employee('Maegor')
employee2 = Employee('Aegon')
employee1.displayEmployeeDetails()
employee2.displayEmployeeDetails()
#employee.welcomeMessage()