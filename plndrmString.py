def palindromestring(para):
    length = len(para)

    

    for i in range(length // 2):
        if para[i] != para[length-i-1]:
            return False
        
    return True
    



def main():
    para = (input("Enter a string..."))

    result = palindromestring(para)
    if para == result:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")
main()
