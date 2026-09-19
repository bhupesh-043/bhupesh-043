num = [1, 3, 3, 2, 3, 2, 4, 5, 5]

lst = []

for i in num:
    if i not in lst:
        lst.append(i)

print(lst)


#................Different way to remove duplicates values................
num1  = [set(num)]

print(num1)