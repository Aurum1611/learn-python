import re
str = "It's nothing but a G thang. Ahh! I just feel sad and I don't wanna feel that way."

result=re.search(r'n\w\w\s', str)
if result != None:
    print(result.group(),result.span(),"\n\n",result,"\n\n")
else:
    print(result,"\n\n")

result=re.findall(r'f\w\w\w', str)
print(result,"\n\n")

result=re.match(r'I\w', str)
if result != None:
    print(result.group(),result.span(),"\n\n",result,"\n\n")
else:
    print(result,"\n\n")

result=re.split(r'\s', str)
print(result,"\n\n")

result=re.sub(r'I', 'me', str)
print(result,"\n\n")

''' Using Quantifiers '''
result=re.findall(r'f\w{0,2}', str)
print(result,"\n\n")

str="""19 Birthdays: 5 Katie- 12/4/1999, Jack- 31/11/1993, Mia- 14/9/1998
Hello world KKK sucks 16/12/1944 ggdg yewg kjhgeqw 7iyyqn3,2 uyfdgwuib kjwendhuhu23mndqwe
52/4/5055"""
result=re.findall(r'\d{1,2}/\d{1,2}/\d{4}', str)
print(result,"\n\n")

result=re.search(r'\A19', str)
if result != None:
    print(result.group(),result.span(),"\n\n",result,"\n\n")
else:
    print(result,"\n\n")

result=re.findall(r'\d*$', str)
print(result,"\n\n")

result=re.findall(r'[^\W]', str)
print(result,"\n\n")

result=re.findall(r'[0-9]', str)
print(result,"\n\n")

result=re.search(r'([a-z]+|[2-5]+)', str)
if result != None:
    print(result.group(),result.span(),"\n\n",result,"\n\n")
else:
    print(result,"\n\n")
