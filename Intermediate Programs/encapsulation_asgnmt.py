class Patient:
    def setID(self,id): #@ReservedAssignment
        self.__id=id
    def setName(self,name):
        self.__name=name
    def setSSN(self,ssn):
        self.__SSN=ssn
        
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def getSSN(self):
        return self.__SSN

p1=Patient()
p1.setID(2134)
p1.setName("Paul Wesley")
p1.setSSN(21239854)

print("Patient ID:",p1.getID())
print("Patient Name: "+p1.getName())
print("Patient SSN:",p1.getSSN())