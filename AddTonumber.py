# write a program to add to number 

# num1 = input("Enter first number ")
# num2 = input("Enter second number ")

# sum = int(num1) + int(num2);

# print("Sum of two number " ,sum )

# write a program to find a maximum of two numbers

# a = int(input("Enter a number = "))
# b= int(input("Enter a number = "))

# if a>b :
#     print("a is greater than b  " ,a)
# elif b>a  :
#     print("b is greater than a ", b)


# num =int(input("Enter number = "))
# fact =1
# while num >1:
#     fact *=num
#     num-=1  
# print(fact)

# a =23
# b=45
# c = a +b 
# d =a-b
# e =a/b
# f=a*b
# print(c,d,e,f)

# name = input("Enter your name")

# print("Hello " + name )

# numberToCheckIsEvenOrOdd = int(input("Enter a number to check is even or odd "))

# if numberToCheckIsEvenOrOdd%2==0 :
#     print("The given number is even")
# else:
#     print("The given number is odd")    


# for number in range(3,16,3):
#     print(number)
    
# fruits = ["Banana","apple","kiwi","orange"]

# for fruit in fruits:
#     print(fruit)

# def sum(a,b):
#     c= a+b
#     return c
# print(sum(2,5)) 

def palindrome(x):
    string = str(x)
    reverseString = string[::-1]
    print(reverseString)
    if string==reverseString:
        print(True)
    else :
        print(False)

palindrome(123)        