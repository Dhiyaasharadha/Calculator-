import math
def calc():
    print('***** MENU *****')
    print(' 1.ADD \n 2.SUBTRACT \n 3.MULTIPLY \n 4.DIVIDE \n 5.SQUARE OF NUMBER \n 6.FACTORIAL \n 7.FLOOR DIVISION \n 8.REMAINDER AFTER DIVISION \n 9.POWER FUNCTION \n 10.SQAURE ROOT \n 11.GREATEST COMMON DIVISOR \n 12.SIN \n 13.COS \n 14.TAN\n 15.ABSOLUTE VALUE OF THE NUMBER\n')
    x= int(input('ENTER THE NUMBER FOR CALCULATION FROM THE MENU:'))
    if x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        if x==1:
            a=int(input('ENTER FIRST NUMBER:'))
            b=int(input('ENTER SECOND NUMBER:'))
            print('THE ANSWER IS:', a+b)
        elif x==2:
            a=int(input('ENTER FIRST NUMBER:'))
            b=int(input('ENTER SECOND NUMBER:'))
            print('THE ANSWER IS:', a-b)
        elif x==3:
            a=int(input('ENTER FIRST NUMBER:'))
            b=int(input('ENTER SECOND NUMBER:'))
            print('THE ANSWER IS:', a*b)
        elif x==4:
            a=int(input('ENTER FIRST NUMBER:'))
            b=int(input('ENTER SECOND NUMBER:'))
            if b==0:
                print("### ZERO DIVISION ERROR ###")
            else:
                print('THE ANSWER IS:', a/b)
        elif x==5:
            a=int(input('ENTER THE NUMBER:'))
            print('THE ANSWER IS:', a*a)
        elif x==6:
            a=int(input('ENTER THE NUMBER:'))
            c=1
            for i in range(1,a+1):
                c*=i
            print('THE ANSWER IS:', c)    
        elif x==7:
            a=int(input('ENTER FIRST NUMBER:'))
            b=int(input('ENTER SECOND NUMBER:'))
            print('THE ANSWER IS:', a//b)
        elif x==8:
            a=int(input('ENTER FIRST NUMBER:'))
            b=int(input('ENTER SECOND NUMBER:'))
            print('THE ANSWER IS:', a%b)
        elif x==9:
            a=int(input('ENTER THE BASE NUMBER:'))
            b=int(input('ENTER THE POWER WHICH HAST TO BE RAISED:'))   
            print('THE ANSWER IS:', math.power(a,b))
        elif x==10:
            a=int(input('ENTER THE NUMBER:'))
            print('THE ANSWER IS:', math.sqrt(a))
        elif x==11:
            a=int(input('ENTER FIRST NUMBER:'))
            b=int(input('ENTER SECOND NUMBER:'))
            print('THE ANSWER IS:', math.gcd(a,b))
        elif x==12:
            a=int(input('ENTER THE NUMBER:'))
            print('THE ANSWER IS:', math.sin(a))
        elif x==13:
            a=int(input('ENTER THE NUMBER:'))
            print('THE ANSWER IS:', math.cos(a))
        elif x==14:
            a=int(input('ENTER THE NUMBER:'))
            print('THE ANSWER IS:', math.tan(a))
        elif x==15:
            a=int(input('ENTER THE NUMBER:'))
            print('THE ANSWER IS:', abs(a))
    else:
        print('### INVALID CHOICE ###')
        
while True:
    print('PRESS 1 TO CALCULATE AND PRESS 2 TO EXIT CALCULATOR')
    y=int(input('ENTER YOUR CHOICE:'))
    if y==1:
        calc()
    elif y==2:
        print('--- THANK YOU ---')
        break
    else:
        print('### INVALID CHOICE###')