
def prime(nums):
    if nums < 2:
        return nums
    for i in range(2, nums):
        if nums % i == 0:
            print("Number is not a prime")
            return


    print("Number is prime")
def main():

    nums = int(input("Enter a number "))
    prime(nums)

main()