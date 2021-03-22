class Programmer:
    def __init__(self,name,salary,tech):
        self.name=name
        self.salary=salary
        self.tech=tech
    
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    def setTech(self,tech):
        self.tech.append(tech)
    
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    def getTech(self):
        return self.tech
    
    def display(self):
        print(self.getName(),self.getSalary(),self.getTech())

P1=Programmer("Akane",40000,["Java","Kotlin"])
P2=Programmer("Chitanda",20000,["HTML5","CSS3","JS","SQL"])

P1.display()
P2.display()

P1.setTech("SQL")
P1.setTech("XML")
P1.setSalary("45000")

P2.setTech("Python")
P2.setSalary("27000")

print()
P1.display()
P2.display()