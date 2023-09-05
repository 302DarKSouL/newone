import re;

regex= re.compile(r'([0-9]{10})')

def validate_number(number):
    if re.fullmatch(regex, number):
        print("number is valid")
    else:
        print("number is not valid")
        
number=input("enter the number\n")
validate_number(number)        
