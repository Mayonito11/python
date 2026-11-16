a =int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
 print("largest number  is:",a)
elif b>a and b>c:
 print("largest number is:",b)
else:
 print("largest number is :",c)
 #display of respective grade based upon marks
 marks=int(input("enter math marks:"))
if marks>=90 and marks<=100:
 print("grade:O")
elif marks>=80 and marks<=89:
 print('grade:A+')
elif marks>=70 and marks<=79:
 print("grade:A")
elif marks>=60 and marks<=69:
 print("grade:B")
elif marks>=50 and marks<=59:
 print("grade:C")
elif marks>=40 and marks<=49:
 print("grade:D")
else:
 print("grade:F")    
