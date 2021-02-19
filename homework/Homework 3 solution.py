"""
Day-4:
Write two functions.
The name of the first function is prime first.
The name of the second function is prime_second.
You must use these two functions inside the for loop. Ensure that the for loop takes values between 0-1000.
Press the prime numbers between 0-500 on the screen with the prime_first function.
Press the prime numbers between 500-1000 on the screen with the prime_second function.
"""

def prime_first(x):
    control = 0
    if (x % 2) != 0:
        k = 2
        while k < x:
            if x % k != 0:
                k += 1
            else:
                control += 1
                k += 1
        if control == 0:
            print(x)

def prime_second(x):
    control = 0
    if (x % 2) != 0:
        j = 2
        while j < x:
            if x % j != 0:
                j += 1
            else:
                control += 1
                j += 1
        if control == 0:
         print(x)

print("2")
for i in range(3, 1001):
    if i <= 500:
        prime_first(i)
    else:
        prime_second(i)
