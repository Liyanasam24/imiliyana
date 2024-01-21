student={
    "name": "sujith",
    "age": "20",
    "major": "computer science",
    "gpa": " 8.9"
}
#accesing values in the dictionary
print("Name:",student["name"])
print("Age:",student["age"])
print("Major:",student["major"])
print("GPA:",student["gpa"])
#modifying values in the dictionary
student["age"]=21
student["gpa"]=8.89
print("updated age:",student["age"])
print("updated GPA:",student["gpa"])
student["year"]="major"
print(["updated student dictionary:",student])
#removing a key-value pair from the dictionary
del student["major"]
print("Student dictionary after removing 'major':",student)
#checking if a key exists in the dictionary
print(("Does 'major' exist in the dictionary?","major" in student))
print(("Does 'name' exist in the dictionary?","name" in student))
#getting all the keys and values from the dictionary
keys=student.keys()
values=student.values()
print("keys:",values)
print("values:",values)
#iterating over the dictionary
print("Iterating over the dictionary:")
for key,value in student.items():
    print(key+":",value)
    








