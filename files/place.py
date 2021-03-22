class Place:
    def __init__(self,name,countryName,continent):
        self.name=name
        self.countryName=countryName
        self.continent=continent

    def display(self):
        print(self.name+","+self.countryName+","+self.continent)