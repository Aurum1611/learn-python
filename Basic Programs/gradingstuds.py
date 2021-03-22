def grade(avg):
    if avg<=59: return "C"
    elif avg<=69: return "B"
    else: return "A"

math,phys,chem=[float(x) for x in input("Enter marks scored in Maths, Physics, Chemistry resp. with each value separated by spaces: ").split()]
avg=(math+phys+chem)/3
if math<35 : print("The student has failed in Maths and hence, has failed the examination.")
elif phys<35 : print("The student has failed in Physics and hence, has failed the examination.")
elif chem<35 : print("The student has failed in Chemistry and hence, has failed the examination.")
else: print("The student has passed with the grade",grade(avg))
