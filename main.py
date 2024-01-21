import re
str= input("enter gmail:")
match=re.search(r'\w+@\w+',str)
if match:
    print("your gmail is correct",match.group())
else:
    print("not match")







