n=int(input("how many students:"))
names=[]
marks=[]
for i in range(n):
    n_1=str(input("enter the names:"))
    m=input("enter the marks:")
    names.append(n_1)
    marks.append(m)
print(max(marks))
marks.index(max(marks))
print(names[marks.index(max(marks))],"is the highest mark")

