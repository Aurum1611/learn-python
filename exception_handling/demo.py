import logging

logging.basicConfig(filename="sanFile.log",level=logging.DEBUG)

try:
    f = open("ichiFile","w")
    a,b = [int(x) for x in input("Enter two numbers: ").split()]
    f.write("Quotient is: %.3f"%(a/b))
    logging.info("Division carried out")
except:
    print("Can't divide by zero")
    logging.error("An error has occured")
else:
    print("You have entered a non zero number.")
finally:
    f.close()
    print("File closed")
print("Code after the exception")