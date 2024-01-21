string=input("Enter a string:").split()
words=[]
for word in string:
    words.append(word[::-1])
    print(word,end=" ")
