import re;

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def validate_email(email):
    if re.fullmatch(regex, email):
        print("email is valid")
    else:
         print("email is not valid")
    
email=input("enter the email\n")
validate_email(email)
  
regex= re.compile(r'[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})')

def validate_url(url):
    if re.fullmatch(regex, url):
        print("url is valid")
    else:
        print("url is not valid")
        
url=input("enter the url\n")
validate_url(url)        

regex= re.compile(r'([0-9]{10})')

def validate_number(number):
    if re.fullmatch(regex, number):
        print("number is valid")
    else:
        print("number is not valid")
        
number=input("enter the number\n")
validate_number(number)        
