import logging

logging.basicConfig(filename="assertDemo.log",level=logging.DEBUG)

try:
    r = int(input("Enter a number less than 5: "))
    assert r < 5,"Wrong number"
    print("Number is:",r)
    logging.info("Number satisfies the conditions")
except AssertionError as msg:
    print("Follow the rules, Rogue!",msg)
    logging.error("Number doesn't satisfy the conditions")
print("After assert")