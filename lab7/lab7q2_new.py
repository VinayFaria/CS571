# @author: vinay
import csv

class Employee:
    # class variable are same for each instance and are outside method
    
    # These are regular method
    # These are class method
    # These are static method
    def __init__(self, employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id):
        # init method runs every time new instance is created
        # this are instance variable
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.hire_date = hire_date
        self.job_id = job_id
        self.salary = salary
        self.manager_id = manager_id
        self.department_id = department_id
    """
    def __str__():
        
    def changeDept():
    """  
    # this is methods of class
    def changeSalary(self, salary):
        self.salary = int(self.salary) + 60    
    @classmethod
    def new_employee(cls, row):
        employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]
        return cls(employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)

with open('employees.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
#    f = open('employee_updated.csv', 'w', newline="")
#    writer = csv.writer(f)
    list_of_employees_object = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
#            writer.writerow(row)
            continue
        else:
            list_of_employees_object.append(Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            dummy = row[5].split('-')
            if int(dummy[2]) < 3:
                list_of_employees_object[line_count-1].changeSalary(int(list_of_employees_object[line_count-1].salary))
            line_count += 1
csv_file.close()
print(list_of_employees_object[6].salary)