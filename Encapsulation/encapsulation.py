#Defining a class
class protected:
    
    #protected data members
    _name = "Kevin"
    _number = 23

    #public member function
    def displayNameandNumber(self):

        #accessing protected data members
        print("Name: ", self._name)
        print("Roll: ", self._number)

#creating object within a class
obj = protected()

#calling public member
#functions of the class
obj.displayNameandNumber()

