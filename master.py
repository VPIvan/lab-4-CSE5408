#String to reverse
string_to_reverse = input("Enter string: ")
reversed_string = ''.join(reversed(string_to_reverse))
print(reversed_string)

#check if prime code
check_number = int(input("Enter a number to see if it is prime: "))
# If given number is greater than 1
if check_number > 1:

    # Iterate from 2 to n / 2
    for i in range(2, int(check_number/2)+1):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (check_number % i) == 0:
            print(check_number, "is not a prime number")
            break
    else:
        print(check_number, "is a prime number")

else:
    print(check_number, "is not a prime number")
