def palindrome(num):
    rev = 0
    
    while(num!=0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10

    return rev

def main():
    num = int(input("Enter a number... "))
    result = palindrome(num)
    if num == result:
        print("Number is palindrome")
    else:
        print("number is not a palindrome")

main()
