from abc import abstractmethod, ABC
class Android(ABC):
    def __init__(self,version,year):
        self.version=version
        self.year=year
        
    def thirdPartyInstallation(self,choice):
        if(choice=='y' or choice=='Y'): print('Allowing Third Party Installation')
        else: print("Third Party Installation Blocked")
    
    def boot(self):
        print("Booting Device")
        
    @abstractmethod
    def signUp(self):
        pass

class Phone(Android):
    def __init__(self,name,OS_Codename,features,version,year):
        Android.__init__(self, version, year)
        self.name=name
        self.OS_Codename=OS_Codename
        self.features=features
        
    def thirdPartyInstallation(self,choice):
        choice=input("Install a third party app? Are you sure?(Y/N)")
        if(choice=='y' or choice=='Y'): print('Allowing Third Party Installation')
        else: print("Third Party Installation Blocked")

class Tablet(Android):
    def __init__(self,name,OS_Codename,features,version,year):
        super().__init__(version, year)
        self.name=name
        self.OS_Codename=OS_Codename
        self.features=features
        self.readingMode=False
        
    def read(self,readingMode):
        if(readingMode):
            print('Reading Mode turned ON')
            print('Welcome and enjoy reading your favourite books')
        else: print('Reading Mode is OFF')

ph=Phone("Vivo V5","Marshmellow","Redesigned Multitasking Layout","6.1","2016")
print(ph.name)
print(ph.OS_Codename)
print(ph.version)
print(ph.features)
print(ph.year)
ph.thirdPartyInstallation('n')
ph.boot()