from abc import ABC, abstractmethod
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling through HP Laptop screen")
    
class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling through Dell Laptop screen")
    
class HPNotebook(HP):
    def scroll(self):
        super().scroll()

    def click(self):
        print("Tapping an element on HP Notebook screen")
    
class DellNotebook(Dell):
    def scroll(self):
        super().scroll()

    def click(self):
        print("Tapping an element on Dell Notebook screen")

hp=HPNotebook()
hp.scroll()
hp.click()
print()
dell=DellNotebook()
dell.scroll()
dell.click()