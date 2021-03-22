class Employee:
    def __init__(self):
        self.__id=213;
        self.__name="Damon";
        self.__salary=234492;
        
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary

card=Employee()
print(card.getID(),card.getName(),card.getSalary(),"\n")
print(card._Employee__id,card._Employee__name,card._Employee__salary)