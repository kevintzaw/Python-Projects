from abc import ABC, abstractclassmethod

class food(ABC):
    def edibility(self, size):
        print("This food is: ",size)
#this function is telling us to pass in an argument
    @abstractclassmethod
    def eaten(self, size):
        pass

class satisfied(food):
#here I've defined how to implement the eaten function from its parent edibility class
    def eaten(self, size):
        print('Youve eaten this {} '.format(size))

obj = satisfied()
obj.edibility("apple")
obj.eaten("apple")