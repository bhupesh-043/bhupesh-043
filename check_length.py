def check_length():

    lst = ["asa", "ab", "a", "fds", "gres", "gresd", "fesfd"]

    result = []

    length = len(lst)

    for i in range(length):
        if len(lst[i]) >=3 and len(lst[i]) <=5:
            result.append(lst[i])

    print(result)
check_length()