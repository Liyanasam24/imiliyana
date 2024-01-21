class student:
    "common base class for all students"
    def getdata(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("ROLL NO:",self.rollno)
        print("NAME:",self.name)
        print("COURSE:",self.course)
class test(student):
    def getmarks(self,marks):
        self.marks=marks
    def displayMarks(self):
        print("TOTAL MARKS:",self.marks)
r=int(input("enter roll number:"))
n=input("enter name:")
c=input("enter course name:")
m=int(input("enter marks:"))
print("result")
stud1=test()
stud1.getdata(r,n,c)
stud1.getmarks(m)
stud1.displaystudent()
stud1.displayMarks()

