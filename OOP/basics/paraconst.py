class Course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    
    def avgR(self):
        addtn=sum(self.ratings)
        avg=float(addtn/len(self.ratings))
        return avg

c1=Course(input("Enter Course name: "),[1,2,3,4,5])
c2=Course(input("Enter Course name: "),[2,2,3,2,5])

print("\nCourse "+c1.name+" is rated",c1.avgR())
print("Course "+c2.name+" is rated",c2.avgR())