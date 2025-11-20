Name - Ayush Dubey
Enrollment Number - 0157CS231051
Batch - 6
Batch Time - 12:10 PM

1. Write a program to check whether a number is positive, negative, or zero.

Ans - num = int(input("Enter the number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


2.Write a program to check whether a number is even or odd. 

Ans- num = int(input("Enter the number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

                

3. Write a program to check if a given year is a leap year or not. 

Ans- year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

4. Write a program to find the greatest of two numbers. 

Ans- num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

if num1 > num2:
    print(num1)
else:
    print(num2)


5. Write a program to check whether a person is eligible to vote (age >= 18). 

Ans-age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote ")
else:
    print("You are not eligible to vote ")


6. Write a program to check whether a given character is a vowel or consonant. 

Ans-ch = input("Enter a character: ")


if len(ch) == 1 and ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print( "is a Vowel ")
    else:
        print( "is a Consonant ")
else:
    print("Please enter a single alphabet character ")


7. Write a program to check if a number is divisible by 5. 

Ans-num = int(input("Enter a number: "))

if num % 5 == 0:
    print(num, "is divisible by 5 ")
else:
    print(num, "is NOT divisible by 5 ")


8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit 
number.  

Ans- num = int(input("Enter a number: "))

if num < 10:   
    print(num, "is one digit")
elif num < 100: 
    print(num, "is two digits")
else:  
    print(num, "is more than two digits")


 
9. Write a program to check whether a student has passed or failed (passing marks = 40). 

Ans- marks = int(input("Enter student's marks: "))

if marks >= 40:
    print("The student has passed ")
else:
    print("The student has failed ")


10. Write a program to find whether the entered number is a multiple of both 3 and 7. 

Ans- num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print(num, "is a multiple of both 3 and 7 ")
else:
    print(num, "is NOT a multiple of both 3 and 7 ")


11. Write a program to find the greatest among three numbers. 

Ans- num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the greatest")
else:
    print(num3, "is the greatest")


12. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+). 

Ans- age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
else:
    print("Senior")


13. Write a program to assign grades based on marks: 
90-100: A,  
75-89: B,  
50-74: C,  
35-49: D,  
<35: Fail. 

Ans- marks = int(input("Enter marks: "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks <= 89:
    print("Grade: B")
elif 50 <= marks <= 74:
    print("Grade: C")
elif 35 <= marks <= 49:
    print("Grade: D")
else:
    print("Grade: Fail")


14. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides. 

Ans- a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


15. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.

Ans- ch = input("Enter a character: ")

if ch.isupper():
    print(ch, "is an uppercase letter")
elif ch.islower():
    print(ch, "is a lowercase letter")
elif ch.isdigit():
    print(ch, "is a digit")
else:
    print(ch, "is a special symbol")

    
16. Write a program to calculate electricity bill based on units: 
Up to 100 units: ₹5 per unit, 
101–200 units: ₹7 per unit, 
Above 200 units: ₹10 per unit. 

Ans- units = int(input("Enter Units: "))

if units < 100:
    bill = units * 5
elif units < 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print( bill)

    
17. Write a program to determine the largest of four numbers using nested if. 

Ans-num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            largest = num1
        else:
            largest = num4
    else:
        if num3 > num4:
            largest = num3
        else:
            largest = num4
else:
    if num2 > num3:
        if num2 > num4:
            largest = num2
        else:
            largest = num4
    else:
        if num3 > num4:
            largest = num3
        else:
            largest = num4

print("The largest number is:", largest)

    
18. Write a program to check if a given year is a century year and also a leap year. 

Ans- year = int(input("Enter a year: "))

if year % 100 == 0:
    print(year, "is a century year.")
    if year % 400 == 0:
        print(year, "is also a leap year ")
    else:
        print(year, "is not a leap year ")
else:
    print(year, "is not a century year.")
    if year % 4 == 0:
        print(year, "is a leap year ")
    else:
        print(year, "is not a leap year ")


19. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), 
Obese (30+). 

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")


20. Write a program to display the smallest number among three using nested if.

Ans- num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

smallest = num1

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

print("The smallest number is:", smallest)


21. Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: 
sum of cubes of digits equals the number itself. Example: 153 => 1³+5³+3³ = 153). 

Ans-print("Armstrong numbers between 100 and 999 are:")

for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    cube_sum = hundreds**3 + tens**3 + units**3

    if cube_sum == num:
        print(num)

    
22. Write a program to generate and display the first n prime numbers using a for loop. 

Ans- n = int(input("Enter how many prime numbers you want: "))

num = 2   
primes_found = 0

for num in range(2, 1000):  
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        primes_found += 1
        if primes_found == n:   
            break

                                                                             
23. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits 
should not exceed 10. 

Ans-for num in range(1, 501):
    if num % 3 == 0:
        digit_sum = sum(int(d) for d in str(num))  
        if digit_sum <= 10:
            print(num)

    
24. Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4: 
* 
*** 
***** 
******* 

Ans-n = int(input("Enter height of pyramid: "))

for i in range(n):
    stars = 2 * i + 1  
    print("*" * stars)

25. Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) 
using a for loop. 

Ans-string = input("Enter a string: ").lower()

alphabets = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for ch in alphabets:
    if ch not in string:
        is_pangram = False
        break

if is_pangram:
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")

    
26. Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime 
numbers with a difference of 2, e.g., (3,5), (11,13)). 

Ans- 
print("Twin primes between 1 and 100 are:")
for n in range(2, 99):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        for j in range(2, n+2):
            if (n+2) % j == 0:
                break
        else:
            print(f"({n}, {n+2})")

    
27. Write a program that accepts a number from the user and prints whether it is a Harshad number (number 
divisible by the sum of its digits) using a for loop. 

Ans-num = int(input("Enter a number: "))
sum_digits = 0
for d in str(num):  
    sum_digits += int(d)
if num % sum_digits == 0:
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")

    
28. Write a program to generate Pascal’s Triangle up to n rows using a for loop. 

Ans-n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

                                                                      
29. Write a program using a for loop to display the sum of the series: 
1² + 2² + 3² + ... + n² 

Ans- n = int(input("Enter the value of n: "))
sum = 0

for i in range(1, n + 1):
    sum += pow(i, 2)

print("Sum of squares =", sum)
         
30. Write a program that accepts a number from the user and prints whether it is a Strong number (sum of 
factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145. 

Ans-num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10
    
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_fact += fact
    temp //= 10
if sum_fact == num:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")


 31. Write a program using a while loop to find the reverse of a number and check if the reversed number is 
prime. Example: Input = 73 → Reverse = 37 → Prime. 

Ans-n = int(input("Enter a number under 100: "))

rev = 0
temp = n
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed number:", rev)

if rev > 1:
    for i in range(2, rev):
        if rev % i == 0:
            print(rev, "is not a prime number")
            break
    else:
        print(rev, "is a prime number")
else:
    print(rev, "is not a prime number")

32. Write a program that continues to accept numbers from the user until the sum of digits of all numbers 
entered becomes greater than 100. 

Ans-total_sum = 0

while total_sum <= 100:
    n = int(input("Enter a number: "))
    digit_sum = 0
    temp = n
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    total_sum += digit_sum
    print("Sum of digits of", n, "=", digit_sum)
    print("Total sum so far =", total_sum)

print("Stopped because total sum of digits exceeded 100.")

     
33. Write a program using a while loop to check whether a number is a Duck number (a number containing zero 
but not starting with zero, e.g., 202, 1203). 

Ans-n = input("Enter a number: ")
if n[0] != "0" and "0" in n:
    print("Duck number")
else:
    print("Not a Duck number")

    
34. Write a program using a while loop to accept a number and check if it is a Happy number. (A number is 
happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a 
happy number. 

Ans-n = int(input("Enter a number: "))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    s = 0
    while n > 0:
        d = n % 10
        s += d * d
        n //= 10
    n = s
if n == 1:
    print("Happy number")
else:
    print("Not a happy number")

                                                                                              
35. Write a program using a while loop to find the largest prime factor of a given number. 

Ans-n = int(input("Enter a number: "))
i = 2
largest = 1
while i <= n:
    if n % i == 0:
        largest = i
        n //= i
    else:
        i += 1
print("Largest prime factor:", largest)

                                                                                              
36. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.

Ans-while True:
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome entered:", s)
        break
    else:
        print("Not a palindrome, try again.")

                                                                                              
37. Write a program using a while loop to compute the sum of digits of a number until the result becomes a 
single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2. 

Ans-n = int(input("Enter a number: "))
while n > 9:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s
print("Digital root:", n)

                                                                                              
38. Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even 
=> n/2, if odd => 3n+1. Continue until n=1). 

Ans-n = int(input("Enter a number: "))
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(1)

    
39. Write a program using a while loop to accept a number and check whether it is a Kaprekar number. 
(Kaprekar number: if square of the number can be split into two parts whose sum equals the number. 
Example: 45²=2025 => 20+25=45). 

Ans-n = int(input("Enter a number: "))
sq = str(n * n)
d = len(str(n))
left = sq[:-d] or "0"
right = sq[-d:]
if int(left) + int(right) == n:
    print("Kaprekar number")
else:
    print("Not a Kaprekar number")

    
40. Write a program to simulate an ATM machine using a while loop where a user can: 
• Check balance 
• Deposit money 
• Withdraw money (only if balance is sufficient) 
• Exit 
Continue until the user chooses to exit.   

Ans-balance = 0
while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Balance:", balance)
    elif choice == 2:
        amt = int(input("Enter amount: "))
        balance += amt
    elif choice == 3:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid")

    