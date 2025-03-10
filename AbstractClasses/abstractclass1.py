from abc import ABC, abstractmethod

class AbstractClass(ABC):
    
    @abstractmethod
    def abstract_method(self):
        pass
    
    def non_abstract_method(self):
        print("This is a Non-Abstract Method")

# AbstractClass obj = AbstractClass()  --> Cannot create object for Abstract Class
