class ObjectCounter:
    NoOfObjects=0
    animeNames=[]
    
    def __init__(self,animeName):
        self.animeNames.append(animeName)
        ObjectCounter.NoOfObjects+=1
    
    def display(self):
        print(self.animeNames)
    
    @staticmethod
    def dispNoOfObjs():
        print("Number of objects in the class is:",ObjectCounter.NoOfObjects)
        print()

ichi=ObjectCounter("Akame Ga Kiru!")
ni=ObjectCounter("Death Note")
ni.display()
ObjectCounter.dispNoOfObjs()

san=ObjectCounter("Angel Beats")
yon=ObjectCounter("Shingeki no Kyojin")
go=ObjectCounter("Psycho Pass")
yon.display()
ObjectCounter.dispNoOfObjs()