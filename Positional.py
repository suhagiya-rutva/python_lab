#basic positional argument
def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b 
result = add(2,5)
print("sum=",result)

#student information
def student_info (name,roll,marks):
    print("Name:",name)
    print("Roll No:", roll)
    print("Marks:", marks)
student_info("Ravi", 101, 85)

#simple interset
def simple_interest(p,r,n):
    si = (p*r*n)/100
    print("simple interest:",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)

#Area of circle
def ar_circle(r):
    a_circle=3.14*r*r
    print("Area of Circle:",a_circle)
ar_circle(1.5)
ar_circle(4)

#check number positive negative or zero
def check_value(no):
    if(no>0):
        print("Positive")
    elif(no<0):
        print("negative")
    else:
        print("Zero")
check_value(0)
check_value(90)
check_value(-15)

#odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value{no} is even")
    else:
          print(f"value{no} is odd")
odd_even(50)
odd_even(15)

#arithmatic operation substraction
def addition(a,b):
    add = a+b
    print("Addition of two values",add)
addition(50,10.5)
addition(100,200)