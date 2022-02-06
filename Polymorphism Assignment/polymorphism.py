#Define parent class
class downtownStores:
    #Define the attributes of the class
    region = 'westcoast'
    size = 'large'

    #function
    def myMethod1(self):
        print("Welcome to our store!")
    

#Define child class
class employee(downtownStores):
    base_pay = 11.00
    department = 'General'

    #polymorphism function
    def myMethod1(self):
        print("Welcome back!")

store = downtownStores()
store.myMethod1()

paydepartment = employee()
paydepartment.myMethod1()
    
