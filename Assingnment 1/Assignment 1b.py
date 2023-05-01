a = int (input("Enter a: "))
b = int (input ("Enter b: "))
c = int (input("Enter c: "))
if a < b+c and b < a+c and c < a+b:
    print ("The possibility of drawing a triangle: Possible")
else:
    print ("The possibility of drawing a triangle: impossible")