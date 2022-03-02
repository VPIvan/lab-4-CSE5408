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



#convert to military time
time_to_convert = raw_input("Enter a 12 hour time to covert to 24 hour(in the following format 00:00:00 AM/PM): ")
def convert24(str1):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

# Driver Code
print(convert24(time_to_convert))
