#Defining a class
class protected:
    
    #protected data members
    _name = "Kevin"
    _number = 23

    #private variables
    __privateVar = 27;

    #public member function
    def displayNameandNumber(self):

        #accessing protected data members
        print("Name: ", self._name)
        print("Roll: ", self._number)

        #accessing private variable
        print("Amount is ", protected.__privateVar)

#creating object within a class
obj = protected()

#calling public member
#functions of the class
obj.displayNameandNumber()

