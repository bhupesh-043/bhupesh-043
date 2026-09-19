
def reverse(num):

    rev = 0
    while num!=0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev

def main():
    num = int(input("Enter a number... "))

    result = reverse(num)
    print("Reverse number", result)
main()