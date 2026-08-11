# Write a program to find the sum of digits of a number using a while loop.

num = input("Enter a Number: ")          #1234

if num.isdigit():
    num = int(num)

    sum = 0

    while num > 0:                      #1234>0
        digit = num % 10                #1234%10(remainder)= 4,3,2,1
        sum = sum + digit               #sum=0+4= 4,7,9,10
        num = num // 10                 #num=1234//10= 123,12,1

    print("Sum of Digits =", sum)

else:
    print("Warning! Entered number must be an integer.")
    
