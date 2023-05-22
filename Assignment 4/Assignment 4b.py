while True:
    a = int(input('First Coefficient   :'))
    b = int(input('Second Coefficient  :'))
    c = int(input('Third Coefficient   :'))
    print(f'your equestion is :',(a),'x^2 +',(b),'x +',(c))
    correct = input('is it correct ? ( yes or no) : ')

    if correct =='yes':

        delta = (b**2) - (4*a*c)

        x1 = ((-b) + (delta**(1/2)))/ (2*a)
        x2 = ((-b) - (delta**(1/2))) / (2*a)

        print('The answers are :',(x1), 'and', (x2))

    else:
        print('Correct your Coefficients :D')
        pass