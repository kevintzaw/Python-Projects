#Define parent class
class westcoastEmployees:
    #Define the attributes of the class
    region = 'westcoast'
    company = 'westcompany'

#Define child class
class Manager(westcoastEmployees):
    base_pay = 11.00
    department = 'General'

#Second child class
class vicePresident(westcoastEmployees):
    meetings = 'highlevel'
    employees = 20
