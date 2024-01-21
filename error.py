try:
    file=open("dat.txt",'r')
    for i in file:
        print(i)

except Exception:
    print("file not found")