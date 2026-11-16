#list
students=["rohan","ihan","keshav"]
students.append("anu")
students.insert(1,"mayu")
students.remove("keshav")
students.pop(0)
students.sort()
print("list:",students)
#tuple
marks=(85,90,85,75)

print("count:", marks.count(85))
print("index:", marks.index(90))
print("lenght:",len(marks))
print("maximum:",max(marks))
print("minimum:",min(marks))
 #dictionary
student={"name":"mayu","age":17,"course":"cse"}
print(student.get("name"))
print(student.keys())
print(student.values())
student.update({"age":18})
student.update({'name':"mayuresh3141"})
student.pop("course")
print("dictionary",student)