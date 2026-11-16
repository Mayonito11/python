a = int(input("enter first side:"))
b = int(input("enter second side:"))
c = int(input("enter third side:"))

def right_triangle(a, b, c):
    if a*a == b*b + c*c:
        print("triangle is right_angled")
    elif b*b == a*a + c*c:
        print("triangle is right_angled")
    elif c*c == a*a + b*b:
        print("triangle is right_angled")
    else:
        print("triangle is not right_angled")

right_triangle(a, b, c)
