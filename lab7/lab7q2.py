"""
@author: vinay
"""
class Employee: # This represents class
    
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def changeSalary(self,salary):
        update = int(salary) + 60
        return update
#    def changeDept(self,y):
        
    def __str__(self,):
        return f"{self.name} manages {self.number} employee"
    
import csv

with open('employees.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    f = open('employee_updated.csv', 'w', newline="")
    writer = csv.writer(f)
    # Each value in dictionary is an individual instance of class
    dict_of_employees_object = {}
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            writer.writerow(row)
            continue
        else:
            dict_of_employees_object[row[1]] = Employee(row[1],0)
            date_of_hire = row[5]
            dummy = date_of_hire.split('-')
            if int(dummy[2]) < 3:
#                row[1] = Employee(row[1])
                row[7] = dict_of_employees_object[row[1]].changeSalary(row[7])
        writer.writerow(row)
csv_file.close()
f.close()
def employee_manage(row):
    employee_manage = {}
    with open('employees.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row1 in csv_reader:
            if row[0] == row1[9]:
                if row[1] in employee_manage:
                    employee_manage[row[1]] += 1
                else:
                    employee_manage[row[1]] = 1
        return employee_manage
    csv_file.close()
    
with open('employees.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
#    manage = {}
    for row in csv_reader:
        dummy = employee_manage(row)
        if bool(dummy) == False:
            pass
        else:
            for key,value in dummy.items():
                if value >3:
                    print(Employee(key,value))
#        manage.update(dummy)
csv_file.close()