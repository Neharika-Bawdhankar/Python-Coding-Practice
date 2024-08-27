class Employee:
    
    def __init__(self,name,age) -> None:
        print("Hello! how are you feeling today?")
        
    def empdetails(self,name,age):
        print("Hello!", self.name, "\nYour age is", self.age, )
        
p = Employee("Neharika", 32)
p.empdetails()